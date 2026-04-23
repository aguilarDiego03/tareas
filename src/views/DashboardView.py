import flet as ft

class DashboardView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/dashboard")

        self.controls = [
            ft.Column(
                [
                    ft.Text("Bienvenido al Dashboard", size=30),
                    ft.ElevatedButton(
                        "Cerrar sesión",
                        on_click=lambda e: page.go("/")
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]