from django.shortcuts import render
from .models import Account
from .forms import NewAccount
from django.shortcuts import render,redirect
# Create your views here.

def login(request):
    
    return render(request,'account/login.html')


def list_account(request):
    
    context={}
    accounts=Account.objects.all()
    context['accounts']=accounts
    return render(request,'account/list_account.html',context)



def create_account(request):
    context = {}
    
    if request.method == 'POST':
        form = NewAccount(request.POST)
        context['form'] = form
        if form.is_valid():
            
            id = form.cleaned_data['id']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            
            Account.create_acc(id, fname, lname, email, password)
            print('success')
            
    else:
        form = NewAccount()
        context['form'] = form
    
    return render(request, 'account/create_account.html', context)

def account_detail(request,id):
    context = {"id":id}
    return render(request,'account/account_detail.html',context)

def update_account(request,id):
    context = {}
    context = {"id": id,'accounts':Account.objects.get(pk=id)}
    context={}
    # context['accounts']=Account.objects.all()
    # context['accounts']=Account.get(pk=id)
    if(request.method=='POST'):
     
        Account.objects.filter(pk=id).update_acc(id=request.POST['id'],
                                        fname=fname.POST['fname'],
                                        lname=lname.POST['lname'],
                                        email=email.POST['email'],
                                        password=password.POST['password'],
        )
    return render(request,'account/update_account.html',context)

    # context = {}
    
    # if request.method == 'POST':
    #     form = NewAccount(request.POST)
    #     context['form'] = form
      
    #     if form.is_valid():
    #         # account =Account.get()
    #         id = form.cleaned_data['id']
    #         fname = form.cleaned_data['fname']
    #         lname = form.cleaned_data['lname']
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']

            
    #         Account.get(pk=id).update_acc(id, fname, lname, email, password)
    #         form.save()
    #         print('success')
            
    # else:
    #     form = NewAccount()
    #     context['form'] = form
    # return render(request,'account/update_account.html',context)

def delete_account(request,id):
    context={}
    try:
        Account.objects.filter(pk=id).delete()
        context = {"id": id,'msg':'account is deleted'}
       
        
    except:
        import sys
        context['error'] =sys.exc_info()[1]
    return render(request,'account/delete_account.html',context)
    # context = {}
    # context = {"id": id}
        