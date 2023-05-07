from helpers import Analysis
import plotly.express as px
from dash import Input, Output, dcc, html
from jupyter_dash import JupyterDash

app = JupyterDash(__name__)


app.layout = html.Div(
    [
    html.H1("USA SURVEY (2019) HOUSEHOLD ANALYSIS "),
    html.H2("FEATURES VARIANCE"),
    dcc.Graph(id="bar-chart"),
    dcc.RadioItems(
                    options=[
                        {"label":"trimmed", "value": True},
                        {"label":"not-trimmed", "value": False}
                        ],
                    value=True,
                    id = "trim-button"
                ),
    html.H2("K - Means Clustering"),
    html.H3("Number of Clusters [k]"),
    dcc.Slider(min=2, max=12, step=1, value=2, id = "k-slider"),
    html.Div(id ="metric"), 
    dcc.Graph(id="pca-scatter")
    ]
)


@app.callback(
    Output("bar-chart", "figure"),
    Input("trim-button", "value")
            )
def var_graph(trimvar=True):
    
    high_tvar= Analysis().var_features(trimvar=trimvar, features_rtrn=False)
    
    fig =px.bar(x=high_tvar,
                y= high_tvar.index,
                orientation="h"
                )
    fig.update_layout(xaxis_title= "Variance", yaxis_title="Feature")
    
    return fig

@app.callback(
    Output("metric", "children"),
    Input("trim-button", "value"),
    Input("k-slider", "value")
    )
def metrics(trimvar=True, k=2):
    metric = Analysis().model_metrics(trimvar=trimvar, k=k, metrics=True)
    text = [
        html.H3(f"Inertia: {metric['inertia']}"),
        html.H3(f"Silhouette Score: {metric['silhouette']}")
        ]
    return text


@app.callback(
    Output("pca-scatter", "figure"),
    Input("trim-button", "value"),
    Input("k-slider", "value")
    )
def scatter_plot(trimvar=True, k=2):
    fig = px.scatter(
        data_frame= Analysis().pca_labels(trimvar=trimvar, k=k),
        x="PC1",
        y="PC2",
        color = "labels",
        title = "Clusters PCA Representation"
        )
    fig.update_layout(xaxis_title="PC1",yaxis_title = "PC2" )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
