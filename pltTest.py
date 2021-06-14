#!C:\Users\kue84\AppData\Local\Programs\Python\Python39\python.exe


"""
import plotly.express as px
import plotly.graph_objects as go
#import chart_studio.tools as tls
import datetime
import pandas_datareader as data
import plotly.io as pio
"""
import cgi
import cgitb
#from realUse1 import CreateGraph
cgitb.enable()
form = cgi.FieldStorage()
ticker = form.getvalue("ticker")
"""
graph = CreateGraph()
graph.createGraphs(ticker)
"""
"""
def makeList(str):
    if str.__contains__(" ") == False:
        return [str]
    
    else:
        return str.split()

def createGraphs(user_input, start=None, end=None, y_value='High'):
    title = ""
    tickers = makeList(user_input)
    
    if len(tickers) == 1:
        d = data.DataReader(tickers[0],'yahoo', start, end)
        fig = px.line(d, y=y_value, template = 'plotly_dark', hover_data=d.columns)
        
    else:
        #create a list of databases 
        list = []
        for x in tickers:
            list.append(data.DataReader(x, 'yahoo', start, end))
        
        #plot each database 1 by 1 
        fig = go.Figure()
        for x in range(len(list)):
            fig.add_trace(go.Scatter(x=list[x].index,y=list[x][y_value], name=tickers[x]))
            
    #ending styling
    for _ in range(len(tickers)):
        if _ != len(tickers)-1:
            title += (tickers[_] + " " + y_value + " vs ")
        else:
            title += (tickers[_] + " " + y_value)

    fig.update_layout(title=title, title_x=0.5, template='plotly_dark')    
    pio.write_html(fig, file='../htdocs/tickerPic.html', auto_open=False)
"""

print("Content-type:text/html\r\n\r\n")



print("""
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>result</title>
    </head>
    <body>
        <iframe src="tickerPic.html"></iframe>
    </body>
</html>

""")


"""
    <p>result test is good</p>
    <img src="testPic.png" alt="tmnk" width="500" height="600"></img>
    <img src="https://i.imgur.com/n95jzfa.png" width=101 height=64 border=0 alt=""></img>
    <object width="500" height="500" data="tickerPic.html" >ticker info</object>
    <a href="../htdocs/tickerPic.html">see more info</a>
    <iframe src="D:/aa.png"></iframe>
"""
