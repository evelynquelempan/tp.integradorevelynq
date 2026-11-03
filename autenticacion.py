from usuario import Usuario

USUARIOS = [
    Usuario("admin", "admin123", "administrador"),
    Usuario("cliente", "cliente123", "cliente"),
]

MAX_INTENTOS = 3


def autenticar(username, password, usuarios=USUARIOS):
    for usuario in usuarios:
        if (usuario.username.lower() == username.strip().lower()
                and usuario.verificar_password(password)):
            return usuario
    return None


def iniciar_sesion(usuarios=USUARIOS):
    print("\n========== INICIO DE SESIÓN ==========")

    for intento in range(1, MAX_INTENTOS + 1):
        username = input("Usuario: ")
        password = input("Contraseña: ")

        usuario = autenticar(username, password, usuarios)
        if usuario:
            print(f"\nBienvenido/a, {usuario.username} ({usuario.rol})")
            return usuario

        print(f"Usuario o contraseña incorrectos. Intento {intento} de {MAX_INTENTOS}.")

    print("Demasiados intentos fallidos. Cerrando el programa.")
    return None