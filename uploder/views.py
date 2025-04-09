from django.shortcuts import render,redirect,HttpResponse
from .models import Document
from .forms import DocForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
# Create your views here.

def front_page(request):
    return render(request,'page.html')

@login_required
def home(request):
    documents = Document.objects.filter(user = request.user)
    return render(request, "base.html", {"documents": documents})

@login_required
def upload(request):
    if request.method == "POST":
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user  
            document.save()
            return redirect('home')
        else:
            return HttpResponse("Error in form submission")

    form = DocForm()
    return render(request, 'upload.html', {'form': form})


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')


        if password == password2:

            if User.objects.filter(username=username).exists():
                return render(request, "register.html", {"error": "Username already taken"})
            

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()


            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

            return redirect('login')  

        else:
            return render(request, "register.html", {"error": "Passwords do not match"})

    return render(request, "register.html")

def views_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')  # Corrected variable name
        user = authenticate(request, username=username, password=password)  # Corrected function call
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid username or password")
        
    return render(request, 'login.html')

def views_logout(request):
    logout(request)
    return redirect('front_page')

def about(request):
    return render(request,'about.html')

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Document

def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    # Ensure only the owner or admin can delete
    if request.user == document.user or request.user.is_superuser:
        document.delete()
        messages.success(request, "Document deleted successfully.")
    else:
        messages.error(request, "You do not have permission to delete this document.")

    return redirect('home')  # Redirect to the home page after deletion

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'profile': profile, 'form': form})
