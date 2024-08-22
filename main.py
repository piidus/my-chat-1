import flet as ft
from controllers.page_control import PageControl
from components.memory_usage import memory_profiler
import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)

@memory_profiler
def main(page: ft.Page):
    page.title = "Flet App"
    page.window_always_on_top = True
    page.window.width = 300
    page.window_left = 3000
    # Initialize page control
    pc = PageControl(page)

    # Set up the initial view (Page 1)
    pc.load_page("page1")

ft.app(target=main)
