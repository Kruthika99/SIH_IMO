
from django.shortcuts import render,redirect
import joblib
import numpy as np
from addshg.models import shg,installments


def signup(request):

        if request.method == 'POST':
            name=request.POST['name']
            act=request.POST['act']
            amount=request.POST['amt']
            amt=int(amount)*100000
            woman=request.POST['wb']
            location=request.POST['location']
            tp=request.POST['tp']
            rate=request.POST['rate']
            reg=request.POST['reg']
            pd=request.POST['pd']
            ycj=request.POST['ycj']
            action=act
            if pd=='Yes' or pd=='yes' or pd=='y':
                pd=1
            else:
                pd=0
            if act=='Tailoring':
                act=1
            elif act=='Handicraft':
                act=2
            elif act=='Handloom':
                act=3
            elif act=='Agriculture':
                act=4
            elif act=='Diary Activities':
                act=5
            elif act == 'Food Processing':
                act = 6
            else:
                act=7
                action="Fishing"
            model = joblib.load('C:/Users/HP/Documents/imo1.pkl')
            x=[int(amount),int(woman),int(ycj),int(tp),act,pd]
            x=np.array(x)
            x=x.reshape(1,-1)
            y_test=model.predict(x)
            if y_test[0]==1:
                s=shg(Name=name,Activity=action,Amount=amt,Woman_beneficiaries=woman,Location=location,TimePeriod=tp,Rate=rate,Registration_id_imo=reg)
                s.save()
                return render(request,'approveSHG.html',{'content':"Loan Approved Successfully!"})
            else:
                return render(request,'approveSHG.html',{'content': "Loan Rejected!!"})
        else:
            return render(request,'approveSHG.html')


def display(request):
    if request.method=='POST':
        reg=request.POST['reg']
        list_shg=shg.objects.values('Name','Amount','Activity').filter(Registration_id_imo=reg)
        return render(request,"displaySHG.html",{'shg':list_shg})
    else:
        list_id=shg.objects.values('Registration_id_imo')
        id=[]
        for i in list_id:
            if i not in id:
                id.append(i)
        return render(request,"displayid.html",{'ids':id})


def payinstallments(request):
    if request.method=='POST':
        name=request.POST['name']
        inst=request.POST['installments']
        reg=request.POST['reg']
        s=shg.objects.get(Name=name,Registration_id_imo=reg)
        s.Amount-=int(inst)
        s.save()
        t=installments(Name=name,Installments=int(inst),Registration_id_imo=reg)
        t.save()
        return redirect('http://127.0.0.1:8000/portal/display')
    else:
        return render(request,'installments.html')