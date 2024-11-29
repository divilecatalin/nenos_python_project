import dash_mantine_components as dmc
from src.common.data_transfer_objects.users import UserDto
from src.web.components.base import DashAppBaseComponent

class UpdatedUserCardComponent(DashAppBaseComponent):
    def __init__(self, user_dto:UserDto, user_id:int):
        self.user_dto = user_dto
        self.user_id = user_id

    def render(self):
        return dmc.Card(
            children=[
                dmc.Text(f"User id: {self.user_id}"),
                dmc.Text(f"Username: {self.user_dto.username}"),
                dmc.Text(f"Email: {self.user_dto.email}"),
                dmc.Text(f"Role: {self.user_dto.role}"),
                dmc.Text(f"Endorsements: {self.user_dto.endorsements}"),
                dmc.Text(f"Reports: {self.user_dto.reports}"),
                dmc.Text(f"Banned: {self.user_dto.banned}",
                        style={"color": "rgb(255, 0, 0)" if self.user_dto.reports >= 10 else "rgb(0, 0, 0)", "fontWeight": "bold"}),
            ],
            shadow="sm",
            p="lg",
            radius="md",
            withBorder=True,
            style={"display": "block", "marginTop": "20px"},
        )