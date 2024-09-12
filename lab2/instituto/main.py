from instituto.clase import estudiante_registrado_en_materia

print(estudiante_registrado_en_materia("Daniel", "Matematica"))  # True
print(estudiante_registrado_en_materia("Daniel", "Biologia"))    # False
print(estudiante_registrado_en_materia("Luis", "Fisica"))        # Error: El estudiante Luis no está registrado.
