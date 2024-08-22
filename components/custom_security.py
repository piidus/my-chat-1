from flet import security

class MySecurity(security):
    def __init__(self):
        super().__init__()

    def on_login(self, e):
        pass