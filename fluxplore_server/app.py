import uuid
import dash
from dash import Dash, html, dcc, callback, Output, Input, ALL
import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State
import data_model  # Assuming data_model.py contains the provided classes

baseurl = ""
external_stylesheets = [dbc.themes.BOOTSTRAP, f"{baseurl}/assets/app.css"]  # dbc.themes.JOURNAL
app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    update_title="Loading...",
    url_base_pathname=baseurl + "/",
)
app._favicon = "favicon.png"
app.title = "FluxPlore is a research project to test and develop competing concepts and behaviors of large language models"

# Load the TestSeriesList
test_series_list = data_model.TestSeriesList()
test_series_list.load()


# Convert TestSeries data to a format suitable for display in a Dash DataTable
def series_to_dataframe(series_list):
    data = [
        {
            "series_id": series.series_id,
            "model": (", ".join(getattr(series.model.classification, "test_methods", ""))),
            # Add other fields as necessary
        }
        for series in series_list
    ]
    return pd.DataFrame(data)


@app.callback(Output("series-store", "data"), [Input("app-load-trigger", "n_clicks")])
def load_series_data(n_clicks):
    test_series_list.load()
    return {"series_data": [series.to_dict() for series in test_series_list.series_list]}


@app.callback(Output("series-table", "data"), [Input("series-store", "data")])
def update_table(store_data):
    series_list = [data_model.TestSeries.from_dict(d) for d in store_data["series_data"]]
    return series_to_dataframe(series_list).to_dict("records")


@app.callback([Output("update-series-btn", "disabled"), Output("delete-series-btn", "disabled")], [Input("series-table", "selected_rows")])
def toggle_buttons_enabled_state(selected_rows):
    if selected_rows:
        # If any row is selected, enable the buttons
        return False, False
    else:
        # If no row is selected, disable the buttons
        return True, True


@app.callback(
    Output("series-store", "data", allow_duplicate=True),
    [Input("add-series-btn", "n_clicks"), Input("update-series-btn", "n_clicks"), Input("delete-series-btn", "n_clicks")],
    [
        State("series-store", "data"),
        State("test-type-dropdown", "value"),
        State("methods-dropdown", "value"),
        State("abilities-dropdown", "value"),
        State("areas-dropdown", "value"),
        State("series-table", "selected_rows"),
    ],
    prevent_initial_call=True,
)
def add_update_series(add_clicks, update_clicks, delete_clicks, store_data, test_type, methods, abilities, areas, selected_rows):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    # Recreate the TestSeriesList from store_data
    test_series_list = data_model.TestSeriesList()
    test_series_list.series_list = [data_model.TestSeries.from_dict(d) for d in store_data["series_data"]]
    if button_id == "add-series-btn":
        # Create a new Model instance
        classification = data_model.Classification(test_type, methods, abilities, areas)
        new_model = data_model.Model(
            version="",
            description="",
            classification=classification,
            test_creation_instructions=[],
            test_provision_strategy=data_model.TestProvisionStrategy.create_default(),
            result_requirements={},
        )

        # Create and add a new TestSeries with the single Model
        new_series = data_model.TestSeries(
            series_id=str(uuid.uuid4()), model=new_model, test_provision_strategy=data_model.TestProvisionStrategy.create_default(), test_implementations=[]
        )
        test_series_list.add_series(new_series)

    elif button_id == "update-series-btn" and selected_rows:
        selected_series_index = selected_rows[0]
        if selected_series_index < len(test_series_list.series_list):
            selected_series = test_series_list.series_list[selected_series_index]
            if selected_series and selected_series.model:
                # Update the model's classification
                selected_series.model.classification.test_type = test_type
                selected_series.model.classification.test_methods = methods
                selected_series.model.classification.abilities_tested = abilities
                selected_series.model.classification.areas_tested = areas

                # Update the series in the list
                test_series_list.update_series(selected_series_index, selected_series)

    return {"series_data": [series.to_dict() for series in test_series_list.series_list]}


# Layout
app.layout = dbc.Container(
    [
        dcc.Store(id="series-store"),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4(
                        f"FluxPlore is a research project to test and develop competing concepts and behaviors of large language models",
                        className="card-title",
                    ),
                    html.P(
                        dbc.Button(
                            "Description",
                            id="collapse-button",
                            className="me-md-2",
                            color="primary",
                            n_clicks=0,
                        ),
                        className="card-text",
                    ),
                ]
            ),
            color="primary",
            className="text-white",
        ),
        html.Div(id="app-load-trigger"),
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
        ),
    ],
    fluid=True,
    className="dbc",
)

# Callbacks and other functionalities will be added here

if __name__ == "__main__":
    app.run_server(debug=True)
