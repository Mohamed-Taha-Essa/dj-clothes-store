from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

from .forms import SignupForm ,ActivateUserForm
from .models import Profile

from products.models import Product ,Brand,Review
# Create your views here.

def signup(request):
    '''
    create new user, profile
    send email with code
    redirect user to activate code
    '''
    # if request.user.is_authenticated:
    #     return redirect('/')

    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save(commit=True)
            # how i can access user befor save(i don't have user yet) i have user creation form
            user.is_active = False
            form.save()            #--------> trigger signals(create profile code) why?? as i create user
            
            profile =Profile.objects.get(user__username = username)
            #send email 
            send_mail(
                "Activate Your email",
                f"Welcome {username} \nUsing this {profile.code} to activate your Account",
                "pythondevloper33@gmail.com",
                [email],
                fail_silently=False,
            )
            

            return redirect(f'/accounts/activate/{username}')
    else:
        form = SignupForm()
    
    return render(request , 'accounts/signup.html',{'form':form })


def user_activate(request,username):
    '''
        activate code
        redirect to login

    '''
    profile = Profile.objects.get(user__username = username)
    if request.method =='POST':
        form = ActivateUserForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if profile.code ==code :
                profile.code = ''
                user = User.objects.get(username = username)
                user.is_active = True

                user.save()
                profile.save()
                return redirect('/accounts/login')
            else:
                messages.error(request, 'Invalid activation code.')

    else:
        form = ActivateUserForm()
    
    return render(request , 'accounts/activate.html',{'form':form,'username':username})

def resend_activation_code(request, username):
    if request.method == 'POST':
        try:
            user = get_object_or_404(User , username = username)
            profile = get_object_or_404(Profile, user=user)
            
            send_mail(
                "Activate Your email",
                f"Welcome {username} \nUsing this {profile.code} to activate your Account",
                "pythondevloper33@gmail.com",
                [user.email],
                fail_silently=False,
            )
            
            messages.success(request, 'Activation code has been resent to your email.')
            return redirect('user_activate', username=username)
        
        except Profile.DoesNotExist:
            messages.error(request, 'User not found.')
        return redirect('user_activate', username=username)  # Redirect back to the activation page
    return redirect('user_activate', username=username)


def dashboard(request):
    product = Product.objects.all().count()
    brand = Brand.objects.all().count()
    review = Review.objects.all().count
    return render(request , 'accounts/dashboard.html',{
        'product':product,
        'brand':brand,
        'review':review,
    })