from typing import List
from instituto.estudiante import devolver_materias

def estudiante_registrado_en_materia(nombre: str, materia: str) -> bool:
    try:
        materias: List[str] = devolver_materias(nombre)
        return materia in materias
    except ValueError as e:
        print(e)
        return False
