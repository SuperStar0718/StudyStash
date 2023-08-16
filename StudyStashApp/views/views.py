# StudyStashApp/views.py
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from ..models import User
import requests
import re





# Create your views here.


def index_view(request):
    return render(request, 'normal_templates/index.html')

def is_strong_password(password):
    # Check if the password meets the strength requirements.
    # You can customize the requirements as needed (e.g., minimum length, special characters, etc.).
    # For this example, we'll require at least 6 characters, one uppercase letter, one lowercase letter,
    # one digit, and one special character.
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$"
    return re.match(pattern, password)



def normal_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        # Use get_user_model() to get the appropriate user model
        User = get_user_model()

        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!', extra_tags='danger')
            return render(request, 'normal_templates/normal_register.html')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!', extra_tags='danger')
            return render(request, 'normal_templates/normal_register.html')

        # Check if the passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!', extra_tags='danger')
            return render(request, 'normal_templates/normal_register.html')

        # Check if the password is strong
        if not is_strong_password(password):
            messages.error(request, 'Password not strong! It should have at least 6 characters, '
                                    'one uppercase letter, one lowercase letter, one digit, '
                                    'and one special character (@$!%*?&)', extra_tags='danger')
            return render(request, 'normal_templates/normal_register.html')

        # Create a new user object and save it to the database
        user = User(email=email, first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)  # Use set_password to hash the password
        user.save()

        messages.success(request, 'Registration successful!, You can now login', extra_tags='success')
        return redirect('login')  # Assuming you have a 'login' URL defined for the login page

    return render(request, 'normal_templates/normal_register.html')




def LoginUserView(LoginView):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Use get_user_model() to get the appropriate user model
        User = get_user_model()

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password', extra_tags='danger')
            return render(request, 'registration/logain.html')

        # Check if the provided password matches the user's password
        if not user.check_password(password):
            messages.error(request, 'Invalid username or password', extra_tags='danger')
            return render(request, 'registration/login.html')

        # Proceed with authentication
        # Log the user in
        login(request, user)

        # Redirect the user to the 'active_first_time_user/' URL
        return redirect('active_first_time_user')

    return render(request, 'registration/login.html')






def statements_view(request):
    # Add any logic or data processing here if needed
    return render(request, 'normal_templates/statements.html')


def normal_studystash_store(request):
     # You can add any additional logic or data processing here if needed
     return render(request, 'normal_templates/normal_studystash_store.html')  
@login_required
def active_first_time_user(request):
    # Add any logic you want for this view
    # For example, you can retrieve data from the database or perform other actions
    return render(request, 'active_templates/active_first_time_user.html')   
@login_required
def active_index(request):
    # Add any logic you want for this view
    # For example, you can retrieve data from the database or perform other actions
    return render(request, 'active_templates/active_index.html')  
@login_required
def active_studystash_store(request):
    return render(request, 'active_templates/active_studystash_store.html')

def normal_forgot_password(request):
    # Your view code here
    return render(request, 'normal_templates/normal_forgot_password.html')
@login_required
def active_studentinfo_checkout_view(request):
    # Add any logic or data processing you need for the view here
    return render(request, 'active_templates/active_studentinfo-checkout.html')
@login_required
def active_session_expired(request):
    # Add any logic or data processing you need for the view here
    return render(request, 'active_templates/active_session_expired.html')    

def user_logout(request):
    logout(request)
    return redirect('index')  # Redirect to the desired page after logout
@login_required
def active_session_membership(request):
    # Add any necessary logic here
    return render(request, 'active_templates/active_session_membership.html')

@login_required
def active_account_deactivated_view(request):
    return render(request, 'active_templates/active_account_deactivated.html')
