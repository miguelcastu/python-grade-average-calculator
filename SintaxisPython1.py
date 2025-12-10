# calculadora_promedios.py

def ingresar_calificaciones():
    """
    Permite al usuario introducir materias y calificaciones.
    Devuelve dos listas: materias y calificaciones.
    """
    materias = []
    calificaciones = []

    print("=== INGRESO DE MATERIAS Y CALIFICACIONES ===")

    while True:
        # Pedir nombre de la materia
        nombre = input("Introduce el nombre de la materia: ").strip()
        while not nombre:
            print("El nombre de la materia no puede estar vacío.")
            nombre = input("Introduce el nombre de la materia: ").strip()

        # Pedir calificación con validación
        while True:
            cal_str = input(f"Introduce la calificación de '{nombre}' (0 a 10): ").strip()
            try:
                cal = float(cal_str)
                if 0 <= cal <= 10:
                    break
                else:
                    print("Error: la calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Error: debes introducir un número válido.")

        materias.append(nombre)
        calificaciones.append(cal)

        # Preguntar si desea continuar
        while True:
            continuar = input("¿Deseas ingresar otra materia? (s/n): ").strip().lower()
            if continuar in ("s", "n"):
                break
            else:
                print("Respuesta no válida. Escribe 's' para sí o 'n' para no.")

        if continuar == "n":
            break

    return materias, calificaciones


def calcular_promedio(calificaciones):
    """
    Recibe una lista de calificaciones y devuelve el promedio.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """
    Recibe la lista de calificaciones y un umbral.
    Devuelve dos listas de índices:
      - indices_aprobadas
      - indices_reprobadas
    """
    indices_aprobadas = []
    indices_reprobadas = []

    for i, cal in enumerate(calificaciones):
        if cal >= umbral:
            indices_aprobadas.append(i)
        else:
            indices_reprobadas.append(i)

    return indices_aprobadas, indices_reprobadas


def encontrar_extremos(calificaciones):
    """
    Devuelve una tupla (indice_max, indice_min) con los índices
    de la calificación más alta y más baja.
    Asume que la lista NO está vacía.
    """
    indice_max = 0
    indice_min = 0

    for i in range(1, len(calificaciones)):
        if calificaciones[i] > calificaciones[indice_max]:
            indice_max = i
        if calificaciones[i] < calificaciones[indice_min]:
            indice_min = i

    return indice_max, indice_min


def main():
    print("==============================================")
    print("  CALCULADORA DE PROMEDIOS ESCOLARES (Python) ")
    print("==============================================\n")

    materias, calificaciones = ingresar_calificaciones()

    # Manejo del caso en que no se ingresa ninguna materia
    if not materias:
        print("\nNo se ingresó ninguna materia. No hay datos para procesar.")
        print("Gracias por utilizar la calculadora de promedios. ¡Hasta pronto!")
        return

    # Cálculos principales
    promedio_general = calcular_promedio(calificaciones)
    indices_aprobadas, indices_reprobadas = determinar_estado(calificaciones, umbral=5.0)
    indice_max, indice_min = encontrar_extremos(calificaciones)

    # Resumen final
    print("\n=========== RESUMEN FINAL ===========")

    # Todas las materias con sus calificaciones
    print("\nMaterias y calificaciones:")
    print("--------------------------------------")
    for i, (mat, cal) in enumerate(zip(materias, calificaciones), start=1):
        print(f"{i}. {mat}: {cal:.2f}")

    # Promedio general
    print("\nPromedio general de calificaciones:")
    print("--------------------------------------")
    print(f"{promedio_general:.2f}")

    # Materias aprobadas y reprobadas
    print("\nMaterias aprobadas (calificación >= 5.0):")
    print("--------------------------------------")
    if indices_aprobadas:
        for i in indices_aprobadas:
            print(f"- {materias[i]}: {calificaciones[i]:.2f}")
    else:
        print("Ninguna materia aprobada.")

    print("\nMaterias reprobadas (calificación < 5.0):")
    print("--------------------------------------")
    if indices_reprobadas:
        for i in indices_reprobadas:
            print(f"- {materias[i]}: {calificaciones[i]:.2f}")
    else:
        print("Ninguna materia reprobada.")

    # Materia con mejor y peor calificación
    print("\nMateria con MEJOR calificación:")
    print("--------------------------------------")
    print(f"{materias[indice_max]} con {calificaciones[indice_max]:.2f}")

    print("\nMateria con PEOR calificación:")
    print("--------------------------------------")
    print(f"{materias[indice_min]} con {calificaciones[indice_min]:.2f}")

    print("\n==============================================")
    print("Gracias por utilizar la calculadora de promedios.")
    print("¡Hasta pronto!")
    print("==============================================")


if __name__ == "__main__":
    main()
