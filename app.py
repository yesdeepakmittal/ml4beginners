import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

#---------------------------------------------------------------------
#defining sales of each quarter
Quarter = ['Q1','Q2','Q3','Q4']

sale_laptop = [100,120,130,160]
sale_mobile = [200,250,280,350]
sale_pwrbnk = [150,130,170,110]

#defining color
color_laptop = 'green'
color_mobile = 'blue'
color_pwrbnk = 'red'

#defining heading & title
heading = 'Hurry! You are getting it👍👍'
title = 'Basic Sales Dashboard'
top_tab_title = 'Sales Data'

#defining item label
label_laptop,label_mobile,label_pwrbnk = 'Laptop','Mobile','Powerbank'

#----------------------------------------------------------------------
#defining data
data_laptop = go.Bar(
	x = Quarter,
	y = sale_laptop,
	name = label_laptop,
	marker = {'color':color_laptop})

data_mobile = go.Bar(
	x = Quarter,
	y = sale_mobile,
	name = label_mobile,
	marker = {'color':color_mobile})

data_pwrbnk = go.Bar(
	x = Quarter,
	y = sale_pwrbnk,
	name = label_pwrbnk,
	marker = {'color':color_pwrbnk})

#definig complete sales data
sales_data = [data_laptop,data_mobile,data_pwrbnk]

#defining layout
sales_layout = go.Layout(barmode='group',title=title)

#defining figure
sales_figure = go.Figure(data=sales_data,layout=sales_layout)

#defining app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
server = app.server
app.title = top_tab_title

app.layout = html.Div(children=[
	html.H1(heading),
	dcc.Graph(id='sales',figure=sales_figure),
	html.A('Visit Vanijya',href='https://vanijya.tech/')])


if __name__ == '__main__':
    app.run_server(debug=True)
    #app.run_server(host='0.0.0.0', port=8080 ,debug=True)
    #choose any above