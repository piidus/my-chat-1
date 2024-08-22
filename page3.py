import flet as ft

def page3_content(page: ft.Page):
    return ft.Column(
        controls=[
            ft.Text("This is Page 3"),
            ft.ElevatedButton("Go to Page 1", on_click=lambda _: page.go("/page1")),
        ]
    )
