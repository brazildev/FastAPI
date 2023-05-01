from models import Curso

# cursos = {
#     1: {
#         'titulo': 'Pro',
#         'aulas': 112,
#         'horas': 58
#     },
#     2: {
#         'titulo': 'Algoritmo',
#         'aulas': 87,
#         'horas': 67
#     }
# }

cursos = [
    Curso(id=1, titulo='Titulo 1', aulas=12, horas=15),
    Curso(id=2, titulo='Titulo 2', aulas=22, horas=25),
    Curso(id=3, titulo='Titulo 3', aulas=32, horas=35),
    Curso(id=4, titulo='Titulo 4', aulas=42, horas=45),
    Curso(id=5, titulo='Titulo 5', aulas=52, horas=55),
    Curso(id=6, titulo='Titulo 6', aulas=62, horas=65),
]
