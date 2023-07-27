from django.shortcuts import render,redirect
from django.http import HttpResponse
from emailverification.models import User
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.


def signup(request):
    if request.method == 'POST':
            email=request.POST.get('email')
            password=request.POST.get('password')
            cpassword=request.POST.get('cpassword')
            if (password==cpassword):
                check=User.check_user_exist(email)
                if check:
                    return render(request,'signin.html')
                else:
                    password=make_password(password)
                    user=User(email=email,password=password)
                    user.save()
                    return redirect('signin')
            else:
                error="wrong password entered"
                return render(request,'signup.html',{'error':error})
    else:
        return render(request,'signup.html')
            
            
            
def signin(request):
    if request.method=="GET":
        return render(request,"signin.html")
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        object=User.user_object(email)
        print(object)
      
        if object:
            if check_password(password,object.password):
                request.session['user']=email
                return redirect('home')
            else:
                error="eneterd wrong password"
                return render(request,'signin.html',{'error':error})
                            
        
        
    
def logout(request):
    request.session.pop('user',None)
    return render(request,'signup.html')