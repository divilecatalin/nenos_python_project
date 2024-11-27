import dash_mantine_components as dmc
from dash import html
from src.web.components.base import DashAppBaseComponent

class UpdateUserComponent(DashAppBaseComponent):
    def __init__(self):
        pass

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(
                    id="update-user-id",
                    label="Update User id:",
                    w=200
                ),
                dmc.TextInput(
                    id="update-user-username",
                    label="Update User Name:",
                    w=200
                ),
                dmc.TextInput(
                    id="update-user-email",
                    label="Update User Email:",
                    w=200
                ),
                dmc.TextInput(
                    id="update-user-role",
                    label="Update User Role:",
                    w=200
                ),
                dmc.TextInput(
                    id="update-user-endorsements",
                    label="Update User Endorsements:",
                    value="0",
                    w=200
                ),
                dmc.TextInput(
                    id="update-user-reports",
                    label="Update User Reports:",
                    value="0",
                    w=200
                ),
                dmc.Button(
                    id="update-user-button",
                    children="Update User",
                    w=200,
                ),
                html.Div(
                id='update_user_details',
                  ), 
            ],
        )