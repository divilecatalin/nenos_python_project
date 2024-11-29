import dash_mantine_components as dmc
from src.web.components.base import DashAppBaseComponent

class MessageCardComponent(DashAppBaseComponent):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def render(self):
        return dmc.Card(
            children=[dmc.Text(f"{self.message} {self.status_code})")],
            shadow="sm",
            p="lg",
            radius="md",
            bg="yellow",
            withBorder=True,
            style={"display": "block", "marginTop": "20px"},
        )