from django.shortcuts import render


# Create your views here.

def login(request):
    
    return render(request,'account/login.html')


def list_account(request):
    account=[]
    acc1={'id':1,'username':'sara','email':'sara.gamal@gmail.com','password':123}
    acc2={'id':2,'username':'esraa','email':'esraa.gamal@gmail.com','password':323}
    account.append(acc1)
    account.append(acc2)
    context={}
    context['accounts']=account
    return render(request,'account/list_account.html',context)

def create_account(request):
    return render(request,'account/create_account.html')

def account_detail(request,id):
    context = {"id":id}
    return render(request,'account/account_detail.html',context)

def update_account(request,id):
    context = {}
    context = {"id": id}
    return render(request,'account/update_account.html',context)

def delete_account(request,id):
    context = {}
    context = {"id": id}
    return render(request,'account/delete_account.html',context)