from fastapi import FastAPI
from data import cursos
from fastapi import HTTPException
from fastapi import status
from models import Curso
from fastapi import Response
from fastapi import Path
from typing import Optional

app = FastAPI()


@app.get('/')
async def raiz():
    return {"msg": "FastAPI"}


@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(
        curso_id: int = Path(
            default=None,
            title='ID do curso',
            description='Deve ser 1 ou 2', ge=1, le=2)):
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


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe um curso com ID {curso_id}.')


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe um curso com ID {curso_id}.')


@app.get('/calculadora')
async def calculadora(n1: float, n2: float, n3: Optional[float] = None):
    """ http://localhost:8000/calculadora?n1=1&n2=3&n3=4
    """
    soma = n1 + n2
    if n3:
        soma = soma + n3
    return {'Soma:': soma}


if __name__ == '__main__':
    import uvicorn

    _host = '0.0.0.0'
    _port = 8000
    _debug = True

    uvicorn.run("main:app", host=_host, port=_port,
                log_level="info", debug=_debug, reload=True)
