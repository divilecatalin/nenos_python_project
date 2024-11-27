import dash
import dash_mantine_components as dmc
from dash import html, dcc, Input, Output
from src.web.callbacks import register_all_callbacks
from src.web.components.header import Header
from src.web.components.add_user import AddUserComponent
from src.web.components.get_user import GetUserComponent
from src.web.components.update_user import UpdateUserComponent


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
            dmc.ButtonGroup(
                children=[
                dmc.Button("Get User", id='get-user-nav', n_clicks=0),
                dmc.Button("Add User", id='add-user-nav', n_clicks=0),
                dmc.Button("Update User", id='update-user-nav', n_clicks=0),
                dmc.Button("Delete User", id='delete-user-nav', n_clicks=0),
            ], style={"marginBottom": "20px"}),
            html.Div(
                id='webapp-content',
                  children=[
                      GetUserComponent().render()
                      ]),
            dcc.Interval(
                id="webapp-refresh-timer",
                  interval=1 * 60 * 1000, n_intervals=0
                  ),
        ]
    )
)


register_all_callbacks(app)


@app.callback(
    Output('webapp-content', 'children'),
    [Input('get-user-nav', 'n_clicks'),
     Input('add-user-nav', 'n_clicks'),
     Input('update-user-nav', 'n_clicks'),
     Input('delete-user-nav', 'n_clicks')
     ]
)
def update_content(get_user_clicks, add_user_clicks, update_user_clicks, delete_user_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return GetUserComponent().render()

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id == 'get-user-nav':
        return GetUserComponent().render()
    elif button_id == 'add-user-nav':
        return AddUserComponent().render()
    elif button_id == 'update-user-nav':
        return UpdateUserComponent().render()
    elif button_id == 'delete-user-nav':
        return GetUserComponent().render()

# Run the app
if __name__ == "__main__":
    app.run(debug=True)