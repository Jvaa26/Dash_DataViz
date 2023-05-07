from ast import In
from sre_parse import State
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json
import unicodedata
import requests

def normalizar(txt):
    novo_txt = unicodedata.normalize("NFD", txt)
    novo_txt = novo_txt.encode("ascii","ignore")
    novo_txt = novo_txt.decode("utf-8")
    if 'State' in novo_txt:
        novo_txt = novo_txt.replace('State of ','')
    return novo_txt

df_states = pd.read_csv("df_geo_estados.csv", sep=",")
df_apis = pd.read_csv("df_geo_api.csv", sep=",")
df = pd.read_csv("df_dados.csv")
#df = df[df['state'] == "Parana"]
df['count'] = df['geoapi_id']
df_api_satate = df.groupby(['geoapi_id','state'], as_index=False)['count'].count()
options = df_states['state']
op = options.tolist()
brasil_map = json.load(open("dataMaps.json", "r"))


#dash
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
fig = px.choropleth_mapbox(df_states, locations="state",center = {"lat": -16.95, "lon":-47.78}, color = 'geos', geojson=brasil_map, color_continuous_scale="darkmint", opacity=0.4, hover_data={'geos':True}, zoom=3)
fig.update_layout(
    paper_bgcolor ="#242424",
    autosize=True,
    margin = go.Margin(l=0,r=0,t=0,b=0),
    showlegend=False,
    mapbox_style="carto-darkmatter",    
)
fig2 = px.bar(df_api_satate,x='state',y='count',color='geoapi_id')
#fig2.add_trace(px.bar(df_api_satate,x='state',y='count',color='geoapi_id',title="Geolocalizacoes por API"))
fig2.update_layout(
    plot_bgcolor="#242424",
    paper_bgcolor = "#242424",
    autosize=True,
    margin = go.Margin(l=15,r=15,t=15,b=15)
)
#==============================================================================
#Layout
app.layout = dbc.Container(
    children=[dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.Div([
                        html.H5("Geolocalizações"),
                        dbc.Button("BRASIL", color = "primary", id = "button", size = "lg")
                    ], style={}),
                    html.P("Inform os estados que gostaria de ver os dados", style={"margin-top":"40px"}),
                    html.Div([
                        dbc.Card([
                            dbc.CardBody([
                                html.H3("Estados",style={"color:":"#0099CC"}),
                                 dcc.Checklist(
                                df_states['state'],df_states['state'],id="state-check"
                                )                 
                            ])
                        ], color= "light", outline=True)
                         
                    ], id="div-teste"),
                ]),
                dbc.Row([
                    dbc.Col([ 
                        html.Div([
                            dcc.Graph(id="graph", figure = fig2)
                        ],style={"margin-top":"10px"})
                    ])
                ])
                ], md=5,style={"padding":"25px","background-color":"#242424"}),
            dbc.Col([
                dcc.Loading(id="loading-1", type="default",children=[
                    dcc.Graph(id="map", figure = fig,style={"height":"100vh"})
                ])
            ],md=7,class_name="g-0"),
        ])
    ],fluid = True 
)
#======== Interatividade ===============

@app.callback(
    Output('graph','figure'),
    Output('map','figure'),
    Input("state-check",'value'),
    Input('map','clickData')
    )
def display_status(states,click_data):
    df_sub = df_states[df_states['state'].isin(states)]
    id = dash.callback_context.triggered[0]['prop_id']
    print('ID: ',id)
    if id != None and id == "map.clickData":
        sts = [click_data['points'][0]['location']]
    else:
        sts = states
    dfas = df_api_satate[df_api_satate['state'].isin(sts)]

    fig = px.choropleth_mapbox(df_sub, locations="state",center = {"lat": -16.95, "lon":-47.78}, color = 'geos', geojson=brasil_map, color_continuous_scale="darkmint", opacity=0.4, hover_data={'geos':True}, zoom=3)
    fig.update_layout(
        paper_bgcolor ="#242424",
        autosize=True,
        margin = go.Margin(l=0,r=0,t=0,b=0),
        showlegend=False,
        mapbox_style="carto-darkmatter",)
    fig2 = px.bar(dfas,x='state',y='count',color='geoapi_id')
    fig2.update_layout(
    plot_bgcolor="#242424",
    paper_bgcolor = "#242424",
    autosize=True,
    margin = go.Margin(l=15,r=15,t=15,b=15)
)
    return fig2, fig

@app.callback(
    Output('state-check','value'),
    Input('button','n_clicks'),
    Input('graph','clickData'),
    State('state-check', 'options')
    )
def display_status(nclick,dataGraph,opts):
    id = dash.callback_context.triggered[0]['prop_id']
    if id != '.' and id != "button.n_clicks":
        x = dataGraph['points'][0]['x']
        return [x]
    else:
        return opts





if __name__ == "__main__":
    app.run_server(debug=True, port= 8051)