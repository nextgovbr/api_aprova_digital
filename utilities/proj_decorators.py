import functools
from fastapi import HTTPException
from utilities.proj_exceptions import ProcessoForadoPadrao, ProcessNotFound

def treat_proc_num_out_of_pattern(func):

    @functools.wraps(func)
    def wraped(*args, **kwargs):
        try:
            resp = func(*args, **kwargs)
            return resp
        except ProcessoForadoPadrao as e:
            raise HTTPException(400, detail = str(e))
    return wraped

def treat_proc_not_found(func):

    @functools.wraps(func)
    def wraped(*args, **kwargs):
        try:
            resp = func(*args, **kwargs)
            return resp
        except ProcessNotFound as e:
            raise HTTPException(404, detail = str(e))
    return wraped
