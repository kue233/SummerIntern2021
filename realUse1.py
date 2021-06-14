import plotly.express as px
import plotly.graph_objects as go
import chart_studio.tools as tls
import datetime
import pandas as pd
import pandas_datareader as data
import plotly.io as pio

class CreateGraph():
    def makeList(str):
        if str.__contains__(" ") == False:
            return [str]
        
        else:
            return str.split()

    def createGraphs(self,user_input, start=None, end=None, y_value='High'):
        title = ""
        tickers = self.makeList(user_input)
        
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
