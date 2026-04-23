from models.UsuarioModel import UsuarioModel
import bcrypt

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(self, nombre, apellido, email, password):
        if not nombre or not apellido or not email or not password:
            return False, "Todos los campos son obligatorios"

        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        creado = self.model.crear_usuario(
            nombre,
            apellido,
            email,
            hashed.decode()
        )

        if creado:
            return True, "Cuenta creada correctamente"
        else:
            return False, "El correo ya existe"

    def login(self, email, password):
        usuario = self.model.obtener_usuario(email)

        if not usuario:
            return False

        stored_password = usuario[4].encode()

        if bcrypt.checkpw(password.encode(), stored_password):
            return True

        return False