import dash_mantine_components as dmc

class ErrorCardComponent:
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def render(self):
        return dmc.Card(
            children=[dmc.Text(f"{self.message} {self.status_code})")],
            shadow="sm",
            p="lg",
            radius="md",
            bg="red",
            withBorder=True,
            style={"display": "block", "marginTop": "20px"},
        )