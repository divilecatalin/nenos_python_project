import dash_mantine_components as dmc
from src.common.data_transfer_objects.users import UserDto

class UserCardComponent:
    def __init__(self, user_dto:UserDto):
        self.user_dto = user_dto

    def render(self):
        return dmc.Card(
            children=[
                dmc.Text(f"Username: {self.user_dto.username}", weight=500),
                dmc.Text(f"Email: {self.user_dto.email}"),
                dmc.Text(f"Role: {self.user_dto.role}"),
                dmc.Text(f"Endorsements: {self.user_dto.endorsements}"),
                dmc.Text(f"Reports: {self.user_dto.reports}"),
                dmc.Text(f"Banned: {self.user_dto.banned}"),
            ],
            shadow="sm",
            p="lg",
            radius="md",
            withBorder=True,
            style={"display": "block", "marginTop": "20px"},
        )