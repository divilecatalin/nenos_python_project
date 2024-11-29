import dash_mantine_components as dmc
from dash import html
from src.web.components.base import DashAppBaseComponent

class DeleteUserComponent(DashAppBaseComponent):
    def __init__(self):
        pass

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(
                    id="delete-user-id",
                    label="User id:",
                    w=200
                ),
                dmc.Button(
                    id="delete-user-button",
                    children="Delete User",
                    w=200,
                ),
                html.Div(
                    id='delete-user-response',
                    style={"marginTop":"20px"},
                  ), 
            ],
        )