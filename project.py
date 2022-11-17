#importing the libraries
import dash
from dash import html, dcc
import plotly.express as px
import json 
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv('https://raw.githubusercontent.com/DaTolok/python-edx/main/MOOC3/Datasets/iris.csv')

#defininf the variables
variables = [{'label':col, 'value':col} for col in df.columns[:-1]] 
marginals = [{'label':m, 'value':m} for m in ['box', 'violin', 'rug', 'histogram']]
#defining the app
app = dash.Dash() 

#defining the layout
app.layout = html.Div([html.Div([html.H1('Análisis del dataset iris.csv')],
                                style={'textAlign':'center'}),
                          html.Div([html.H3('Configuración de parámetros de la gráfica')],
                                      style={'textAlign':'5%'}),
                            html.Div([html.Label('Selecciona la variable del eje X'), 
                                                dcc.Dropdown(id='eje-x', options=variables)],
                                                style={'width':'20%', 
                                                       'marginRight':'3%',
                                                       'marginLeft':'5%',
                                                       'verticalAlign':'top',
                                                       'display':'inline-block'}),
                            html.Div([html.Label('Selecciona el marginal del eje X'),
                                                dcc.RadioItems(id='marginal-x', options=marginals, labelStyle={'display':'block'})],
                                                style={'width':'20%',
                                                        'marginRight':'4%',
                                                        'display':'inline-block'}),
                            html.Div([html.Label('Selecciona la variable del eje Y'),
                                                dcc.Dropdown(id='eje-y', options=variables)],
                                                style={'width':'20%',
                                                        'marginRight':'3%',
                                                        'verticalAlign':'top',
                                                        'display':'inline-block'}),
                            html.Div([html.Label('Selecciona el marginal del eje Y'),
                                                dcc.RadioItems(id='marginal-y', options=marginals, labelStyle={'display':'block'})],
                                                style={'width':'20%',
                                                        'display':'inline-block'}),
                            html.Div([dcc.Graph(id='scatter')])])

#defining the callback
@app.callback(Output('scatter', 'figure'),
                [Input('eje-x', 'value'),
                 Input('marginal-x', 'value'),
                 Input('eje-y', 'value'), 
                 Input('marginal-y', 'value')])  


#defining the function
def update_graph(eje_x, marginal_x, eje_y, marginal_y):
    fig = px.scatter(df, x = eje_x,
                         y = eje_y, 
                         mx = marginal_x, 
                         my = marginal_y, 
                         color = 'class',
                         title= 'Diagrama de dispersión: '+str(eje_x)+' vs '+str(eje_y))
    return fig


#running the app
if __name__ == '__main__':
    app.run_server()