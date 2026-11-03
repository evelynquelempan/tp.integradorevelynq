class Usuario:
    ROLES_VALIDOS = ("administrador", "cliente")

    def __init__(self, username, password, rol):
        if not isinstance(username, str) or not username.strip():
            raise ValueError("El nombre de usuario no puede estar vacío")

        if not isinstance(password, str) or not password.strip():
            raise ValueError("La contraseña no puede estar vacía")

        if rol not in self.ROLES_VALIDOS:
            raise ValueError("El rol debe ser 'administrador' o 'cliente'")

        self._username = username
        self._password = password
        self._rol = rol

    @property
    def username(self):
        return self._username

    @property
    def rol(self):
        return self._rol

    def verificar_password(self, password):
        return self._password == password

    def es_administrador(self):
        return self._rol == "administrador"

    def __str__(self):
        return f"Usuario: {self._username} | Rol: {self._rol}"