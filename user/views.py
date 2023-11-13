from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def loginView(request):

    loginForm= None

    if request.method == "POST":

        loginForm = LoginForm(request.POST)
        user = authenticate(request, username=loginForm.data["username"], password=loginForm.data["password"])
        if user is not None:
            login(request,user)
            return redirect("journals")
    elif request.method == "GET":
        loginForm = LoginForm()
    
    return render(request,"login.html",{"form":loginForm})
    


def register(request):
    newForm = None
    if request.method == "POST":
        newForm = RegisterForm(request.POST)

        if newForm.is_valid():

            cleanedForm = newForm.cleaned_data
        
            user = User.objects.create_user(cleanedForm["username"],
                                            password=cleanedForm["password"],
                                            first_name=cleanedForm["first_name"],
                                            last_name = cleanedForm["last_name"])
            return redirect("login")
    elif request.method == "GET":
        newForm = RegisterForm()
    
                    
    return render(request,"register.html",{"form":newForm})

def logOutUser(request):

    logout(request)


    return redirect("login")