from django.shortcuts import render

from home.models import register

# Create your views here.
def index(request):
    return render(request, 'home.html')
def login(request):

    if request.method == 'POST':
        nmo=request.POST['nmo']
        password=request.POST['your_pass']
        check_list=None
        check_list = register.objects.get(nmo=nmo,password=password)
        if check_list!=None:
            return render(request,'home.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def reg(request):
    if request.method == 'POST' :
        nmo=request.POST['nmo']
        headname=request.POST['headname']
        address=request.POST['address']
        state=request.POST['state']
        phno=request.POST['phno']
        uniqueid=request.POST['uniqueid']
        password=request.POST['password']
        s=register(nmo=nmo,headname=headname,address=address,state=state,phno=phno,uniqueid=uniqueid,password=password)
        s.save()
        return render(request,'imo_portal.html')
    return render(request,'register.html')

def portal(request):
    return render(request,'imo_portal.html')