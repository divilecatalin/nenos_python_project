import dash_mantine_components as dmc
from dash import html
from src.web.components.base import DashAppBaseComponent

class AddUserComponent(DashAppBaseComponent):
    def __init__(self):
        pass

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(
                    id="add-user-username",
                    label="User Name:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-user-email",
                    label="User Email:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-user-role",
                    label="User Role:",
                    w=200
                ),
                dmc.Button(
                    id="add-user-button",
                    children="Add User",
                    w=200,
                ),
                html.Div(
                    id='add_user_details',
                  ),
            ],
        )