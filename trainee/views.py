from django.shortcuts import render

# Create your views here.

def create_trainee(request):
    return render(request,'trainee/create_trainee.html')

def list_trainee(request):
    trainee=[]
    tra1={'id':1,'name':'aya','track_id':2}
    tra2={'id':2,'name':'ali','track_id':5}
    trainee.append(tra1)
    trainee.append(tra2)
    context={}
    context['trainees']=trainee
    return render(request,'trainee/list_trainee.html',context)

def create_trainee(request):
    return render(request,'trainee/create_trainee.html')

def trainee_detail(request,id):
    context = {"id":id}
    return render(request,'trainee/trainee_detail.html',context)

def update_trainee(request,id):
    context = {}
    context = {"id": id}
    return render(request,'trainee/update_trainee.html',context)

def delete_trainee(request,id):
    context = {}
    context = {"id": id}
    return render(request,'trainee/delete_trainee.html',context)