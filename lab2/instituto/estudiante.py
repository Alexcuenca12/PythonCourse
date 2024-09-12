from typing import List, Dict

estudiantes: Dict[str, List[str]] = {
    "Daniel": ["Matematica", "Computacion"],
    "Maria": ["Matematica", "Fisica"]
}

def devolver_materias(nombre: str) -> List[str]:
    try:
        return estudiantes[nombre]
    except KeyError:
        raise ValueError(f"El estudiante {nombre} no está registrado.")
