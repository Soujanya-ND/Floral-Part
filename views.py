from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime
from floral.models import customer,flower

def greet(request):
 dt=datetime.datetime.now()
 name="Chetan"
 subjects=["PYT","CN","ATC"]
 return render(request,"dt.html",{"dt":dt,"name":name,"subjects":subjects})

def employeedetails(request):
 return render(request,'employeedetails.html',{})


def login(request):
 return render(request,'login.html',{})

def customerlogin(request):
 return render(request,'customerlogin.html')


def ucustomerlogin(request):
  uname=request.GET.get('usname')
  pwd=request.GET.get('pswd')
  print('innn')
  pwd=hashlib.md5(pwd.encode('utf-8')).hexdigest()
  print(uname,pwd)
  u=customer.objects.filter(cust_name=uname,password=pwd)
  if(u):
   print('Successfully logged in')
   response=render(request,'index.html')
   response.set_cookie(uname,'usname')
   return response
  else:
    return render(request,'customerlogin.html')


def customersignin(request):
 return render(request,'customersignin.html')

import hashlib
def ucustomersignin(request):
  uname=request.GET.get('usrname')
  pwd=request.GET.get('psw')
  pwd=hashlib.md5(pwd.encode('utf-8')).hexdigest()

  address=request.GET.get('address')
  email=request.GET.get('email')
  Phone=request.GET.get('Phone')
  print(uname,pwd,address,email,Phone)
  u=customer(cust_name=uname,password=pwd,address=address,email=email,phone_no=Phone)
  u.save()
  return render(request,'customerlogin.html')

def index(request):
 return render(request,'index.html',{})

def addemp(request):
 return render(request,'addemp.html',{})

def products(request):
 return render(request,'products.html',{})

def uproducts(request):
    pro_list=flower.objects.all()
    istr='''
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script>
    function pro(fid)
  {
    $.get("http://localhost:8000/uproducts/", {fid:flower_id}).done(function(data)
    {
      alert(data);
    });
  }
</script>
<header>
        <h1>FLOWER PRODUCTS IN STOCK</h1>
        <h5>want to avail our services ?</h5>
        <button class="btn">SERVICES</button>
 </header>
 '''
    cnt=1
    for fl in pro_list:
      
      istr+='''
  
        <div class="card">

            <img src="http://localhost:8000/static/img/'''+str(cnt)+'''.jpg" alt="Sandwich" class="bg-img" width="100%">
            <div class="content">
                <h4>'''+fl.flower_name+'''</h4>
                <p>Price of each flower =<span style="color: red; font-weight: bold;">'''+str(fl.price)+''' </span></p>
                <button>BUY</button>
            </div>
        </div>

    
            '''
      cnt+=1
      #if cnt%5==0:
       # istr+='''''</div><div class="grid-row" style="display: grid; grid-gap: 20px;">'''''
    return HttpResponse(istr)


def services(request):
  return render(request,'services.html',{})

def order(request):
  return render(request,'order.html',{})