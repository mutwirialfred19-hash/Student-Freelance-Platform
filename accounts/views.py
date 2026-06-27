from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StudentRegisterForm, ClientRegisterForm
from .models import User
from profiles.models import StudentProfile, ClientProfile
from projects.models import Project, Category
from proposals.models import Proposal
from reviews.models import Review

def home(request):
    categories = Category.objects.all()
    recent_projects = Project.objects.filter(status='open', is_approved=True)[:6]
    student_count = User.objects.filter(role='student').count()
    project_count = Project.objects.count()
    top_students = User.objects.filter(role='student').select_related('student_profile')[:6]
    return render(request, 'core/home.html', {
        'categories': categories,
        'recent_projects': recent_projects,
        'student_count': student_count,
        'project_count': project_count,
        'top_students': top_students,
    })

def register_student(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            StudentProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, f"Welcome {user.first_name}! Complete your profile to start getting hired.")
            return redirect('dashboard')
    else:
        form = StudentRegisterForm()
    return render(request, 'accounts/register_student.html', {'form': form})

def register_client(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            ClientProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, f"Welcome {user.first_name}! Start by posting your first project.")
            return redirect('dashboard')
    else:
        form = ClientRegisterForm()
    return render(request, 'accounts/register_client.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, "Invalid username or password.")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    ctx = {'user': user}
    if user.role == 'student':
        try:
            profile = user.student_profile
        except:
            profile = StudentProfile.objects.create(user=user)
        proposals = Proposal.objects.filter(student=user).select_related('project')[:5]
        ctx.update({'profile': profile, 'proposals': proposals})
    else:
        try:
            profile = user.client_profile
        except:
            profile = ClientProfile.objects.create(user=user)
        projects = Project.objects.filter(client=user).order_by('-created_at')[:5]
        ctx.update({'profile': profile, 'projects': projects})
    return render(request, 'core/dashboard.html', ctx)
