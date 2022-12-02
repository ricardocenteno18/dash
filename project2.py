import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

df = pd.read_csv('https://raw.githubusercontent.com/DaTolok/python-edx/main/MOOC3/Datasets/iris.csv')

#variables
variables = [{'label':col, 'value':col} for col in df.columns[:-1]]
marginals = [{'label':m, 'value':m} for m in ['box', 'violin', 'rug', 'histogram']]

#app
app = dash.Dash()

#layout
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

#callback
@app.callback(Output('scatter', 'figure'),
                [Input('eje-x', 'value'),
                Input('eje-y', 'value'),
                Input('marginal-x', 'value'),
                Input('marginal-y', 'value')])
def update_graph(eje_x, eje_y, marginal_x, marginal_y):
    fig = px.scatter(df, 
                     x=eje_x, 
                     y=eje_y, 
                     color='class',
                     marginal_x=marginal_x, 
                     marginal_y=marginal_y,
                     title='Diagrama de dispersión: '+str(eje_x)+' v.s. '+str(eje_y))
    return fig

#run
if __name__ == '__main__':
    app.run_server(debug=True)