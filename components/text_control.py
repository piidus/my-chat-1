import flet as ft

class MyText(ft.Text):
    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
        self.text = value
        self.text_align = kwargs.get('text_align', ft.TextAlign.CENTER)  # Set the default value to ft.TextAlign.CENTER
