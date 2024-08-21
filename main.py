import flet as ft
from random import randint
from pages.home import home_page
from components.menu import menu
from components.memory_usage import memory_profiler

@memory_profiler
def main(page: ft.Page):
    page.title = "My Chat"
    page.window.width = 300

    # Retrieve session ID or set it if not already present
    session_id = page.session.get("session_id")
    if not session_id:
        session_id = randint(1000, 9999) # Example session ID, you can set this dynamically
        page.session.set("session_id", session_id)

    content_area = ft.Container()
    
    def show_page(page_content):
        content_area.content = page_content
        page.update()

    menu_bar = menu(show_page,session_id)  # Pass the show_page function to the menu

    # Add the content_area to the page first
    page.add(menu_bar, content_area)

    # Initial page`s content will show the session ID on the initial page
    show_page(home_page(session_id))

    

ft.app(main)