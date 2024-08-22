import flet as ft


def page1_content(pc):
   

    return ft.Column(
        controls=[
            ft.Text("This is Page 1"),
            ft.ElevatedButton("Go to Page 2", on_click=lambda _: pc.load_page("page2")),
        ]
    )
