from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(title="Recomenda Filmes API")

print("\n" * 50)

print("$$$$$$$\                                                                        $$\           ")
print("$$  __$$\                                                                       $$ |          ")
print("$$ |  $$ | $$$$$$\   $$$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\   $$$$$$$ | $$$$$$\  ")
print("$$$$$$$  |$$  __$$\ $$  _____|$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$ | \____$$\ ")
print("$$  __$$< $$$$$$$$ |$$ /      $$ /  $$ |$$ / $$ / $$ |$$$$$$$$ |$$ |  $$ |$$ /  $$ | $$$$$$$ |")
print("$$ |  $$ |$$   ____|$$ |      $$ |  $$ |$$ | $$ | $$ |$$   ____|$$ |  $$ |$$ |  $$ |$$  __$$ |")
print("$$ |  $$ |\$$$$$$$\ \$$$$$$$\ \$$$$$$  |$$ | $$ | $$ |\$$$$$$$\ $$ |  $$ |\$$$$$$$ |\$$$$$$$ |")
print("$$ |  $$ | \_______| \_______| \______/ \__| \__| \__| \_______|\__|  \__| \_______| \_______|")
print("                                                                                              ")
print("                                                                                              ")
print("                                                                                              ")
print("$$$$$$$$\ $$\ $$\                                          $$$$$$\  $$$$$$$\ $$$$$$\          ")
print("$$  _____|\__|$$ |                                        $$  __$$\ $$  __$$\\_$$  _|         ")
print("$$ |      $$\ $$ |$$$$$$\$$$$\   $$$$$$\   $$$$$$$\       $$ /  $$ |$$ |  $$ | $$ |           ")
print("$$$$$\    $$ |$$ |$$  _$$  _$$\ $$  __$$\ $$  _____|      $$$$$$$$ |$$$$$$$  | $$ |           ")
print("$$  __|   $$ |$$ |$$ / $$ / $$ |$$$$$$$$ |\$$$$$$\        $$  __$$ |$$  ____/  $$ |           ")
print("$$ |      $$ |$$ |$$ | $$ | $$ |$$   ____| \____$$\       $$ |  $$ |$$ |       $$ |           ")
print("$$ |      $$ |$$ |$$ | $$ | $$ |\$$$$$$$\ $$$$$$$  |      $$ |  $$ |$$ |     $$$$$$\          ")
print("\__|      \__|\__|\__| \__| \__| \_______|\_______/       \__|  \__|\__|     \______|         ")

print("\n" * 2)


# Loading nos Dados (Modelos)
print("[ Loading ] Carregando Modelos")
matriz_filmes = pd.read_pickle("./data/matriz_filmes.pkl")
tabela_filmes = pd.read_pickle("./data/tabela_filmes.pkl")
print("[ Loaded ] Modelos Carregados")

print("[ Create Dict ] Criando Dicionário de Filmes")
dict_id_para_titulo = pd.Series(tabela_filmes.title.values, index=tabela_filmes.movieId).to_dict()
print("[ Created ] Dicionário de Filmes Criado")

# Classes de Restrição para API
class AvaliacaoFilme(BaseModel):
    movie_id: int
    rating: float = Field(ge = 0, le = 5.0)

class PerfilUsuario(BaseModel):
    avalicoes: List[AvaliacaoFilme]


@app.post("/recomendar")
def recomendar(perfil: PerfilUsuario):
    novo_usuario = pd.DataFrame(0, index=[0], columns=matriz_filmes.columns)
    
    filmes_encontrados = 0
    filmes_ignorados = []

    for filme in perfil.avalicoes:
        titulo = dict_id_para_titulo.get(filme.movie_id)

        if titulo:
            if titulo in matriz_filmes.columns:
                novo_usuario[titulo] = filme.rating
                filmes_encontrados += 1
            else:
                filmes_ignorados.append(filme.movie_id)
        else:
            filmes_ignorados.append(filme.movie_id)
    
    if filmes_encontrados == 0:
        raise HTTPException(status_code=400, detail="Nenhum dos filmes avaliados foi encontrado na base de dados.")
    
    similaridades = cosine_similarity(novo_usuario, matriz_filmes)

    similaridades_usuarios = pd.Series(similaridades[0], index=matriz_filmes.index)
    indice_usuarios = similaridades_usuarios.sort_values(ascending=False).head(10).index
    usuarios_selecionados = matriz_filmes.loc[indice_usuarios]

    ranking_recomendacoes = usuarios_selecionados.mean().sort_values(ascending=False)

    filmes_vistos = [dict_id_para_titulo[i.movie_id] for i in perfil.avalicoes if dict_id_para_titulo.get(i.movie_id) in matriz_filmes.columns]

    recomendacoes = ranking_recomendacoes.drop(filmes_vistos, errors='ignore')

    return {
        "recomendacoes": recomendacoes.head(10).index.tolist(),
        "debug": {
            "usuarios_encontrados": len(usuarios_selecionados),
            "filmes_ignorados": filmes_ignorados,
        }
    }