import flet as ft
from components.memory_usage import memory_profiler
from components.text_control import MyText
# @memory_profiler
def home_page(session_id):
    """
    Returns a ft.Column widget containing the home page content.

    The home_page function creates a ft.Column widget with ft.Text widgets as its children.
    The ft.Text widgets display the welcome message and the session ID.

    Parameters:
        session_id (str): The ID of the current session.

    Returns:
        ft.Column: The ft.Column widget containing the home page content.
    """

    return ft.Column([
        # ft.Text("Welcome to the home page"),
        MyText("Welcome to the home page"),
        MyText(f"Session ID: {session_id}"),
        # ft.Text(f"Session ID: {session_id}"),
        # ft.Text(value='Hi'),
        # ... other home page content
    ])
