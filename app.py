

    html.Div([

        html.Div([
            html.Label('Choose country'),
            dcc.Dropdown(
                id='country_drop',
                options=country_options,
                value=['Portugal'],
                multi=False
            ),

            html.Br(),

            html.Label('Select year'),
            dcc.Slider(
                id='year_slider',
                min=sum_mig['Year'].min(),
                max=2017,
                marks={str(i): '{}'.format(str(i)) for i in
                       [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]},
                value=2017,
                step=1,
                included=False
            ),

            html.Br(),

            html.Label(''),
            dcc.RadioItems(
                id='mig_radio',
                options=mig_options,
                value='log Net',
                labelStyle={'display': 'block'}
            )

        ], style={'width': '35%', 'display': 'inline-block', 'color' : '#111', 'font-family':'sans-serif', 'height': '300px', 'backgroundColor': '#fff'},
            className='box class2'),

        html.Div([
            html.Div(dcc.Markdown('### MIGRATION AROUND THE WORLD'
                                  '\n\nMigration refers to the movement of people from place to place. People migrate for many different reasons, which can be classified as *economic*, *social*, *political* or *environmental*.'
                                  '\n\n* **Economic migration** is related to finding work or better economic opportunities. '
                                  '\n\n* **Social migration** refers to the search of a better quality of life or to be closer to family and friends.'
                                  '\n\n* **Political migration** occurs when people is moving to escape conflict, political persecution, terrorism, or human rights violations. '
                                  '\n\n* **Environmental** causes of migration include the adverse effects of climate change, natural disasters, and other environmental factors. '
                                  '\n\nOver the last years, migration has become a key issue for countries all over the world. More people than ever live in a country other than the one in which they were born. Therefore, as a group, we thought that it would be interesting to explore migration patterns and their underlying causes.'
                                  )
                     , style={'width': '35%', 'display': 'inline-block', 'height': '500px', 'color': '#111',
                              'font-family': 'sans-serif', 'font-size':'13px', 'text-align': 'justify', 'vertical-align': 'middle',
                              'padding': '5px'}
                     ),
            html.Div(dcc.Graph(
                id='choropleth_graph'
            ), style={'width': '60%', 'display': 'inline-block', 'font-family':'sans-serif', 'color' : '#111',
                      'height': '500px', 'backgroundColor': '#fff'})
        ], style={'width': '100%','display': 'inline-flex', 'height': '550px'}),

    html.Div([
        html.Footer([
            html.Label(["Data Visualization | June 2020 | Carlos Pereira, M20190426 |"
                        " Cátia Duro, M20190394 | João Miguel Lopes, M20190465 | Marta Faria, M20190178"]),

            html.Label([" | Data available at: ", html.A("OECD",
                                                      href="https://www.oecd.org/migration/mig/oecdmigrationdatabases.htm", target="_blank")], style={"margin-top": "0px"})
        ], style ={'width': '100%', 'display': 'inline-block', 'color' : '#111', 'font-family':'sans-serif','font-size':'10px', 'text-align': 'centered','vertical-align': 'middle', 'padding': '5px'},
            className='footer'),

])])])


######################################################Callbacks#########################################################

@app.callback(
    Output('choropleth_graph', 'figure'),
    [Input('mig_radio', 'value')]
)

def update_graph(migvar):
    if migvar=='log Net':
        new_migvar='Net-Migration'
    elif migvar=='log Inflow':
        new_migvar='Migrants Inflow'
    else:
        new_migvar='Migrants Outflow'

    data_choropleth = px.choropleth(sum_mig,
                                    locations="Country",
                                    locationmode="country names",
                                    color=migvar,
                                    hover_name="Country",
                                    color_continuous_scale=px.colors.cmocean.matter,
                                    animation_frame="Year",
                                    projection="natural earth",
                                    title=dict(text="Global " + str(new_migvar), x=.5),
                                    labels={migvar:'Number of migrants <br> [log scale]'})


    fig = go.Figure(data=data_choropleth)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
