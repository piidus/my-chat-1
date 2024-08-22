import flet as ft
from controllers.menu import menu
from pages.auth.sign_in import Page1
from pages.page2 import Page2

class PageControl:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.appbar = menu(self)

        # Dictionary mapping page names to their class instances
        self.pages = {
            "Page1": Page1(self.page, self),
            "Page2": Page2(self.page, self),
        }

    def load_page(self, page_name: str):
        if page_name in self.pages:
            # Clear existing controls
            self.page.controls.clear()

            # Add the new page content
            self.page.add(self.pages[page_name].content())

            # Update the page to reflect changes
            self.page.update()

            # Call did_mount if it exists
            if hasattr(self.pages[page_name], 'did_mount'):
                self.pages[page_name].did_mount()
        else:
            self.page.controls.clear()
            self.page.add(ft.Text(f"404 - Page '{page_name}' not found."))
            self.page.update()

    def navigate_to(self, page_name: str):
        self.load_page(page_name)