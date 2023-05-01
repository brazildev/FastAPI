from time import sleep


def fake_db():
    try:
        print('Abrindo conexão...')
        sleep(1)
    finally:
        print('Fechando conexão...')
        sleep(1)
