import dash_mantine_components as dmc

from src.web.components.base import DashAppBaseComponent


class Loading(DashAppBaseComponent):

    def __init__(self) -> None:
        pass

    def render(self) -> dmc.Paper:
        return dmc.Center(
            children=[
                dmc.Loader(color="blue", size="xl", variant="dots")
            ]
        )
