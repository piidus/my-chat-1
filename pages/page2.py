import flet as ft

def page2_content(pc):
    

    return ft.Column(
        controls=[
            ft.Text("This is Page 2"),
            ft.ElevatedButton("Go to Page 1", on_click=lambda _: pc.load_page("page1")),
        ]
    )
