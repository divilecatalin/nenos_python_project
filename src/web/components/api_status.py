import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html

from src.web.components.base import DashAppBaseComponent

# check for icons here: https://icon-sets.iconify.design/

class ApiStatusOK(DashAppBaseComponent):

    def __init__(self):
        pass

    def render(self):
        return html.Div(children=[
            DashIconify(icon="fluent-color:checkmark-circle-48"),
            dmc.Text("API is connected"),
        ])

class ApiStatusNOK(DashAppBaseComponent):

    def __init__(self, status_code: int):
        self.status_code = status_code

    def render(self):
        return html.Div(children=[
            DashIconify(icon="fluent-color:error-circle-48"),
            dmc.Text("API is yielding"),
            dmc.Text(str(self.status_code)),
        ])

class ApiStatusError(DashAppBaseComponent):

    def __init__(self, exception: Exception):
        self.exception = exception

    def render(self):
        return html.Div(children=[
            DashIconify(icon="fluent-color:dismiss-circle-48"),
            dmc.Text("API is down"),
            dmc.Text(str(self.exception)),
        ])
