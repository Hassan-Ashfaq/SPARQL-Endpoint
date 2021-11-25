from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from .Query import All_Queries, Mapper

from rdflib import Graph

Knowledge_Graph = Graph()
Knowledge_Graph.parse("graph.nt")

#=============================LOGO IN=========================
def logInUser(request):
    if request.method=='GET':
        return render(request, 'nobel/logInUser.html', {
            'form': AuthenticationForm()
        })
    elif request.method=='POST':
        user = authenticate(request, 
            username=request.POST['username'], 
            password=request.POST['password']
        )
        if user is None:
            messages.error(request, 'Please Enter Correct Name or Password')
            return render(request, 'nobel/logInUser.html', {
                'form': AuthenticationForm()
            })
        else:
            login(request, user)
            return redirect('board')

@login_required(redirect_field_name='LogInUser')
def logOutUser(request):
    if request.method=='GET':
        logout(request)
        return redirect('LogInUser')
    
#=================================================================

@login_required(redirect_field_name='LogInUser')      
def dashboard(request):
    return render(request, 'nobel/dashboard.html', {
        'Mapper': Mapper,
    })

@login_required(redirect_field_name='LogInUser')      
def selectQueryResult(request, id):
    if request.method=='GET':
        Query = All_Queries[id]
        names = []
        result = []
        Result = Knowledge_Graph.query(Query)
        for var in Result.vars:
            names.append(var.split("''")[0])
            
        for stmt in Result:
            col = []
            for i in range(len(stmt)):
                col.append(stmt[i].split("''")[0])
            result.append(col)
        return render(request, 'nobel/selectedResult.html', {
            'Col_names': names,
            'Col_res': result,
        })


@login_required(redirect_field_name='LogInUser')      
def sparqlEndpoint(request):
    return render(request, 'nobel/sparql.html', {})

@login_required(redirect_field_name='LogInUser')      
def queryResult(request):
    if request.method=='POST':
        Query = request.POST['Query']
        Column_names = []
        Column_result = []
        try:
            QueryResult = Knowledge_Graph.query(Query)
            for var in QueryResult.vars:
                Column_names.append(var.split("''")[0])
            for stmt in QueryResult:
                col = []
                for i in range(len(stmt)):
                    col.append(stmt[i].split("''")[0])
                Column_result.append(col)
        except:
            messages.error(request, 'Please Enter Correct Query !')
            return render(request, 'nobel/sparql.html', {})
        return render(request, 'nobel/result.html', {
            'Col_names': Column_names,
            'Col_res': Column_result,
        })
    return redirect('sparqlEnd')