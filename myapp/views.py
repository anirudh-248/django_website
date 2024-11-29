from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Feature, Service, Portfolio, Team, Review, Faq, UserForm, SpForm, UserProfile, Contact
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    features = Feature.objects.all()
    services = Service.objects.distinct('service_name')
    portfolios = Portfolio.objects.all()
    team = Team.objects.all()
    reviews = Review.objects.all()
    faqs = Faq.objects.all()
    return render(request, 'index.html', {
        'features': features,
        'services': services,
        'portfolios': portfolios,
        'team': team,
        'reviews': reviews,
        'faqs': faqs,
    })

def register(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        phno = request.POST['phno']
        utype = request.POST['utype']
        password = request.POST['password']
        password_r = request.POST['password_r']
        if password==password_r:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken.')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=username,
                    email=email,
                    password=password
                )
                UserProfile.objects.create(
                    user=user,
                    phone_number=phno,
                    user_type=utype
                )
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid login credentials.')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def customer(request):
    # Get distinct service names and corresponding provider names
    services_by_name = Service.objects.values('service_name').annotate(
        providers=Count('provider_name')
    )
    
    services = Service.objects.order_by('service_name', 'provider_name')
    
    return render(request, 'customer.html', {
        'services_by_name': services_by_name,
        'services': services
    })

def customer_services(request, name):
    services = Service.objects.all()
    services_d = Service.objects.distinct('service_name')
    
    # Initialize filters
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    # Filter by price range
    if min_price:
        services = services.filter(service_cost__gte=min_price)
    if max_price:
        services = services.filter(service_cost__lte=max_price)

    return render(request, 'customer-services.html', {'services': services, 'services_d': services_d, 'name': name})

@login_required
def service_provider(request):
    
    if request.method == 'POST':
        # Get form data
        service_name = request.POST.get('service_name')
        provider_name = request.user.username
        details = request.POST.get('details')
        service_cost = request.POST.get('service_cost')
        banner = request.FILES.get('banner')

        # Create a new service instance
        new_service = Service(
            service_name=service_name,
            provider_name=provider_name,
            details=details,
            service_cost=service_cost,
            banner=banner,
        )

        # Save the service to the database
        new_service.save()

        # Redirect to the service provider page after saving
        return redirect('service-provider')

    services = Service.objects.distinct('service_name')
    services_filtered = Service.objects.filter(provider_name=request.user.username)
    return render(request, 'service-provider.html', {'services': services, 'services_f': services_filtered})

def delete_service(request,service_id): 
    service = get_object_or_404(Service, id=service_id)
    if request.method=='POST':
        service.delete() 
        previous_page = request.META.get('HTTP_REFERER')
        if previous_page:
            return redirect(previous_page)
        else:
            return redirect('default-view')
    return redirect('/service-provider')

def sp_services(request, name):
    services = Service.objects.all()
    services_d = Service.objects.distinct('service_name')
    return render(request, 'sp-services.html', {'services': services, 'services_d': services_d, 'name': name})

def services(request):
    services = Service.objects.distinct('service_name')
    return render(request, 'services.html', {'services': services})

def service_details(request, name):
    services = Service.objects.all()
    services_d = Service.objects.distinct('service_name')
    return render(request, 'service_details.html', {'services': services, 'services_d': services_d, 'name': name})

def portfolio_details(request):
    services = Service.objects.distinct('service_name')
    return render(request, 'portfolio-details.html', {'services': services})

def user_form(request):
    if request.method=='POST':
        wed_date = request.POST['wed_date']
        city = request.POST['city']
        services = request.POST.getlist('services')
        event_mgr = request.POST['event_mgr']
        budget = request.POST['budget']
        uf = UserForm.objects.create(
            wed_date=wed_date,
            city=city,
            services=', '.join(services),
            event_mgr=event_mgr,
            budget=budget
            )
        messages.success(request, 'Data has been submitted')
    return render(request, 'user-form.html')

def sp_form(request):
    if request.method=='POST':
        cname = request.POST['name']
        stype = request.POST['stype']
        desc = request.POST['desc']
        cost = request.POST['cost']
        sf = SpForm.objects.create(name=cname, stype=stype, desc=desc, cost=cost)
        messages.success(request, 'Data has been submitted')
    return render(request, 'sp-form.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        co = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Data has been submitted')
    return render(request, 'contact.html')

def aboutus(request):
    services = Service.objects.distinct('service_name')
    return render(request, 'aboutus.html', {'services': services})

def feedback(request):
    return render(request, 'feedback.html')