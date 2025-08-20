import random
import string

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Ejemplo de uso
if __name__ == "__main__":
    print("Generador de Contraseñas Seguras 🔐")
    longitud = int(input("¿Qué longitud deseas para tu contraseña? (Ej. 12): "))
    nueva_contraseña = generar_contraseña(longitud)
    print(f"\nTu contraseña generada es:\n{nueva_contraseña}")

    # Guardar en archivo (opcional)
    guardar = input("¿Deseas guardarla en un archivo? (s/n): ").lower()
    if guardar == 's':
        with open("contraseña_generada.txt", "w") as archivo:
            archivo.write(nueva_contraseña)
        print("✅ Contraseña guardada en 'contraseña_generada.txt'")
