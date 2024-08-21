from django.shortcuts import render
from django.shortcuts import render
from .models import Track
# Create your views here.

def create_track(request):
    return render(request,'track/create_track.html')

def list_track(request):
    # track=[]
    # tra1={'id':1,'name':'aya','track_id':2}
    # tra2={'id':2,'name':'ali','track_id':5}
    # track.append(tra1)
    # track.append(tra2)
    context={}
    tracks=Track.objects.all()
    context['tracks']=tracks
    return render(request,'track/list_track.html',context)

def create_track(request):
    return render(request,'track/create_track.html')

def track_detail(request,id):
    # context = {"id":id}
    context = {'tracks':Track.objects.get(id=id)}
    return render(request,'track/track_detail.html',context)

def update_track(request,id):
    context = {}
    context = {"id": id}
    return render(request,'track/update_track.html',context)

def delete_track(request,id):
    context = {'tracks':Track.objects.get(id=id)}
    # tracks=track.objects.aget()
    # context = {'track': track}
    return render(request,'track/delete_track.html',context)