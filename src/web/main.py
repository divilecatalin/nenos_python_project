import dash
import dash_mantine_components as dmc
from dash import html, dcc, Input, Output
from src.web.callbacks import register_all_callbacks
from src.web.components.header import Header
from src.web.components.add_user import AddUserComponent
from src.web.components.get_user import GetUserComponent
from src.web.components.update_user import UpdateUserComponent
from src.web.components.delete_user import DeleteUserComponent


# Create the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "API Status Checker"

# App layout
app.layout = dmc.MantineProvider(
    children=dmc.Stack(
        children=[
            html.Div(
                id='webapp-header',
                children=Header("Online shop").render()),
            dmc.Divider(variant="solid"),
            dmc.Tabs(
                [
                    dmc.TabsList([
                            dmc.Tab("Get User", value="get-user", className="tab-inactive"),
                            dmc.Tab("Add User", value="add-user", className="tab-inactive"),
                            dmc.Tab("Update User", value="update-user", className="tab-inactive"),
                            dmc.Tab("Delete User", value="delete-user", className="tab-inactive"),
                        ],
                        grow=True,
                        style={"display": "flex", "justifyContent": "center"},
                        
                    ),
                    dmc.TabsPanel(GetUserComponent().render(), value="get-user"),
                    dmc.TabsPanel(AddUserComponent().render(), value="add-user"),
                    dmc.TabsPanel(UpdateUserComponent().render(), value="update-user"),
                    dmc.TabsPanel(DeleteUserComponent().render(), value="delete-user"),
                ],
                value="get-user",  
                id="webapp-tabs",
                color="blue",
                variant="pills",
                style={"marginBottom": "20px"}
            ),
            dcc.Interval(
                id="webapp-refresh-timer",
                  interval=1 * 60 * 1000, n_intervals=0
                  ),
        ]
    )
)


register_all_callbacks(app)


@app.callback(
    Output("webapp-tabs", "value"),
    Input("webapp-refresh-timer", "n_intervals"),
    prevent_initial_call=True
)
def refresh_tabs(n_intervals):
    return dash.no_update
# Run the app
if __name__ == "__main__":
    app.run(debug=True)