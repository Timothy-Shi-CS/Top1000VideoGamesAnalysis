__author__ = 'Timothy Shi'

import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv("vgsales.csv")

attributeNames = {
    'NA_Sales': 'Total Sales in North America (millions)',
    'EU_Sales': 'Total Sales in Europe (millions)',
    'JP_Sales': 'Total Sales in Japan (millions)',
    'Other_Sales': 'Total Sales in other places (millions)',
    'Global_Sales': 'Total Sales in the world (millions)',
    'Rank': 'Rank',
    'Name': 'Name',
    'Platform': 'Platform',
    'Year': 'Year',
    'Genre': 'Genre',
    'Publisher': 'Publisher'
}

app.layout = html.Div(children=[
    html.H1('Timothy Shi CSE 332 Lab 2'),
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Pie Chart', value='tab-1', children=[
            html.Div([
                html.Label(['Top Selling Video Games Pie Chart']),
                dcc.Dropdown(
                    id='pie_chart_dropdown',
                    options=[
                        {'label': 'Platform', 'value': 'Platform'},
                        {'label': 'Genre', 'value': 'Genre'},
                        {'label': 'Publisher', 'value': 'Publisher'},
                        {'label': 'Year', 'value': 'Year'},
                        {'label': 'Global Sales (in Millions)', 'value': 'Global_Sales'},
                        {'label': 'North America Sales (in Millions)', 'value': 'NA_Sales'},
                        {'label': 'Europe Sales (in Millions)', 'value': 'EU_Sales'},
                        {'label': 'Japan Sales (in Millions)', 'value': 'JP_Sales'},
                        {'label': 'Other Country Sales (in Millions)', 'value': 'Other_Sales'},
                    ],
                    value='Platform',
                    multi=False,
                    clearable=False
                ),
                html.Div([
                    dcc.Graph(id="pie_chart")
                ])
            ])
        ]),
        dcc.Tab(label='Histogram/Bar Chart', value='tab-2', children=[
            html.Div([
                html.Label(['Top Selling Video Game Sales Histogram']),
                dcc.Dropdown(
                    id='histogram_dropdown',
                    options=[
                        {'label': 'Year', 'value': 'Year'},
                        {'label': 'North America Sales (in Millions)', 'value': 'NA_Sales'},
                        {'label': 'Europe Sales (in Millions)', 'value': 'EU_Sales'},
                        {'label': 'Japan Sales (in Millions)', 'value': 'JP_Sales'},
                        {'label': 'Other Country Sales (in Millions)', 'value': 'Other_Sales'},
                        {'label': 'Global Sales (in Millions)', 'value': 'Global_Sales'},
                        {'label': 'Name', 'value': 'Name'},
                        {'label': 'Platform', 'value': 'Platform'},
                        {'label': 'Publisher', 'value': 'Publisher'}
                    ],
                    value='Year',
                    multi=False,
                    clearable=False
                ),
            ]),
            html.Div([
                dcc.Graph(id="histogram")
            ])
        ]),
        dcc.Tab(label='Scatterplot', value='tab-3', children=[
            html.Div(
                style={"width": "45%", "display": "inline-block"},
                children=[
                    html.Label(['Scatterplot x-value']),
                    dcc.Dropdown(
                        id='scatterplot_dropdown_x',
                        options=[
                            {'label': 'Year', 'value': 'Year'},
                            {'label': 'North America Sales (in Millions)', 'value': 'NA_Sales'},
                            {'label': 'Europe Sales (in Millions)', 'value': 'EU_Sales'},
                            {'label': 'Japan Sales (in Millions)', 'value': 'JP_Sales'},
                            {'label': 'Other Country Sales (in Millions)', 'value': 'Other_Sales'},
                            {'label': 'Global Sales (in Millions)', 'value': 'Global_Sales'},
                            {'label': 'Rank', 'value': 'Rank'},
                            {'label': 'Publisher', 'value': 'Publisher'},
                            {'label': 'Platform', 'value': 'Platform'},
                        ],
                        value='Rank',
                        multi=False,
                        clearable=False,
                    ),
                ]
            ),
            html.Div(
                style={"width": "45%", "display": "inline-block"},
                children=[
                    html.Label(['Scatterplot y-value']),
                    dcc.Dropdown(
                        id='scatterplot_dropdown_y',
                        options=[
                            {'label': 'Year', 'value': 'Year'},
                            {'label': 'North America Sales (in Millions)', 'value': 'NA_Sales'},
                            {'label': 'Europe Sales (in Millions)', 'value': 'EU_Sales'},
                            {'label': 'Japan Sales (in Millions)', 'value': 'JP_Sales'},
                            {'label': 'Other Country Sales (in Millions)', 'value': 'Other_Sales'},
                            {'label': 'Global Sales (in Millions)', 'value': 'Global_Sales'},
                            {'label': 'Rank', 'value': 'Rank'},
                            {'label': 'Publisher', 'value': 'Publisher'},
                            {'label': 'Platform', 'value': 'Platform'},
                        ],
                        value='Year',
                        multi=False,
                        clearable=False,
                    ),
                ]
            ),
            html.Div([
                dcc.Graph(id="scatterplot")
            ]),
            # html.Div([
            #     dcc.RangeSlider(
            #         id='x-axis',
            #         min=df['Rank'].min(),
            #         max=df['Rank'].max(),
            #         value=[df['Rank'].min(), df['Rank'].max()],
            #         marks={100: '100', 200: '200', 300: '300', 400: '400', 500: '500', 600: '600',
            #                700: '700', 800: '800', 900: '900', 1000: '1000'},
            #         step=None
            #
            #     )
            # ])
        ]),
    ]),
])


