# prestamos_equipos.py
# Sistema de gestión de préstamos de equipos
# Autor: [Tu Nombre]
# Descripción: Programa para registrar, devolver y consultar préstamos de equipos.

from datetime import datetime

# Diccionario inicial de equipos
equipos = {
    "Portatil HP": {"disponible": True, "prestamos": []},
    "Proyector Epson": {"disponible": True, "prestamos": []},
    "Tablet Samsung": {"disponible": True, "prestamos": []}
}


def mostrar_equipos():
    """Muestra todos los equipos y su estado actual"""
    print("\n📋 Lista de equipos registrados:")
    for nombre, datos in equipos.items():
        estado = "Disponible ✅" if datos["disponible"] else "Prestado ❌"
        print(f" - {nombre}: {estado}")
    print("-" * 40)


def registrar_prestamo():
    """Registra un nuevo préstamo de equipo"""
    print("\n🔑 Registrar préstamo de equipo")
    mostrar_equipos()

    equipo = input("👉 Ingrese el nombre exacto del equipo a prestar: ")

    # Validar existencia
    if equipo not in equipos:
        print("⚠️ Error: El equipo no existe en el sistema.")
        return

    # Validar disponibilidad
    if not equipos[equipo]["disponible"]:
        print("⚠️ El equipo ya está prestado.")
        return

    usuario = input("👤 Ingrese el nombre del usuario: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardar préstamo en una tupla inmutable
    prestamo = (usuario, fecha)
    equipos[equipo]["prestamos"].append(prestamo)
    equipos[equipo]["disponible"] = False

    print(f"✅ Préstamo registrado con éxito: {equipo} → {usuario} el {fecha}")


def devolver_equipo():
    """Marca un equipo como devuelto"""
    print("\n📦 Devolver equipo")
    equipo = input("👉 Ingrese el nombre exacto del equipo a devolver: ")

    # Validar existencia
    if equipo not in equipos:
        print("⚠️ Error: El equipo no existe en el sistema.")
        return

    # Validar que esté prestado
    if equipos[equipo]["disponible"]:
        print("⚠️ Ese equipo ya está disponible. No se puede devolver.")
        return

    equipos[equipo]["disponible"] = True
    print(f"✅ El equipo '{equipo}' ha sido devuelto y ahora está disponible.")


def ver_historial():
    """Muestra el historial completo de préstamos"""
    print("\n📖 Historial de préstamos")
    for nombre, datos in equipos.items():
        print(f"\n🔹 {nombre}:")
        if datos["prestamos"]:
            for usuario, fecha in datos["prestamos"]:
                print(f"   - Prestado a {usuario} el {fecha}")
        else:
            print("   Sin préstamos registrados.")
    print("-" * 40)


def agregar_equipo():
    """Agrega un nuevo equipo al sistema"""
    print("\n➕ Agregar nuevo equipo")
    nuevo = input("👉 Ingrese el nombre del nuevo equipo: ")

    if nuevo in equipos:
        print("⚠️ Error: Ese equipo ya existe en el sistema.")
        return

    equipos[nuevo] = {"disponible": True, "prestamos": []}
    print(f"✅ Equipo '{nuevo}' agregado exitosamente.")


def menu():
    """Menú principal interactivo"""
    while True:
        print("\n===== 📌 MENÚ PRINCIPAL - PRÉSTAMO DE EQUIPOS =====")
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")
        print("=================================================")

        opcion = input("👉 Seleccione una opción (1-6): ")

        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("👋 Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")


# Punto de entrada principal
if __name__ == "__main__":
    menu()
