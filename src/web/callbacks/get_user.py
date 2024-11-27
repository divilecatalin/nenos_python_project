import requests
from dash import Dash
from dash import callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
from src.config import API_URL
from src.common.data_transfer_objects.users import UserDto
from src.web.components.user_card import UserCardComponent
from src.web.components.error_card import ErrorCardComponent

def register_get_user_callbacks(app: Dash) -> None:
    """
    Register get user callbacks
    """
    @app.callback(
        Output('fetch-user-detail', "children"),  
        [
            Input("get-user-button", "n_clicks"),
            Input("get-user-id", "value"),
        ]
    )
    def fetch_user_info_from_api(n_clicks: int, user_id: str):
        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "get-user-button":
            if user_id is None or user_id.strip() == "":
                raise PreventUpdate
            response = requests.get(f"{API_URL}/users/{user_id}", timeout=5)
            if response.status_code == 200:
                user_data = response.json()
                user_dto = UserDto(**user_data)
                return UserCardComponent(user_dto).render()
            else:
                return ErrorCardComponent(response.status_code,"Error: User not found (status code:").render()

        raise PreventUpdate