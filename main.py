import flet as ft
from page_control import PageControl
import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)
def main(page: ft.Page):
    page.title = "Flet App"
    page.window_always_on_top = True
    page.window.width = 300
    # Initialize page control
    pc = PageControl(page)

    # Set up the initial view (Page 1)
    pc.load_page("page1")

ft.app(target=main)
