import flet as ft

def menu(pc):
    return ft.AppBar(
        title=ft.Text("Menu"),
        leading=ft.Icon(ft.icons.MENU),
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Page 1", on_click=lambda _: pc.load_page("page1")),
                    ft.PopupMenuItem(text="Page 2", on_click=lambda _: pc.load_page("page2")),
                ]
            )
        ]
    )
