# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import calc_square_wave

wave = calc_square_wave.generateSquareWave(1, 1)
x = wave["x"]
y = wave["y"]
titleX = wave["titleX"]
titleY = wave["titleY"]
infoSignal = wave["waveInfo"]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Gerador de Onda Quadrada'),

    html.Div(children='''
        Por: Guilherme Rodrigues
    '''),
    html.Div(children='''
        Usando -> Dash: A web application framework for Python.
    '''),
    dcc.Input(id='my-id', value='1', type='number'),
    html.Div(id='my-div'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x, 'y': y, 'type': 'scatter', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Exercicio 48',
                'xaxis':{
                    'title': titleX
                },
                'yaxis':{
                     'title': titleY
                }
            }
        }
    ),

    html.Div(children=infoSignal)
])

# @app.callback(
#     Output(component_id='my-div', component_property='children'),
#     [Input(component_id='my-id', component_property='value')]
# )
# def update_output_div(input_value):
#     print(input_value)
#     return 'You\'ve entered "{}"'.format(input_value)

@app.callback(
    Output('example-graph', 'figure'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    # print(input_value)

    wave = calc_square_wave.generateSquareWave(input_value, 1)
    x = wave["x"]
    y = wave["y"]
    titleX = wave["titleX"]
    titleY = wave["titleY"]
    infoSignal = wave["waveInfo"]

    res = {
        'data': [
            {'x': x, 'y': y, 'type': 'scatter', 'name': 'SF'},
        ],
        'layout': {
            'title': 'Exercicio 48',
            'xaxis':{
                'title': titleX
            },
            'yaxis':{
                    'title': titleY
            }
        }
    }
    return res

if __name__ == '__main__':
    app.run_server(debug=True)