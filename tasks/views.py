from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q
from .models import Project, Task, Comment, TimeLog
from .forms import ProjectForm, TaskForm, CommentForm, TimeLogForm

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

def is_manager(user):
    return user.is_authenticated and (user.role == 'manager' or user.role == 'admin')

@login_required
def dashboard(request):
    user = request.user
    
    if hasattr(user, 'is_admin') and user.is_admin():
        projects = Project.objects.all()
        tasks = Task.objects.all()
    elif hasattr(user, 'is_manager') and user.is_manager():
        projects = Project.objects.filter(
            Q(manager=user) | Q(team_members=user)
        ).distinct()
        tasks = Task.objects.filter(
            Q(project__in=projects) | Q(assigned_to=user)
        ).distinct()
    else:
        projects = Project.objects.filter(team_members=user)
        tasks = Task.objects.filter(assigned_to=user)
    
    # Statistiques
    total_projects = projects.count()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='done').count()
    overdue_tasks = tasks.filter(status__in=['todo', 'in_progress']).count()
    
    context = {
        'projects': projects[:5],
        'tasks': tasks[:10],
        'total_projects': total_projects,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'overdue_tasks': overdue_tasks,
    }
    
    return render(request, 'tasks/dashboard.html', context)

@login_required
def project_list(request):
    user = request.user
    
    if hasattr(user, 'is_admin') and user.is_admin():
        projects = Project.objects.all()
    elif hasattr(user, 'is_manager') and user.is_manager():
        projects = Project.objects.filter(
            Q(manager=user) | Q(team_members=user)
        ).distinct()
    else:
        projects = Project.objects.filter(team_members=user)
    
    return render(request, 'tasks/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    # Vérifier les permissions
    if not request.user.is_admin() and request.user not in project.team_members.all() and request.user != project.manager:
        messages.error(request, "Vous n'avez pas accès à ce projet.")
        return redirect('project_list')
    
    tasks = project.tasks.all()
    
    # Initialiser le formulaire
    form = TaskForm(initial={'project': project})
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            messages.success(request, 'Tâche créée avec succès!')
            return redirect('project_detail', pk=project.pk)
    
    context = {
        'project': project,
        'tasks': tasks,
        'form': form,
    }
    
    return render(request, 'tasks/project_detail.html', context)

@login_required
@user_passes_test(is_manager)
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.manager = request.user
            project.save()
            form.save_m2m()  # Pour sauvegarder les relations ManyToMany
            messages.success(request, 'Projet créé avec succès!')
            return redirect('project_list')
    else:
        form = ProjectForm()
    
    return render(request, 'tasks/project_form.html', {'form': form, 'title': 'Créer un projet'})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    # Vérifier les permissions
    if not request.user.is_admin() and request.user != task.assigned_to and request.user != task.project.manager and request.user not in task.project.team_members.all():
        messages.error(request, "Vous n'avez pas accès à cette tâche.")
        return redirect('dashboard')
    
    comments = task.comments.all()
    time_logs = task.time_logs.all()
    
    # Initialiser les formulaires (TOUJOURS les définir)
    comment_form = CommentForm()
    time_form = TimeLogForm()
    
    if request.method == 'POST':
        if 'comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.task = task
                comment.author = request.user
                comment.save()
                messages.success(request, 'Commentaire ajouté!')
                return redirect('task_detail', pk=task.pk)
        elif 'time_log' in request.POST:
            time_form = TimeLogForm(request.POST)
            if time_form.is_valid():
                time_log = time_form.save(commit=False)
                time_log.task = task
                time_log.user = request.user
                time_log.save()
                messages.success(request, 'Temps enregistré!')
                return redirect('task_detail', pk=task.pk)
    
    context = {
        'task': task,
        'comments': comments,
        'time_logs': time_logs,
        'comment_form': comment_form,
        'time_form': time_form,
    }
    
    return render(request, 'tasks/task_detail.html', context)

@login_required
def my_tasks(request):
    tasks = Task.objects.filter(assigned_to=request.user).order_by('-due_date')
    return render(request, 'tasks/my_tasks.html', {'tasks': tasks})