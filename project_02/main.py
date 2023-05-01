from fastapi import FastAPI
from data import cursos
from fastapi import HTTPException
from fastapi import status
from models import Curso

app = FastAPI()


@app.get('/')
async def raiz():
    return {"msg": "FastAPI"}


@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Não encontrado ID do Curso.')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso


if __name__ == '__main__':
    import uvicorn

    _host = '0.0.0.0'
    _port = 8000
    _debug = True

    uvicorn.run("main:app", host=_host, port=_port,
                log_level="info", debug=_debug, reload=True)
