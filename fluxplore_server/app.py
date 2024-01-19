import dash
import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State
import data_model  # Assuming data_model.py contains the provided classes

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load the TestSeriesList
test_series_list = data_model.TestSeriesList()
test_series_list.load()


# Convert TestSeries data to a format suitable for display in a Dash DataTable
def series_to_dataframe(series_list):
    data = [
        {
            "series_id": series.series_id,
            "models": ", ".join(series.models),
            # Add other fields as necessary
        }
        for series in series_list
    ]
    return pd.DataFrame(data)


@app.callback([Output("update-series-btn", "disabled"), Output("delete-series-btn", "disabled")], [Input("series-table", "selected_rows")])
def toggle_buttons_enabled_state(selected_rows):
    print(selected_rows)
    if selected_rows:
        # If any row is selected, enable the buttons
        return False, False
    else:
        # If no row is selected, disable the buttons
        return True, True


@app.callback(
    Output("series-table", "data"),
    [Input("add-series-btn", "n_clicks"), Input("update-series-btn", "n_clicks"), Input("delete-series-btn", "n_clicks")],
    [
        State("test-type-dropdown", "value"),
        State("methods-dropdown", "value"),
        State("abilities-dropdown", "value"),
        State("areas-dropdown", "value"),
        State("series-table", "selected_rows"),
    ],
)
def modify_series(add_clicks, update_clicks, delete_clicks, test_type, methods, abilities, areas, selected_rows):
    ctx = dash.callback_context

    if not ctx.triggered:
        return dash.no_update
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "add-series-btn":
        # Implement logic to add a new series
        pass  # Replace with actual implementation

    elif button_id == "update-series-btn" and selected_rows:
        # Implement logic to update the selected series
        pass  # Replace with actual implementation

    elif button_id == "delete-series-btn" and selected_rows:
        # Implement logic to delete the selected series
        pass  # Replace with actual implementation

    return series_to_dataframe(test_series_list.series_list).to_dict("records")


# Layout
app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dash_table.DataTable(
                            id="series-table",
                            columns=[{"name": i, "id": i} for i in series_to_dataframe(test_series_list.series_list).columns],
                            data=series_to_dataframe(test_series_list.series_list).to_dict("records"),
                            row_selectable="single",  # Allow users to select a row
                        )
                    ],
                    width=8,
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id="test-type-dropdown", options=[{"label": i, "value": i} for i in data_model.config["testType"]], multi=True, placeholder="Select Test Types"
                        ),
                        dcc.Dropdown(id="methods-dropdown", options=[{"label": i, "value": i} for i in data_model.config["methods"]], multi=True, placeholder="Select Methods"),
                        dcc.Dropdown(
                            id="abilities-dropdown", options=[{"label": i, "value": i} for i in data_model.config["abilities"]], multi=True, placeholder="Select Abilities"
                        ),
                        dcc.Dropdown(id="areas-dropdown", options=[{"label": i, "value": i} for i in data_model.config["areas"]], multi=True, placeholder="Select Areas"),
                        html.Button("Add Series", id="add-series-btn", n_clicks=0),
                        html.Button("Update Series", id="update-series-btn", n_clicks=0, disabled=True),
                        html.Button("Delete Series", id="delete-series-btn", n_clicks=0, disabled=True),
                    ],
                    width=4,
                ),
            ]
        )
    ]
)

# Callbacks and other functionalities will be added here

if __name__ == "__main__":
    app.run_server(debug=True)