@app.callback(
    Output(component_id='pie_chart', component_property='figure'),
    Input(component_id='pie_chart_dropdown', component_property='value')
)
def update_pie_chart(dropdown_var):
    copy_df = df
    filtered_df = copy_df.filter(items=[dropdown_var]).values.tolist()
    if dropdown_var == 'Platform':
        platforms = ['PS2', 'XBOX 360', 'PS3', 'PS', 'Wii', 'Others']
        num_games = [0] * 6
        for i in range(999):
            if filtered_df[i][0] == 'PS2':
                num_games[0] += 1
            elif filtered_df[i][0] == 'X360':
                num_games[1] += 1
            elif filtered_df[i][0] == 'PS3':
                num_games[2] += 1
            elif filtered_df[i][0] == 'PS':
                num_games[3] += 1
            elif filtered_df[i][0] == 'Wii':
                num_games[4] += 1
            else:
                num_games[5] += 1

        pie_chart = px.pie(
            title='Top 1000 Best Selling Games by Platforms',
            labels=platforms,
            values=num_games,
            names=platforms,
            hole=.5,
        )
    elif dropdown_var == 'Genre':
        genre = ['Action', 'Sports', 'Shooter', 'Role-Playing', 'Platform', 'Others']
        num_games = [0] * 6
        for i in range(999):
            if filtered_df[i][0] == 'Action':
                num_games[0] += 1
            elif filtered_df[i][0] == 'Sports':
                num_games[1] += 1
            elif filtered_df[i][0] == 'Shooter':
                num_games[2] += 1
            elif filtered_df[i][0] == 'Role-Playing':
                num_games[3] += 1
            elif filtered_df[i][0] == 'Platform':
                num_games[4] += 1
            else:
                num_games[5] += 1

        pie_chart = px.pie(
            title='Top 1000 Best Selling Games by Genre',
            labels=genre,
            values=num_games,
            names=genre,
            hole=.5,
        )
    elif dropdown_var == 'Publisher':
        publisher = ['Nintendo', 'Electronic Arts', 'Sony Computer Entertainment', 'Activision', 'Others']
        num_games = [0] * 5
        for i in range(999):
            if filtered_df[i][0] == 'Nintendo':
                num_games[0] += 1
            elif filtered_df[i][0] == 'Electronic Arts':
                num_games[1] += 1
            elif filtered_df[i][0] == 'Sony Computer Entertainment':
                num_games[2] += 1
            elif filtered_df[i][0] == 'Activision':
                num_games[3] += 1
            else:
                num_games[4] += 1

        pie_chart = px.pie(
            title='Top 1000 Best Selling Games by Publisher',
            labels=publisher,
            values=num_games,
            names=publisher,
            hole=.5,
        )
    elif dropdown_var == 'Year':
        year = ['2007', '2008', '2010', '2009', '2011', 'Others']
        num_games = [0] * 6
        for i in range(999):
            if filtered_df[i][0] == 2007:
                num_games[0] += 1
            elif filtered_df[i][0] == 2008:
                num_games[1] += 1
            elif filtered_df[i][0] == 2010:
                num_games[2] += 1
            elif filtered_df[i][0] == 2009:
                num_games[3] += 1
            elif filtered_df[i][0] == 2011:
                num_games[4] += 1
            else:
                num_games[5] += 1

        pie_chart = px.pie(
            title='Top 1000 Best Selling Games by Year',
            labels=year,
            values=num_games,
            names=year,
            hole=.5,
        )

    elif dropdown_var == 'Global_Sales':
        global_sales = ['0-14 M', '15-29 M', '30-44 M', '45-59 M', '60-74 M', '75-90 M']
        num_games = [0] * 6
        for i in range(999):
            if 15 > filtered_df[i][0] >= 0:
                num_games[0] += 1
            elif 30 > filtered_df[i][0] >= 15:
                num_games[1] += 1
            elif 45 > filtered_df[i][0] >= 30:
                num_games[2] += 1
            elif 60 > filtered_df[i][0] >= 45:
                num_games[3] += 1
            elif 75 > filtered_df[i][0] >= 60:
                num_games[4] += 1
            else:
                num_games[5] += 1

        pie_chart = px.pie(
            title='Top 1000 Best Selling Games by Global Sales (in Millions)',
            labels=global_sales,
            values=num_games,
            names=global_sales,
            hole=.5,
        )
    elif dropdown_var == 'NA_Sales':
        na_sales = ['0-9 M', '10-19 M', '20-29 M', '30-39 M', '40-50 M']
        num_games = [0] * 5
        for i in range(999):
            if 10 > filtered_df[i][0] >= 0:
                num_games[0] += 1
            elif 20 > filtered_df[i][0] >= 10:
                num_games[1] += 1
            elif 30 > filtered_df[i][0] >= 20:
                num_games[2] += 1
            elif 40 > filtered_df[i][0] >= 30:
                num_games[3] += 1
            else:
                num_games[4] += 1

        pie_chart = px.pie(
            title='Top 1000 Best Selling Games by North America Sales (in Millions)',
            labels=na_sales,
            values=num_games,
            names=na_sales,
            hole=.5,
        )
    elif dropdown_var == 'EU_Sales':
        eu_sales = ['0-4 M', '5-9 M', '10-14 M', '15-19 M', '20-24 M', '25-30 M']
        num_games = [0] * 6
        for i in range(999):
            if 5 > filtered_df[i][0] >= 0:
                num_games[0] += 1
            elif 10 > filtered_df[i][0] >= 5:
                num_games[1] += 1
            elif 15 > filtered_df[i][0] >= 10:
                num_games[2] += 1
            elif 20 > filtered_df[i][0] >= 15:
                num_games[3] += 1
            elif 25 > filtered_df[i][0] >= 20:
                num_games[4] += 1
            else:
                num_games[5] += 1

        pie_chart = px.pie(
            title='Top 1000 Best Selling Games by Europe Sales (in Millions)',
            labels=eu_sales,
            values=num_games,
            names=eu_sales,
            hole=.5,
        )
    elif dropdown_var == 'JP_Sales':
        jp_sales = ['0-1 M', '2-3 M', '4-5 M', '6-7 M', '8-9 M', '10-11 M']
        num_games = [0] * 6
        for i in range(999):
            if 2 > filtered_df[i][0] >= 0:
                num_games[0] += 1
            elif 4 > filtered_df[i][0] >= 2:
                num_games[1] += 1
            elif 6 > filtered_df[i][0] >= 4:
                num_games[2] += 1
            elif 8 > filtered_df[i][0] >= 6:
                num_games[3] += 1
            elif 10 > filtered_df[i][0] >= 8:
                num_games[4] += 1
            else:
                num_games[5] += 1

        pie_chart = px.pie(
            title='Top 1000 Best Selling Games by Japan Sales (in Millions)',
            labels=jp_sales,
            values=num_games,
            names=jp_sales,
            hole=.5,
        )
    elif dropdown_var == 'Other_Sales':
        other_sales = ['0-1 M', '2-3 M', '4-5 M', '6-7 M', '8-9 M', '10-11 M']
        num_games = [0] * 6
        for i in range(999):
            if 2 > filtered_df[i][0] >= 0:
                num_games[0] += 1
            elif 4 > filtered_df[i][0] >= 2:
                num_games[1] += 1
            elif 6 > filtered_df[i][0] >= 4:
                num_games[2] += 1
            elif 8 > filtered_df[i][0] >= 6:
                num_games[3] += 1
            elif 10 > filtered_df[i][0] >= 8:
                num_games[4] += 1
            else:
                num_games[5] += 1

        pie_chart = px.pie(
            title='Top 1000 Best Selling Games by Other Country Sales (in Millions)',
            labels=other_sales,
            values=num_games,
            names=other_sales,
            hole=.5,
        )
    else:
        pie_chart = px.pie(
            data_frame=copy_df,
            names=dropdown_var,
            hole=.5,
        )

    pie_chart.update_layout(
        title_x=0.5,
        height=600,
        margin=dict(t=170)
    )
    return pie_chart


