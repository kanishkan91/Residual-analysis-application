#Import packages
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash_table import DataTable
from plotly import tools
from dash.dependencies import Input, Output

#Declare application
app=dash.Dash(__name__)
application=app.server

#App layout

#Read data. Note that data has been generated using the GenerateResiduals function
data=pd.read_csv('Residuals.csv')
dataMain=pd.read_csv('Residuals.csv')
app.layout = html.Div([html.Div(
    [
        dcc.Markdown(
            '''
            ### Exploring multi dimensional residual calculations using a python function and dashboard
            The below visualization app allows the user to explore residuals for different variables using GDP per capita at PPP as the IV, using a specailized function described below . 
            For the code, please visit my [github]("https://github.com/kanishkan91/Py-Dash-GlobalDisplacementswithHoverFunctionality") page.
            Use the slider under the plot to change the year.
            '''.replace('  ', ''),
            className='eight columns offset-by-three'
        )
    ], className='row',
    style={'text-align': 'center', 'margin-bottom': '20px'}
),

    html.Div([
        html.Div(dcc.Dropdown(id='Selector',
            options=[{'label':'Health expenditure as a % of GDP','value':'Health expenditure as a % of GDP'},
                     {'label': 'Average years of education for the population aged 15+', 'value': 'Average years of education for the population aged 15+'},
                     {'label': 'Average life expectancy at birth', 'value': 'Average life expectancy at birth'},
                     {'label': 'Education Quality- Average adult test score', 'value': 'Education Quality- Average adult test score'},
                     {'label': 'Education expenditure as a % of GDP',
                      'value': 'Education expenditure as a % of GDP'},
                     {'label': 'Adult stunting',
                      'value': 'Adult stunting'},
                    {'label': 'Corruption Perception Index',
                      'value': 'Corruption Perception Index'},
                    {'label': 'Economic Freedom Index (Fraser Index)',
                      'value': 'Economic Freedom Index (Fraser Index)'},
                    {'label': 'Governance effectiveness',
                      'value': 'Governance effectiveness'},
                    {'label': 'Polity index',
                      'value': 'Polity index'},
                    {'label': 'Research and development expenditure as a % of GDP',
                      'value': 'Research and development expenditure as a % of GDP'},
                    {'label': 'Tertiray graduates from science and education',
                      'value': 'Tertiray graduates from science and education'}
                     ],
            value='Health expenditure as a % of GDP'
        ),style={'height': '50px', 'width': '100%','display': 'inline-block'}),
        html.Div(dcc.Graph(id='graph-with-slider', style={'height': 450},
              hoverData={'points': [{'text': 'India'}]}
                  ),style={'height': '500px', 'width': '100%','display': 'inline-block'}),
        html.Div(dcc.Slider(id='slider',vertical=False
                   ),style={'height': '50px', 'width': '100%','display': 'inline-block'}),
       dcc.Graph(id='time-series',style={'display': 'inline-block', 'width': '95%','float':'left','height': 400})
    ], style={'width': '69%', 'float': 'left', 'display': 'inline-block', 'font': '15', 'height': '100%'})

    ,
    dcc.Textarea(
        placeholder='Enter a variable name...',
        value=''
              'Explanation of the features available in the dashboard-'
              ''
              ''
              ''
              '''
                             
1. The residuals and the resultant statistics are calculated using the GenerateResiduals function.

2. The 3D scatter plot can be used to explore the IV (GDP per capita), the selected DV and the residuals themselves.

3. The color bar shows the range of the residuals which is technically a 4th dimension.

4. The table in the right hand corner shows different summary stats like the R-Squared, standard error, co-efficients and the n.

5. Finally, the user can hover over any country and see the predicted vs the actual over time.'''''
              '''
            ''''',
        style={'display': 'inline-block', 'width': '30%', 'float': 'right', 'height': '150px'}
    ),
    html.Br(),
    html.Br(),
    html.Div(id='result',
             style={'display': 'inline-block', 'width': '30%', 'float': 'right', 'height': '50px', 'font': '20'}),
    html.Div(DataTable(id='table1'),style={'display': 'inline-block', 'width': '30%', 'float': 'right', 'height': '150px'}),


])


#Define callback for slider

@app.callback(
    dash.dependencies.Output('slider', 'marks'),
    [dash.dependencies.Input('Selector', 'value')])

def update_slider(value):
    data1=data[data['Series']==value]
    data1.Year=data1.Year.astype(str)
    marks={str(Year):str(Year) for Year in data1['Year'].unique() }

    return(marks)

