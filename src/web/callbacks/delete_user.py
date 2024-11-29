import requests
from dash import Dash
from dash import callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
from src.config import API_URL
from src.web.components.error_card import MessageCardComponent

def register_delete_user_callbacks(app: Dash) -> None:
    """
    Register delete user callbacks
    """
    @app.callback(
        Output('delete-user-response', "children"),  
        [
            Input("delete-user-button", "n_clicks"),
            Input("delete-user-id", "value"),
        ]
    )
    def delete_user_info_from_api(_: int, user_id: str):
        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "delete-user-button":
            if user_id is None or user_id.strip() == "":
                raise PreventUpdate
            response = requests.delete(f"{API_URL}/users/{user_id}", timeout=5)
            print(response)
            if response.status_code == 204:
                return MessageCardComponent(response.status_code,f"Success: User with id:{user_id} deleted (status code:").render()
            elif response.status_code == 404:
                return MessageCardComponent(response.status_code,"Error: User not found (status code:").render()
            else:
                return MessageCardComponent(response.status_code,"Error:  (status code:").render()

        raise PreventUpdate