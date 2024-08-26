from django.shortcuts import render
from .models import Trainee ,Track
from .forms import Newtrainee
from django.shortcuts import render,redirect
# Create your views here.

def list_trainee(request):
    
    context={}
    trainees=Trainee.objects.all()
    context['trainee']=trainees
    return render(request,'trainee/list_trainee.html',context)



def create_trainee(request):
    context = {}
    
    if request.method == 'POST':
        form = Newtrainee(request.POST,request.FILES)
        context['form'] = form
        if form.is_valid():
            
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            id_track = form.cleaned_data['id_track']
            image = form.cleaned_data['image']

            
            Trainee.create_trainee(id, name, id_track,image)
            return redirect('list_trainee') 
            
    else:
        form = Newtrainee()
        context['form'] = form
    
    return render(request, 'trainee/create_trainee.html', context)

def trainee_detail(request,id):
    context = {"id":id,'trainee':Trainee.objects.get(pk=id)}
    return render(request,'trainee/trainee_detail.html',context)

def update_trainee(request,id):
    context = {}
    all_tracks = Track.objects.all() 
    context = {"id": id,'trainee':Trainee.objects.get(pk=id),'tracks':all_tracks}
    
    if request.method == 'POST':
        train = Trainee.objects.get(pk=id)
        train.name = request.POST['name']
        track_id = request.POST['id_track']
        track_instance = Track.objects.get(pk=id)
        train.id_track = track_instance 
        train.image=request.FILES['trainee_image']
        train.save()
        return redirect('list_trainee') 
    return render(request,'trainee/update_trainee.html',context)

# @dajaxice_register
def delete_trainee(request,id):
    # dajax = Dajax()
    context={}
    try:
        # dajax.
        Trainee.objects.filter(pk=id).delete()
        context = {"id": id,'msg':'trainee is deleted'}
        return redirect('list_trainee') 
        
    except:
        import sys
        context['error'] =sys.exc_info()[1]
    # return dajax.json()
    return render(request,'trainee/delete_trainee.html',context)


# def create_trainee(request):
#     return render(request,'trainee/create_trainee.html')

# def list_trainee(request):
#     # trainee=[]
#     # tra1={'id':1,'name':'aya','track_id':2}
#     # tra2={'id':2,'name':'ali','track_id':5}
#     # trainee.append(tra1)
#     # trainee.append(tra2)
#     context={}
#     trainees=Trainee.objects.all()
#     context['trainees']=trainees
#     return render(request,'trainee/list_trainee.html',context)

# def create_trainee(req):
#     # context = {'trainees':Trainee.objects.get(id=id)}
    
    
#     #  context={}
#     # context['trainees']=Trainee.objects.all()
#     # if(req.method=='POST'):
#     #     context={}
      
#     #     if(len(req.POST['name'])>0 and len(req.POST['bookname'])<=200):
#     #         traineeobj=Trainee()
#     #         traineeobj.name=req.POST['name']
#     #         # traineeobj.version=req.POST['bookversion']
#     #         traineeobj.id_track_id=Trainee.objects.get(pk=req.POST['t_id'])
#     #        traineeobj.save()
           
#     #         return redirect('book:list_trainee')
#     #     else:
#     #         context['error']='invalid name'
    
#     return render(request,'trainee/create_trainee.html')

# def trainee_detail(request,id):
#     # context = {"id":id}
#     context = {'trainees':Trainee.objects.get(id=id)}
#     return render(request,'trainee/trainee_detail.html',context)

# def update_trainee(request,id):
#     context = {}
#     context = {"id": id}
#     return render(request,'trainee/update_trainee.html',context)

# def delete_trainee(request,id):
#     context = {'trainees':Trainee.objects.get(id=id)}
#     # trainees=Trainee.objects.aget()
#     # context = {'trainee': trainee}
#     return render(request,'trainee/delete_trainee.html',context)