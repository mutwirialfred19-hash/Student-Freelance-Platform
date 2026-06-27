from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Category
from .forms import ProjectForm
from proposals.models import Proposal
from proposals.forms import ProposalForm

def project_list(request):
    projects = Project.objects.filter(status='open', is_approved=True)
    categories = Category.objects.all()
    cat_slug = request.GET.get('category')
    search = request.GET.get('q', '')
    if cat_slug:
        projects = projects.filter(category__slug=cat_slug)
    if search:
        projects = projects.filter(title__icontains=search) | projects.filter(description__icontains=search)
    return render(request, 'projects/list.html', {'projects': projects, 'categories': categories, 'search': search, 'cat_slug': cat_slug})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.views += 1
    project.save(update_fields=['views'])
    user_proposal = None
    proposal_form = None
    if request.user.is_authenticated and request.user.role == 'student':
        user_proposal = Proposal.objects.filter(project=project, student=request.user).first()
        if not user_proposal:
            proposal_form = ProposalForm()
    if request.method == 'POST' and request.user.is_authenticated and request.user.role == 'student':
        form = ProposalForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.project = project
            p.student = request.user
            p.save()
            messages.success(request, "Proposal submitted successfully!")
            return redirect('project_detail', pk=pk)
        else:
            proposal_form = form
    proposals = project.proposals.all() if request.user == project.client else None
    return render(request, 'projects/detail.html', {
        'project': project, 'proposal_form': proposal_form,
        'user_proposal': user_proposal, 'proposals': proposals,
    })

@login_required
def post_project(request):
    if request.user.role != 'client':
        messages.error(request, "Only clients can post projects.")
        return redirect('projects')
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = request.user
            project.save()
            messages.success(request, "Project posted successfully!")
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'projects/post.html', {'form': form})
