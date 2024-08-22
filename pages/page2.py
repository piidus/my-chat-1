import flet as ft

class Page2(ft.Control):
    def __init__(self, page: ft.Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc

    def did_mount(self):
        self.page.session.set("last_page", "Page2")
        print('did mount page 2')
        self.page.update()

    def content(self):
        return ft.Column(
            controls=[
                ft.Text("This is Page 2"),
                ft.ElevatedButton("Go to Page 1", on_click=lambda _: self.pc.load_page("Page1")),
                ft.Text(f"Last Page: {self.page.session.get("last_page")}", selectable=False),
            
            ]
        )
