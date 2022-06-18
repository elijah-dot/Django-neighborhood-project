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

def join(request,id):
    hood = get_object_or_404(Neighbourhood,id=id)
    request.user.profile.hood =hood
    request.user.profile.save()
    return redirect('home')

def leave(request,id):
    hood = get_object_or_404(Neighbourhood,id=id)
    request.user.profile.hood =None
    request.user.profile.save()
    return redirect('n_hoods')

def my_hood(request,hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    business=Business.objects.filter(hood=hood)
    context={"business":business,
             "hood":hood
    }
    
    return render(request, 'my_hood.html', context)

def business(request,hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    business = Business.objects.filter(hood=hood)
    context={
        'hood':hood,
        'business': business,
    }
    return render(request, 'business.html', context)

def contacts(request,hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    contacts = Contacts.objects.filter(hood=hood)
    context={
        'hood':hood,
        'contacts': contacts
    }
    
    return render(request, 'contacts.html', context)

def announcements(request,hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    posts = Posts.objects.filter(hood=hood)
    current_user = request.user
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES or None)
        if form.is_valid():
            add = form.save(commit=False)
            add.author = request.user.profile
            add.hood = hood
            add.save()
            return redirect('announcements',hood=id)
        context = {
                'hood':hood,
                'posts':posts,
                'form':form,
                 } 
    return render(request, 'announcements.html', context)

def search_results(request):
    if request.method == 'GET':
        name = request.GET.get("query")
        results = Business.objects.filter(name_icontains=name).all()
        message = f"name"
        context = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', context)
    else:
        message = "invalid input"
        return render(request, 'search.html', {'message': message})
    

        

    

