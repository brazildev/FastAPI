from fastapi import FastAPI
from data import cursos

app = FastAPI()


@app.get('/')
async def raiz():
    return {"msg": "FastAPI"}


if __name__ == '__main__':
    import uvicorn

    _host = '0.0.0.0'
    _port = 8000
    uvicorn.run("main:app", host=_host, port=_port,
                log_level="info", reload=True)
