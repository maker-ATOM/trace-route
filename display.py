import plotly.graph_objects as go
import plotly.express as px

def mapsInit(fig):
    fig.update_layout(
        showlegend = True,
        mapbox = {
        'center': {'lon': 10, 'lat': 30},
        'style': "open-street-map",
        'zoom': 1.8},
    margin ={'l':40,'t':40,'b':40,'r':40}
   )
    
def addRoute(fig, lats, longs, city):
    fig.add_trace(go.Scattermapbox(
        name = 'route',
        text = city,
        mode = "markers+lines",
        lon = longs,
        lat = lats,
        marker = {'size':10},
        line = dict(width=2)
        ))
    
def addNode(fig, lats, longs, city, name):
    fig.add_trace(go.Scattermapbox(
        name = name,
        text = city,
        mode = "markers+text",
        lon = [longs],
        lat = [lats],
        marker = {'size':12}
        ))


