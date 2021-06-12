import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_core_components as dcc
import dados

# ==================  Para obter/atualizar os dados de exemplo é necessário executar dados.py  ==================

# Fonte externa de estilo (Bootstrap)
app = dash.Dash(__name__, external_stylesheets=['https://bootswatch.com/5/superhero/bootstrap.css'])

# Gráfico padrão
df = dados.ordenaDados('trocas', 'semiordenado')
fig = px.scatter(df, x='Tamanho', y=['insert', 'quick', 'merge'],
                 labels={'value': 'trocas'}).update_traces(mode='lines+markers')

# Layout da aplicação
app.layout = html.Div([
    # Título principal
    html.H1('Dashboard Métodos de Ordenação', className='col-xs-12', style={
        'textAlign': 'center'}),
    # Título dropdown 1
    dcc.Markdown(
        '''
            ##### Selecione o tipo de característica que deseja comparar:
        '''),
    # Dropdown 1
    dcc.Dropdown(
        id='dropdown1',
        options=[
            {'label': 'Quantidade de trocas', 'value': 'trocas'},
            {'label': 'Quantidade de comparações', 'value': 'comp'},
            {'label': 'Tempo', 'value': 'tempo'}
        ],
        value='trocas',
        clearable=False,
        style={'width': '500px', 'color': 'black'}),
    # Título dropdown 2
    dcc.Markdown(
        '''
            ##### Selecione o tipo de arquivo:
        '''),
    # Dropdown 2
    dcc.Dropdown(
        id='dropdown2',
        options=[
            {'label': 'Arquivo desordenado', 'value': 'desordenado'},
            {'label': 'Arquivo semiordenado', 'value': 'semiordenado'},
            {'label': 'Arquivo ordenado', 'value': 'ordenado'}
        ],
        value='desordenado',
        clearable=False,
        style={'width': '500px', 'color': 'black'}),
    # Gráfico
    dcc.Graph(
        id='grafico',
        figure=fig,
        style={'padding': '20px 20px'}
    ),
    # Rodapé
    html.Footer([
        html.P('© 2021 Utatsu', style={'textAlign': 'center'})
    ])
])


# Integração entre os dados de entrada e a saída na tela
@app.callback(
    Output(component_id='grafico', component_property='figure'),
    Input(component_id='dropdown1', component_property='value'),
    Input(component_id='dropdown2', component_property='value')
)
# Função responsável por atualizar o gráfico de acordo com os dados de entrada
def atualizaGrafico(caracteristicas, arquivo):
    print(caracteristicas, arquivo)
    if caracteristicas is not None and arquivo is not None:
        dt = dados.ordenaDados(caracteristicas, arquivo)
        graf = px.scatter(dt, x='Tamanho', y=['insert', 'quick', 'merge'],
                          labels={'value': caracteristicas}).update_traces(mode='lines+markers')
        return graf
    return fig


# Servidor da aplicação
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)
