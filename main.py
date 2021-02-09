from fastapi import FastAPI
from utilities.my_tools import get_proc_aleatorio, get_proc
from utilities.proj_decorators import treat_proc_num_out_of_pattern, treat_proc_not_found
from process_data.responsavel_imovel import dados_resps_imovel

app = FastAPI()

@app.get("/responsavel_imovel/{num_proc}")
@treat_proc_not_found
@treat_proc_num_out_of_pattern
def dados_responsavel(num_proc: str, json_alike : bool = True):

    if num_proc:
        p = get_proc(num_proc)
    else:
        p = get_proc_aleatorio()

    return dados_resps_imovel(p, json_alike = json_alike)