@app.callback(
    dash.dependencies.Output('slider', 'min'),
    [dash.dependencies.Input('Selector', 'value')])

def update_slider(value):
    data2=data[data['Series']==value]
    data2.Year=data2.Year.astype(int)
    min= data2['Year'].min()

    return(min)


@app.callback(
    dash.dependencies.Output('slider', 'max'),
    [dash.dependencies.Input('Selector', 'value')])

def update_slider(value):
    data3 = data[data['Series']==value]
    data3.Year = data.Year.astype(int)
    max = data3['Year'].max()

    return(max)

@app.callback(
    dash.dependencies.Output('slider', 'value'),
    [dash.dependencies.Input('Selector', 'value')])

def update_slider(val):
    data2=data[data['Series']==val]
    data2.Year=data2.Year.astype(int)
    value= data2['Year'].min()

    return(value)

@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('Selector', 'value'),
     dash.dependencies.Input('slider','value')])

def update_plot(value,value1):



    data4 = dataMain[dataMain['Series'] == value]
    data4.Year = data4.Year.astype(int)
    data4 = data4[data4['Year'] == value1]
    trace=go.Scatter3d(
        x=data4['x'],
        y=data4['y'],
        z=data4['Resid'],
        text=(data4['Country']),
        mode='markers+text',
        textposition='top center',
        textfont=dict(
            size=8
        ),
        marker=dict(
            size=8,
            color= data4['Resid'],  # set color to an array/list of desired values
            colorscale='Viridis',  # choose a colorscale
            opacity=0.8
            , colorbar=dict(
                title='Range of residual values'
            ))

    )

    data=[trace]

    layout = go.Layout(
                       margin=dict(
                           l=0,
                           r=0,
                           b=0,
                           t=0
                       ),
                       height=500,
                       width=1000,
                       scene=dict(yaxis=dict(
                           title=str(value)),
                           xaxis=dict(
                               title='Logged GDP'),
                           zaxis=dict(
                               title='Residuals'))
                       )
    return  {'data': data,
            'layout': layout}

@app.callback(
    dash.dependencies.Output('table1', 'columns'),
    [dash.dependencies.Input('Selector', 'value'),
     dash.dependencies.Input('slider','value')])

def update_table(value,value1):
    data5=dataMain[dataMain['Series'] == value]
    data5.Year = data5.Year.astype(int)
    data5=data5.drop_duplicates('Year')
    data5 = data5[['Year', 'n', 'R-squared', 'Constant', 'X-coefficient', 'Std-error']]
    data5 = data5.sort_values(by=['Year'])
    columns = [{"name": i, "id": i} for i in data5.columns]

    return(columns)


@app.callback(
    dash.dependencies.Output('table1', 'data'),
    [dash.dependencies.Input('Selector', 'value'),
     dash.dependencies.Input('slider', 'value')])
def update_table(value, value1):
    data5 = dataMain[dataMain['Series'] == value]
    data5.Year = data5.Year.astype(int)
    data5=data5.drop_duplicates('Year')
    data5=data5[['Year','n','R-squared','Constant','X-coefficient','Std-error']]
    data5=data5.sort_values(by=['Year'])
    data = data5.to_dict('records')

    return (data)

@app.callback(
    dash.dependencies.Output('time-series','figure'),
    [dash.dependencies.Input('graph-with-slider','hoverData'),
     dash.dependencies.Input('Selector', 'value')])

def update_timeseries(hoverData,value):
    data6 = dataMain[dataMain['Series'] == value]
    data6.Year = data6.Year.astype(int)
    data6=data6[data6['Country']==hoverData['points'][0]['text']]
    data6 = data6.sort_values(by=['Year'])
    trace1=go.Scatter(
        x=data6['Year'],
        y=data6['predicted'],
        mode='lines',
        name='Predicted value',
        marker=dict(
            color='#3D9970'
        ))
    trace2=go.Scatter(
        x=data6['Year'],
        y=data6['y'],
        mode='lines',
        name='Actual value',
        marker=dict(
            color='rgba(152, 0, 0, .8)'
        )
    )



    fig = tools.make_subplots(rows=1, cols=1, specs=[[{}]],
                              shared_xaxes=True, shared_yaxes=True,
                              vertical_spacing=0.001)

    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 1, 1)


    fig['layout'].update(
                         title='Predicted vs actual for ' + str(hoverData['points'][0]['text'] +' for '+str(value)),
        yaxis=dict(title='Value'),
        xaxis=dict(title='Year')

    )

    return fig

if __name__ == '__main__':
    application.run_server(debug=True)



