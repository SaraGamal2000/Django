from django.shortcuts import render
from .models import Trainee
# Create your views here.

def create_trainee(request):
    return render(request,'trainee/create_trainee.html')

def list_trainee(request):
    # trainee=[]
    # tra1={'id':1,'name':'aya','track_id':2}
    # tra2={'id':2,'name':'ali','track_id':5}
    # trainee.append(tra1)
    # trainee.append(tra2)
    context={}
    trainees=Trainee.objects.all()
    context['trainees']=trainees
    return render(request,'trainee/list_trainee.html',context)

def create_trainee(req):
    # context = {'trainees':Trainee.objects.get(id=id)}
    
    
    #  context={}
    # context['trainees']=Trainee.objects.all()
    # if(req.method=='POST'):
    #     context={}
      
    #     if(len(req.POST['name'])>0 and len(req.POST['bookname'])<=200):
    #         traineeobj=Trainee()
    #         traineeobj.name=req.POST['name']
    #         # traineeobj.version=req.POST['bookversion']
    #         traineeobj.id_track_id=Trainee.objects.get(pk=req.POST['t_id'])
    #        traineeobj.save()
           
    #         return redirect('book:list_trainee')
    #     else:
    #         context['error']='invalid name'
    
    return render(request,'trainee/create_trainee.html')

def trainee_detail(request,id):
    # context = {"id":id}
    context = {'trainees':Trainee.objects.get(id=id)}
    return render(request,'trainee/trainee_detail.html',context)

def update_trainee(request,id):
    context = {}
    context = {"id": id}
    return render(request,'trainee/update_trainee.html',context)

def delete_trainee(request,id):
    context = {'trainees':Trainee.objects.get(id=id)}
    # trainees=Trainee.objects.aget()
    # context = {'trainee': trainee}
    return render(request,'trainee/delete_trainee.html',context)