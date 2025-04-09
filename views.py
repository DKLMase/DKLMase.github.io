from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from .forms import WellnessCheckForm, DailyTaskForm, TutorialScheduleForm, ClassScheduleForm, RegisterForm
from .models import WellnessCheck, DailyTask, TutorialSchedule, ClassSchedule
from django.shortcuts import redirect


# Home view (landing page)
def home(request):
    return render(request, 'home.html')


# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_management')  # Redirect to task_management after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Register view
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')


# Task management view (requires login)
@login_required




def task_management(request):
    if request.method == 'POST':
        if 'create_task' in request.POST:
            task_form = DailyTaskForm(request.POST)
            if task_form.is_valid():
                task = task_form.save(commit=False)
                task.user = request.user  # Link task to current user
                task.save()
                messages.success(request, 'Task successfully added.')
            else:
                messages.error(request, 'There was an error adding the task.')
        
        elif 'create_tutorial' in request.POST:
            tutorial_form = TutorialScheduleForm(request.POST)
            if tutorial_form.is_valid():
                tutorial = tutorial_form.save(commit=False)
                tutorial.user = request.user  # Link tutorial to current user
                tutorial.save()
                messages.success(request, 'Tutorial schedule successfully added.')
            else:
                messages.error(request, 'There was an error adding the tutorial.')
        
        elif 'create_class' in request.POST:
            class_form = ClassScheduleForm(request.POST)
            if class_form.is_valid():
                class_instance = class_form.save(commit=False)
                class_instance.user = request.user  # Link class to current user
                class_instance.save()
                messages.success(request, 'Class schedule successfully added.')
            else:
                messages.error(request, 'There was an error adding the class.')

        return redirect('task_management')  # Redirect to avoid resubmission of form data

    task_form = DailyTaskForm()
    tutorial_form = TutorialScheduleForm()
    class_form = ClassScheduleForm()

    context = {
        'task_form': task_form,
        'tutorial_form': tutorial_form,
        'class_form': class_form,
    }

    return render(request, 'task_management.html', context)




# Custom password reset view (no email needed — console backend)
class CustomPasswordResetRequestView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('password_reset_done')


# Dashboard view
@login_required
def dashboard(request):
    # Fetching tasks, tutorials, and class schedules for the logged-in user
    daily_tasks = DailyTask.objects.filter(user=request.user)
    class_schedule = ClassSchedule.objects.filter(user=request.user)
    tutorial_schedule = TutorialSchedule.objects.filter(user=request.user)

    # Pass the fetched data to the template
    context = {
        'daily_tasks': daily_tasks,
        'class_schedule': class_schedule,
        'tutorial_schedule': tutorial_schedule,
    }

    return render(request, 'dashboard.html', context)


# View schedules
@login_required
def view_schedules(request):
    # Fetching schedules for the logged-in user
    daily_tasks = DailyTask.objects.filter(user=request.user)
    class_schedule = ClassSchedule.objects.filter(user=request.user)
    tutorial_schedule = TutorialSchedule.objects.filter(user=request.user)

    context = {
        'daily_tasks': daily_tasks,
        'class_schedule': class_schedule,
        'tutorial_schedule': tutorial_schedule,
    }

    return render(request, 'view_schedules.html', context)


# Wellness check view (handles both displaying form and saving data)
@login_required
def wellness_check(request):
    suggestion = None  # Initialize the suggestion as None

    if request.method == "POST":
        form = WellnessCheckForm(request.POST)
        if form.is_valid():
            wellness_check = form.save(commit=False)
            wellness_check.user = request.user  # Link the wellness check to the current user
            wellness_check.save()

            # Check the tiredness level and suggest a break if very tired
            if wellness_check.tiredness_level == 'Very tired':
                suggestion = "You seem very tired. How about taking a 15-minute break to recharge?"

            # Render the result page with the wellness check and suggestion
            return render(request, 'wellness_check_result.html', {
                'wellness_check': wellness_check,
                'suggestion': suggestion,
            })
    else:
        form = WellnessCheckForm()

    # If the request method is GET, render the wellness check form
    return render(request, 'wellness_check.html', {'form': form})


# Wellness check result view (Displays the latest wellness check result)
@login_required
def wellness_check_result(request):
    wellness_check = WellnessCheck.objects.filter(user=request.user).order_by('-date').first()

    # If no wellness check exists, display a message or redirect
    if not wellness_check:
        return render(request, 'wellness_check_result.html', {
            'message': "You have not completed a wellness check yet."
        })

    suggestion = None
    if wellness_check.tiredness_level == 'Very tired':
        suggestion = "You seem very tired. How about taking a 15-minute break to recharge?"

    return render(request, 'wellness_check_result.html', {
        'wellness_check': wellness_check,
        'suggestion': suggestion,
    })



def view_schedules(request):
    tasks = DailyTask.objects.all()
    class_schedule = ClassSchedule.objects.all()
    tutorial_schedule = TutorialSchedule.objects.all()

    return render(request, 'view_schedules.html', {
        'tasks': tasks,
        'class_schedule': class_schedule,
        'tutorial_schedule': tutorial_schedule,
    })


def view_schedules(request):
    return render(request, 'view_schedule.html')

def view_schedules(request):
    print("Rendering view_schedules.html")  # Add this for debugging
    return render(request, 'view_schedule.html')

