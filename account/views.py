from django.shortcuts import render
from .models import Account
from .forms import NewAccount
from django.shortcuts import render,redirect
# from dajax.core import Dajax
# from dajaxice.utils import deserialize_form
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
        form = NewAccount(request.POST,request.FILES)
        context['form'] = form
        if form.is_valid():
            
            id = form.cleaned_data['id']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            image = form.cleaned_data['image']

            
            Account.create_acc(id, fname, lname, email, password,image)
            return redirect('list_account') 
            
    else:
        form = NewAccount()
        context['form'] = form
    
    return render(request, 'account/create_account.html', context)

def account_detail(request,id):
    context = {"id":id,'account':Account.objects.get(pk=id)}
    return render(request,'account/account_detail.html',context)

def update_account(request,id):
    context = {}
    context = {"id": id,'account':Account.objects.get(pk=id)}
    if request.method == 'POST':
        acc = Account.objects.get(pk=id)
        acc.fname = request.POST['fname']
        acc.lname = request.POST['lname']
        acc.email = request.POST['email']
        acc.password = request.POST['password']
        acc.image=request.FILES['acc_image']
        acc.save()
        return redirect('list_account') 
    return render(request,'account/update_account.html',context)

# @dajaxice_register
def delete_account(request,id):
    # dajax = Dajax()
    context={}
    try:
        # dajax.
        Account.objects.filter(pk=id).delete()
        context = {"id": id,'msg':'account is deleted'}
        return redirect('list_account') 
        
    except:
        import sys
        context['error'] =sys.exc_info()[1]
    # return dajax.json()
    return render(request,'account/delete_account.html',context)
    # context = {}
    # context = {"id": id}
        