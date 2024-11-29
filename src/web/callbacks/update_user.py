import requests
from dash import Dash

from dash import callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

from src.config import API_URL
from src.common.data_transfer_objects.users import UserDto

from src.web.components.updated_user_card import UpdatedUserCardComponent
from src.web.components.error_card import MessageCardComponent



def register_update_user_callbacks(app: Dash) -> None:
    """
    Register update user callbacks
    """
    @app.callback(
        Output('update_user_details', "children"),
        [
            Input("update-user-button", "n_clicks"),
            Input("update-user-id", "value"),
            Input("update-user-username", "value"),
            Input("update-user-email", "value"),
            Input("update-user-role", "value"),
            Input("update-user-endorsements", "value"),
            Input("update-user-reports", "value"),
        ]
    )
    def update_user_info_to_api(_: int, user_id:int, username: str, email: str, role: str, endorsements: int, reports: int):
        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "update-user-button":
            if user_id is None or user_id.strip() == "":
                raise PreventUpdate
            
            dto = UserDto(
                username=username,
                email=email,
                role=role,
                endorsements=endorsements,
                reports=reports,
                banned=False,
            )
            response = requests.patch(f"{API_URL}/users/{user_id}", timeout=5, data=dto.json())
            print(response)
            if response.status_code == 200:
                user_data = response.json()
                user_dto = UserDto(**user_data)
                return UpdatedUserCardComponent(user_dto,user_id).render()
            else:
                return MessageCardComponent(response.status_code,"Error: User not found (status code:").render()

        raise PreventUpdate