@app.callback(
    Output(component_id='histogram', component_property='figure'),
    Input(component_id='histogram_dropdown', component_property='value')
)
def update_histogram(dropdown_var):
    # df['total_sale'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales'] + df['Global_Sales']
    # print(df.groupby(['Name'])['total_sale'].sum())
    copy_df = df
    copy_df2 = df[:30]
    if str(dropdown_var) == 'Name':
        hist = px.bar(
            title='Total Sales (in millions) of Top 30 Best Selling Video Games',
            data_frame=copy_df2,
            x=str(dropdown_var),
            y=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"],
            labels={
                'value': 'Number of Sales (millions)'
            }
        )
    else:
        hist = px.histogram(
            title='Top 1000 Best Selling Video Games',
            data_frame=copy_df,
            x=str(dropdown_var),
            nbins=40,
            labels={
                str(dropdown_var): attributeNames[str(dropdown_var)],
            }
        )
    hist.update_layout(
        title_x=0.5,
        margin=dict(b=160),
        height=700
    )
    return hist


@app.callback(
    Output(component_id='scatterplot', component_property='figure'),
    Input(component_id='scatterplot_dropdown_x', component_property='value'),
    Input(component_id='scatterplot_dropdown_y', component_property='value')
)
def update_scatterplot(dropdown_x, dropdown_y):
    copy_df = df
    scatterplot = px.scatter(
        data_frame=copy_df,
        x=str(dropdown_x),
        y=str(dropdown_y),
        hover_name="Name",
        hover_data=["Platform", "Publisher", "Genre"],
        color='Genre',
        size='Global_Sales',
        title=attributeNames[str(dropdown_x)] + ' VS. ' + attributeNames[str(dropdown_y)],
        labels={
            str(dropdown_x): attributeNames[str(dropdown_x)],
            str(dropdown_y): attributeNames[str(dropdown_y)],
        }
        # log_y=True,
    )
    scatterplot.update_layout(
        title_x=0.5,
        margin=dict(b=160),
        height=700
    )
    return scatterplot


if __name__ == '__main__':
    app.run_server(debug=True)
