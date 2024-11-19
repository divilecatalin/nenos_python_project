import dash_mantine_components as dmc

from src.web.components.base import DashAppBaseComponent


class Header(DashAppBaseComponent):

    def __init__(self, title: str) -> None:
        self.title=title

    def render(self) -> dmc.Paper:
        return dmc.Paper(
            children=dmc.Title(self.title, order=1, style={"margin": "0", "color": "white"}),
            shadow="xs",
            style={
                "backgroundColor": "#4C6EF5",
                "padding": "10px"
            },
        )
