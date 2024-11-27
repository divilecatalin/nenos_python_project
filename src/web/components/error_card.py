import dash_mantine_components as dmc

class ErrorCardComponent:
    def __init__(self, status_code):
        self.status_code = status_code

    def render(self):
        return dmc.Card(
            children=[dmc.Text(f"Error: User not found (status code: {self.status_code})")],
            shadow="sm",
            p="lg",
            radius="md",
            withBorder=True,
            style={"display": "block", "marginTop": "20px"},
        )