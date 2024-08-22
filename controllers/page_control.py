import flet as ft
from controllers.menu import menu

import pages.page1 as page1
import pages.page2 as page2

class PageControl:
    def __init__(self, page: ft.Page):
        """
        Initializes a new instance of the `PageControl` class.

        Args:
            page (ft.Page): The page object to associate with the page control.

        Initializes the `page` attribute with the provided `page` object.
        Sets the `appbar` attribute of the `page` object to the result of calling the `menu` function with `self` as the argument.
        Initializes the `pages` dictionary with mappings from page names to their content functions.

        Example:
            page_control = PageControl(page)
        """
        self.page = page
        # Set the `appbar` attribute of the `page` object to the result of calling the `menu` function with `self` as the argument.
        self.page.appbar = menu(self)

        # Dictionary mapping page names to their content functions
        self.pages = {
            "page1": page1.page1_content,
            "page2": page2.page2_content,
        }

    def load_page(self, page_name: str):
        if page_name in self.pages:
            self.page.controls.clear()
            self.page.add(self.pages[page_name](self))
        else:
            self.page.controls.clear()
            self.page.add(ft.Text(f"404 - Page '{page_name}' not found."))
        self.page.update()
