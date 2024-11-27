import dash_mantine_components as dmc
from src.web.components.base import DashAppBaseComponent

class GetUserComponent(DashAppBaseComponent):
    def __init__(self):
        pass
        

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(
                    id="get-user-id",
                    label="User id:",
                    w=200
                ),
                dmc.Button(
                    id="get-user-button",
                    children="Get User",
                    w=200,
                ),
            ],
        )