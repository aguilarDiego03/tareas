import flet as ft

class LoginView(ft.View):
    def __init__(self, page: ft.Page, controller):
        super().__init__("/")
        self.page = page
        self.controller = controller

        self.nombre = ft.TextField(label="Nombre")
        self.apellido = ft.TextField(label="Apellido")
        self.email = ft.TextField(label="Correo")
        self.password = ft.TextField(label="Contraseña", password=True)

        self.mensaje = ft.Text()

        self.controls = [
            ft.Column(
                [
                    ft.Text("Registro / Login", size=30),

                    self.nombre,
                    self.apellido,
                    self.email,
                    self.password,

                    self.mensaje,

                    ft.Row(
                        [
                            ft.ElevatedButton("Iniciar sesión", on_click=self.login),
                            ft.ElevatedButton("Crear cuenta", on_click=self.crear_cuenta),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]

    def login(self, e):
        success = self.controller.login(
            self.email.value,
            self.password.value
        )

        if success:
            self.page.go("/dashboard")
        else:
            self.mensaje.value = "Credenciales incorrectas"
            self.mensaje.color = "red"
            self.page.update()

    def crear_cuenta(self, e):
        ok, msg = self.controller.registrar_usuario(
            self.nombre.value,
            self.apellido.value,
            self.email.value,
            self.password.value
        )

        self.mensaje.value = msg
        self.mensaje.color = "green" if ok else "red"
        self.page.update()