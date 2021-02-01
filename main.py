from fastapi import FastAPI
from utilities.my_tools import get_proc_aleatorio
from process_data.responsavel_imovel import dados_resps_imovel

app = FastAPI()

@app.get("/responsavel_imovel/")
def dados_responsavel():

    p = get_proc_aleatorio()

    return dados_resps_imovel(p)