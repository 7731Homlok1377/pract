import app as app
from django.shortcuts import render
from django.http import  HttpResponse


from plotly.offline import plot
from plotly.graph_objs import Scatter

# Create your views here.

def index(request):
    return render(request, "main/index.html", {'title': 'ndufjdb'})

def user(request):
    return render(request, "main/user.html")

def login(request):
    return render(request, "main/login.html")

def regist(request):
    return render(request, "main/regist.html")
def graph(request):
    return render(request, "main/graph.html")

def plot_div(request):
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
    mode='lines', name='test',
    opacity=0.8, marker_color='green')],
    output_type='div')
    return render(request, "main/index.html", {'plot_div': plot_div})