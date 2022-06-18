from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .forms import UserRegistrationForm,ProfileUpdateForm,UserUpdateForm,PostForm
from .models import Neighbourhood,Profile,Business,Contacts,Posts
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .email import send_welcome_email

# Create your views here.
def home(request):
    hoods = Neighbourhood.objects.all()
    context = {
        'hoods':hoods
    }
    
    return render(request, 'home.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            # send_welcome_email(name,email)

            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration_form.html',{'form':form})

def profile(request):
    user=request.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.Files,instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "User updated successfully")
            return redirect('profile')
        
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)
        
    context={
        'user_form': user_form,
        'profile_form': profile_form,
        'user':user,
    }
    return render(request, 'profile.html', context)

def n_hoods(request):
    hoods = Neighbourhood.objects.all()
    context = { 'hoods':hoods }
    return render(request, 'n_hoods.html', context)

def join(request):
    hood = get_object_or_404(Neighbourhood,id=id)
    request.user.profile.hood =hood
    request.user.profile.save()
    return redirect('home')