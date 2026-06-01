import sqlite3

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect('tareas.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT NOT NULL
    )
''')
conn.commit()

# Funciones
def agregar_tarea(descripcion):
    cursor.execute('INSERT INTO tareas (descripcion) VALUES (?)', (descripcion,))
    conn.commit()
    print("✅ Tarea agregada.")

def ver_tareas():
    cursor.execute('SELECT * FROM tareas')
    tareas = cursor.fetchall()
    print("\n📋 Lista de tareas:")
    for tarea in tareas:
        print(f"{tarea[0]} - {tarea[1]}")
    print()

def eliminar_tarea(id_tarea):
    cursor.execute('DELETE FROM tareas WHERE id = ?', (id_tarea,))
    conn.commit()
    print("🗑️ Tarea eliminada.")

# Menú interactivo
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            descripcion = input("Escribe la tarea: ")
            agregar_tarea(descripcion)
        elif opcion == '2':
            ver_tareas()
        elif opcion == '3':
            id_tarea = input("ID de la tarea a eliminar: ")
            eliminar_tarea(id_tarea)
        elif opcion == '4':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")

menu()

# Cerrar conexión al final
conn.close()