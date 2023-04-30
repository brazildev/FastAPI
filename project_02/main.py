from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {
        'titulo': 'Pro',
        'aulas': 112,
        'horas': 58
    },
    2: {
        'titulo': 'Algoritmo',
        'aulas': 87,
        'horas': 67
    }
}


@app.get('/')
async def raiz():
    return {"msg": "FastAPI"}


if __name__ == '__main__':
    import uvicorn

    _host = '0.0.0.0'
    _port = 8000
    uvicorn.run("main:app", host=_host, port=_port,
                log_level="info", reload=True)
