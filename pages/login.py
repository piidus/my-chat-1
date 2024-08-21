import flet as ft
from components.memory_usage import memory_profiler
from components.text_control import MyText
# @memory_profiler
def login_page(session_id):
    
    return ft.Column([
        # ft.Text("Welcome to the home page"),
        MyText("Welcome to the home page"),
        MyText(f"Session ID: {session_id}"),
        # ft.Text(f"Session ID: {session_id}"),
        # ft.Text(value='Hi'),
        # ... other home page content
    ])
