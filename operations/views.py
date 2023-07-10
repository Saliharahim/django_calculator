from django.shortcuts import render
from django.views.generic import View
from django import forms
from geopy.geocoders import Nominatim
 
def get_address(place):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(place)
    return getLoc.address

def get_location(latitude,longitude):
    loc = Nominatim(user_agent="GetLoc")
    Loca=loc.reverse(latitude,longitude)
    return Loca.address


class OperationForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()

class LoginForm(forms.Form):
    usename=forms.CharField()
    password=forms.CharField()

class RegistrationForm(forms.Form):
    firstname=forms.CharField()
    lastname=forms.CharField()
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()


class GeoForm(forms.Form):
    place=forms.CharField()


class GeoView(View):
    def get(self,request,*args,**kw):
        form=GeoForm()
        return render(request,"geo.html",{"form":form})
    def post(self,request,*args,**kw):
        form=GeoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            place=form.cleaned_data.get("place")
            address=get_address(place)
            print(address)

        return render(request,"geo.html",{"form":form,"address":address})
    
class GeolocationForm(forms.Form):
    latitude=forms.IntegerField()
    longitude=forms.IntegerField()

class GeolocationView(View):
    def get(self,request,*args,**kw):
        form=GeolocationForm()
        return render(request,"geolocation.html",{"form":form})
    def post(self,request,*args,**kw):
        form=GeolocationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            latitude=form.cleaned_data.get("latitude")
            longitude=form.cleaned_data.get("longitude")
            address=get_location(latitude,longitude)
            print(address)
            return render(request,"geolocation.html",{"address":address,"form":form})


# Create your views here.

class AdditionView(View):
    def get(self,request,*args,**kw):
        form=OperationForm()
        return render(request,'addition.html',{"form":form})
    def post(self,request,*args,**kw):
        # dict name=request.POST
        form=OperationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=n1+n2

        
        return render(request,'addition.html',{"result":res})
    

class SubtractionView(View):
    def get(self,request,*args,**kw):
        return render(request,'subtraction.html')
    def post(self,request,*args,**kw):
        form=OperationForm(request.POST)
        if form.is_invalid:
            print("valid")
        else:
            print("invalid")
        return render(request,"subtraction.html",{"result":res})


class MutiplicationView(View):
    def get(self,request,*args,**kw):
        return render(request,'mutiplication.html')
    def post(self,request,*args,**kw):
        form=OperationForm(request.POST)
        if form.is_invalid:
            print("valid")
        else:
            print("invalid")
        return render(request,"mutiplication.html",{"result":res})


class DivisionView(View):
    def get(self,request,*args,**kw):
        return render(request,'division.html')
    def post(self,request,*args,**kw):
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        res=n1/n2
        print(res)
        return render(request,"division.html",{"result":res})

class FactorialView(View):
    def get(self,request,*args,**kw):
        return render(request,'factorial.html')
    def post(self,request,*args,**kw):
        n=int(request.POST.get('num'))
        fact=1
        for i in range(1,(n+1)):
            fact=fact*i

        return render(request,"factorial.html",{"fact":fact})
    

class PalindromeView(View):
    def get(self,request,*args,**kw):
        return render(request,'palindrome.html')
    def post(self,request,*args,**kw):
        n=request.POST.get('word')
        if(n==n[::-1]):
            return render(request,'palindrome.html',{"result":'true'})        
        else:
            return render(request,'palindrome.html',{"result":'false'})
        

class AmstrongView(View):
    def get(self,request,*args,**ka):
        return render(request,'amstrong.html')
    def post(self,request,*args,**kw):
        n=int(request.POST.get('num'))

        st=len(str(n))
        sum=0
        temp=n
        while temp>0:
            a=temp%10
            sum=sum+(a**st)
            temp//=10
        if sum==n:
            return render(request,'amstrong.html',{"result":'amstrong'})        
        else:
            return render(request,'amstrong.html',{"result":'not amstrong'})    
# or   result=num==original
# return render(request,'amstrong.html,{"res":result})
# or   original=int(num)
    #   sum=0
    # l=len(num)
    # for n in num:
    #     sum=sum+int(n)**len
    # result=sum==original
    # return render(request,"amstrong.html",{"res":result})





class PrimeView(View):
    def get(self,request,*args,**kw):
        return render(request,'prime.html')
    def post(self,request,*args,**kw):
        n=int(request.POST.get('num'))
        f=0
        if n==1:
            return render(request,'prime.html',{"result":'not defiened'})        
        else:
            for i in range(1,n+1):
                if n%i==0:
                    f=f+1
            if f==2:
                return render(request,'prime.html',{"result":'prime'})        
            else:
                return render(request,'prime.html',{"result":'not prime'})        
            


class PrintevenView(View):
    def get(self,request,*args,**kw):
        return render(request,"even.html")
    def post(self,request,*args,**kw):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        

        even=[n for n in range(n1,n2+1) if n%2==0]
        return render(request,"even.html",{"result":even})

class HomeView(View):
    def get(self,request,*args,**kw):
        return render(request,"home.html")
    

class BodysizeView(View):
    def get(self,request,*args,**kw):
        return render(request,"size.html")
    
    def post(self,request,*args,**kw):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        g=request.POST.get("gender")
        n=n1/n2
        n=round(n,2)
        if g=='female':
            if n<=0.80:
                risk='Low'
                shape='Pear'
            elif n>0.85 and n<=.85:
                risk='Moderate'
                shape='Avocado'
            else:
                risk='High'
                shape='Apple'
        elif g=='male':
            if n<=0.95:
                risk='Low'
                shape='Pear'
            elif n>=0.96 and n<=1:
                risk='Moderate'
                shape='Avocado'
            else:
                risk='High'
                shape='Apple'
        else:
            risk="none"
            shape='none'
        return render(request,"size.html",{"risk":risk,"shape":shape,"bmi":n})
                      
# or we can write context={"gender":"","risk":"","shape":""}
# then give it a value in every condition .eg:-context["risk"]=low
# and then print it   {"result":context}

class TemperatureView(View):
    def get(self,request,*args,**kw):
        return render(request,"temp.html")
    def post(self,request,*args,**kw):
        n=int(request.POST.get("temp"))	
        f=(n * 9/5) + 32

        return render(request,"temp.html",{"farenheat":f})
    

class ExponentView(View):
    def get(self,request,*args,**kw):
        form=OperationForm()
        return render(request,"exponent.html",{"form":form})
    
    def post(self,request,*args,**kw):
        form=OperationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1**n2
        return render(request,"exponent.html",{"result":result,"form":form})
    
class LoginView(View):
    def get(self,request,*args,**kw):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    


class RegistrationView(View):
    def get(self,request,*args,**kw):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kw):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print("form is invalid")
        return render(request,"registration.html")