from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# Create your views here.
def login(request):
    try:
        if "username" in request.session:
            return redirect("/home")
        if request.method == "POST":
            return perform_login(request) 
        return render(request, "login.html")
    except KeyError as e:
        return HttpResponse(f"{e} is required")
        # messages.info(request, f"{e} is required")
        # return redirect("/")

    except Exception as e:
        messages.info(request, f"Failed {e}")
        return redirect("/")


def perform_login(request):
    user = auth.authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if not user:
        messages.info(request, f"Failed to authenitcate")
        return redirect("/")
    auth.login(request, user)
    save_session(request, user)
    return redirect("/home")


def save_session(request, user):
    request.session["username"] = user.username
    request.session["email"] = user.email


def validate(request, *args):
    map(lambda x: request.POST[x], args)

@csrf_exempt

def register(request):
    try:
        if request.method == 'POST':
            validate(("first_name", "last_name", "username", "email", "password1",
            "password2"))
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 != password2:
                messages.info(request, "Password does not Not Match!")
                return redirect("register")
                # return HttpResponse(f"Password does not Not Match!")

            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken!")
                return redirect("register")
                # return HttpResponse(f"Email is already taken")

            User.objects.create_user(
                username=request.POST['username'],
                email=email,
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                password=password1
            )
            return redirect('/')
        else:
            return render(request,"register.html")
    except KeyError as e:
        return HttpResponse(f"{e} is required")
    except Exception as e:
        return HttpResponse(f"Failed {e}")