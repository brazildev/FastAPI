from data import cursos
from models import Curso
from typing import Optional, Any, Dict, List
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import Depends
from db import fake_db

app = FastAPI(
    title='API GGS',
    version='Alfa',
    description='Descrição: API para estudo.'
)  # http://localhost:8000/docs


@app.get('/')
async def raiz():
    return {"msg": "FastAPI"}


@app.get('/cursos',
         summary='Retorna os cursos.',  # http://localhost:8000/docs#/default/get_cursos_cursos_get
         description='Retorna todos os cursos.',  # http://localhost:8000/redoc
         # response_model=Dict[int, Curso]
         response_model=List[Curso]
         )
async def get_cursos():
    return cursos


@app.get('/cursos2')
async def get_cursos2(db: Any = Depends(fake_db)):
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


@app.post('/cursos', status_code=status.HTTP_201_CREATED,
          response_model=Curso)  # http://localhost:8000/docs#/default/post_curso_cursos_post
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
async def calculadora(
        x_ggs: str = Header(default=None),  # key = x-ggs in Headers
        n1: float = Query(default=None, gt=4.0),
        n2: float = Query(default=None, gt=9.0),
        n3: Optional[float] = None
):
    """ http://localhost:8000/calculadora?n1=5&n2=10&n3=4
    """
    soma = n1 + n2
    if n3:
        soma = soma + n3
    print(f'X-GGS: {x_ggs}')
    return {'Soma:': soma}


if __name__ == '__main__':
    import uvicorn

    _host = '0.0.0.0'
    _port = 8000
    _debug = True

    uvicorn.run("main:app", host=_host, port=_port,
                log_level="info", debug=_debug, reload=True)
