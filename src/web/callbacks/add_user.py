import requests
from dash import Dash

from dash import callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

from src.config import API_URL
from src.common.data_transfer_objects.users import UserDto
from src.web.components.error_card import MessageCardComponent



def register_add_user_callbacks(app: Dash) -> None:
    """
    Register add user callbacks
    """
    @app.callback(
        Output('add_user_details', "children"),
        [
            Input("add-user-button", "n_clicks"),
            Input("add-user-username", "value"),
            Input("add-user-email", "value"),
            Input("add-user-role", "value"),
        ]
    )
    def send_user_info_to_api(_: int, username: str, email: str, role: str):
        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "add-user-button":
            if not username or not email or not role:
                raise PreventUpdate
            dto = UserDto(
                username=username,
                email=email,
                role=role,
                endorsements=0,
                reports=0,
                banned=False,
            )
            response = requests.put(f"{API_URL}/users", timeout=5, data=dto.json())
            if response.status_code == 201:
                return MessageCardComponent(response.status_code,f"Success: User inserted (status code:").render()
            elif response.status_code == 404:
                return MessageCardComponent(response.status_code,"Error: User not found (status code:").render()
            else:
                return MessageCardComponent(response.status_code,"Error:  (status code:").render()

        raise PreventUpdate