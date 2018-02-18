import dash
import dash_core_components as dcc
import dash_html_components as html

from Graphs import figure
from Graphs import figure1
from Graphs import figure2
from Graphs import figure3
from Graphs import figure4

app=dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout = html.Div ([
	html.Div([
		html.H1("Homework 3")
		]),
    #row1
	html.Div([
	 	html.Div([html.H2(children="Graph 1"),
	 		"The graph on the right hand side is showing correlations of different variables (call them from x1 to x8) with employee churn. Data is artificial, manually inputted by the developer. Recreate the graph. Small coloring or corelation value differences will be neglected."
	 		], className='four columns'),
	 	html.Div([
	 		dcc.Graph(id='figure4',figure=figure4)], className='six columns'),
	 		], className="row"),
	#row2
	html.Div([
		html.Div([html.H2(children="Graph 2"),
			"One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph."
			], className = 'four columns'),
		html.Div([
			dcc.Graph(id='figure',figure=figure)], className='six columns'),
	 		], className="row"),
	#row3
	html.Div([
		html.Div([html.H2(children="Graph 3 and 4"),
			"The two graphs on this row are based on Google's stock (WIKI/GOOGL) and Bitcoin's (BCHARTS/ABUCOINSUSD) prices sourced from Quandl. First, percentage changes are calculated. Then the latter is plotted using Box plot to find the distribution and outliers. In the end the first 4 percentage changes (apart from the very first one, which is N/A) are plotted in a table. Recreate similar graphs with the same values (minor styling is neglected)."
			], className = 'four columns'),
		html.Div([
			dcc.Graph(id='figure1',figure=figure1)], className='six columns'),
	 		
	 	html.Div([
			dcc.Graph(id='figure2',figure=figure2)], className='two columns')
	 		], className="row"),
	#row4
	html.Div([
		html.Div([html.H2(children="Graph 5"),
			"Last graph is based on manually inputted data. It shows the Roadmap developed by an artificial startup. Task 1 is assumed to take the whole Janduary, while Task 2 is starting from March and ending in mid April. Afterwards, Task 3 begins and ends in the end of September. Recreate a similar Roadmap"
		], className = 'four columns'),		
		html.Div([
			dcc.Graph(id='fig',figure=figure3)], className='eight columns'),
	 		], className="row")  
	 		      ])

if __name__ == '__main__':
    app.run_server(debug=True)

	