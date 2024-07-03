from django.shortcuts import render, HttpResponse, redirect
from copy import deepcopy
from .models import Shop 

def home(request):
 return render(request,'home.html')

def shopreg(request):
 sname=request.POST["sname"]
 address=request.POST["address"]
 sid=str(len(sname))+sname[0]+sname[1]
 ot=str(request.POST["ot"])
 ct=str(request.POST["ct"])
 img=request.FILES.get("img")	
 o=Shop(sname=sname,sid=sid,address=address,ot=ot,ct=ct,img=img)
 o.save()
 return redirect('sellerp',sid=sid,flag=1)

def takin(request):
 sid=request.POST["sid"]
 n=int(request.POST["n"])
 st=""
 obj=Shop.objects.get(sid=sid)
 for i in range(1,(n+1)):
  st=st+request.POST["p"+str(i)]+" "+str(request.POST["pn"+str(i)])+" "+str(request.POST["q"+str(i)])+"\t"
 print(st)
 obj.p=obj.p+st
 obj.save()
 return redirect('home')

def updaterec(request):
 sid=request.POST["sid"]
 c=int(request.POST["c"])
 st=""
 obj=Shop.objects.get(sid=sid)
 for i in range(1,int(c)):
  st=st+request.POST["pn"+str(i)]+" "+str(request.POST["p"+str(i)])+" "+str(request.POST["q"+str(i)])+"\t"
 print(st)
 obj.p=st
 obj.save()
 return redirect('home')

def updatein(request):
 sid=request.POST["sid"]
 st=""
 obj=Shop.objects.get(sid=sid)
 l=obj.p
 l=l.split("\t")
 for i in range(len(l)):
  l[i]=l[i].split(" ")
 return render(request,'updateind.html',{'sid':sid,'list':l})

def delin(request):
 sid=request.POST["sid"]
 obj=Shop.objects.get(sid=sid)
 obj.p="	"
 obj.save()
 return redirect('home')

def shopin(request):
 return render(request,'shopinterface.html')

def adds(request):
 return render(request,'addshop.html') 

def sell(request,sid=0,flag=0):
 return render(request,'seller/seller.html',{'sid':sid,'flag':flag})

def de(request):
 return render(request,'delete.html')

def up(request):
 return render(request,'update.html')
# Create your views here.
