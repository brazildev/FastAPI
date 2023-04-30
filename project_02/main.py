from fastapi import FastAPI
from data import cursos
from fastapi import HTTPException
from fastapi import status

app = FastAPI()


@app.get('/')
async def raiz():
    return {"msg": "FastAPI"}


@app.get('/cursos')
async def get_cursos() -> dict:
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int) -> dict:
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Não encontrado id do Curso.')


if __name__ == '__main__':
    import uvicorn

    _host = '0.0.0.0'
    _port = 8000
    _debug = True

    uvicorn.run("main:app", host=_host, port=_port,
                log_level="info", debug=_debug, reload=True)
