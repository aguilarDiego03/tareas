import flet as ft

class LoginView(ft.View):
    def __init__(self, page: ft.Page, controller):
        super().__init__("/")
        self.page = page
        self.controller = controller
        
        # Agrega esto para forzar visibilidad
        self.bgcolor = ft.Colors.BLUE_GREY_50  # Fondo claro
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.nombre = ft.TextField(label="Nombre", width=300)
        self.apellido = ft.TextField(label="Apellido", width=300)
        self.email = ft.TextField(label="Correo", width=300)
        self.password = ft.TextField(label="Contraseña", password=True, width=300)
        self.mensaje = ft.Text()

        # El contenido debe estar dentro de un contenedor visible
        self.controls = [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Registro / Login", size=30, weight=ft.FontWeight.BOLD),
                        ft.Divider(height=20),
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
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15
                ),
                padding=30,
                bgcolor=ft.Colors.WHITE,
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors.GREY_300
                )
            )
        ]
