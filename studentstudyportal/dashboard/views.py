from datetime import datetime
from cgitb import text
from doctest import Example
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import *
from django.views import generic
from youtubesearchpython import VideosSearch
import requests
import wikipedia
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import StepForm
from .models import Step
###@login_required
def home(request):
    if request.session.has_key('user_email'):

        return render(request,'dashboard/home.html')
    else:
        template = 'dashboard/logout.html'
        lf = LoginForm()
        context = {
            'form' : lf,
            'msg_error' : 'please login first'
            }
        return render(request,template,context)
def home1(request):
    if request.session.has_key('user_email'):

        return render(request,'dashboard/home1.html')
    else:
        template = 'dashboard/logout.html'
        lf = LoginForm()
        context = {
            'form' : lf,
            'msg_error' : 'please login first'
            }
        return render(request,template,context)

def front(request):
    return render(request,'dashboard/front.html')
def about(request):
    return render(request,'dashboard/about.html')
def service(request):
    return render(request,'dashboard/services.html')
###@login_required
def notes(request):
    if request.session.has_key('user_email'):

        if request.method == "POST":
            form = NotesForm(request.POST)
            if form.is_valid():
                notes = Notes(
                title=request.POST['title'],
                description =request.POST['description'],
                )
                notes.save()
            messages.success(request,f"Notes Added from  Successfully!")
        else:
            form = NotesForm()
        notes = Notes.objects.filter()
        context ={
            
            'notes': notes,
            'form':form
            }
        return render(request,'dashboard/notes.html',context)
    else:
        template = 'dashboard/logout.html'
        
        return render(request,template)

###@login_required
def delete_note(request,pk=None):
    if request.session.has_key('user_email'):
        Notes.objects.get(id=pk).delete()
        return redirect("notes")

class NotesDetailView(generic.DetailView):
    model = Notes


def homework(request):
    if request.session.has_key('user_email'):
        if request.method =="POST":
            form = HomeworkForm(request.POST)
            if form.is_valid():
                try:
                    finished = request.POST['is_finished']
                    if finished == 'on':
                        finished = True
                    else:
                        finished = False
                except:
                    finished = False
                homeworks = Homework(
                    
                    
                    title = request.POST['title'],
                    description = request.POST['description'],
                    
                    is_finished = finished,
                )
                homeworks.save()   
        else:
            form = HomeworkForm()
        homework = Homework.objects.filter()
        if len(homework) == 0:
            homework_done = True
        else:
            homework_done = False
        

        context = {
            'homeworks':homework,
            'homeworks_done':homework_done,
            'form':form
        }
        return render(request,'dashboard/homework.html',context)
    else:

        template = 'dashboard/logout.html'
        
        return render(request,template)

def update_homework(request,pk=None):
    homework =Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')

def delete_homework(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')



def youtube(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text,limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input' : text,
                'title' :i['title'],
                'duration' :i['duration'],
                'thumbnail' :i['thumbnails'][0]['url'],
                'channel' :i['channel']['name'],
                'link' :i['link'],
                'views' :i['viewCount']['short'],
                'published' :i['publishedTime'],

            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc +=j['text']
                result_dict['description'] = desc
                result_list.append(result_dict)
                context={
                    'form': form,
                    'results' : result_list,
                }
                return render(request,'dashboard/youtube.html',context)

    else:
        form = DashboardForm()
    context = { 'form':form}
    return render(request,'dashboard/youtube.html',context)
###@login_required
def todo(request):
    if request.session.has_key('user_email'):
        if request.method == "POST":
            form = TodoForm(request.POST)
            if form.is_valid():
                try:
                    finished = request.POST['is_finished']
                    if finished == 'on':
                        finished = True
                    else:
                        finished = False
                except:
                    finished = False
                todos = Todo(user=request.user,
                title=request.POST['title'],
                is_finished = finished

                )
                todos.save()
                messages.success(request,f'Todo Added From {request.user.username}!!')
        
        else:
            form = TodoForm()
        todo = Todo.objects.filter(user=request.user)
        if len(todo) == 0:
            todos_done == True
        else:
            todos_done = False
        
        context = {
            'form':form,
            'todos':todo,
            'todos_done':todos_done


        }
        return render (request,'dashboard/todo.html',context)
    else:
        template = 'dashboard/user_login.html'
        lf = LoginForm()
        context = {
            'form' : lf,
            'msg_error' : 'please login first'
            }
        return render(request,template,context)
##@login_required
def update_todo(request,pk=None):
    todo =Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todo')
@login_required
def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')

def books(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        
        answer = r.json()
        result_list = []
        for i in range(10):
            result_dict = {
                'title' :answer['items'][i]['volumeInfo']['title'],
                'subtitle' :answer['items'][i]['volumeInfo'].get('subtitle'),
                'description' :answer['items'][i]['volumeInfo'].get('description'),
                'count' :answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories' :answer['items'][i]['volumeInfo'].get('categories'),
                'rating' :answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail' :answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview' :answer['items'][i]['volumeInfo'].get('previewLink'),
            }
            
            result_list.append(result_dict)
            context={
                'form': form,
                'results' : result_list,
                }
        return render(request,'dashboard/books.html',context)

    else:
        form = DashboardForm()
    context = { 'form':form}
    return render(request,'dashboard/books.html',context)
@login_required
def step(request):
    
    return render(request,'dashboard/step.html')


@login_required
def wiki(request):
    if request.method =='POST':
        text = request.POST['text']
        form = DashboardForm(request.POST)
        search = wikipedia.page(text)
        context = {
            'form':form,
            'title':search.title,
            'link':search.url,
            'details':search.summary
        }
        return render(request,'dashboard/wiki.html',context)
    else:
        form = DashboardForm()
        context = {
            'form':form,
        }
    return render(request,'dashboard/wiki.html',context)
#@login_required
def Conversion(request):
    if request.session.has_key('user_email'):
        if request.method == "POST":
            form = ConversionForm(request.POST)
            
            if request.POST['measurement'] =='mass':
                measurement_form = ConversionMassForm()
                context = {
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
                if 'input' in request.POST:
                    first = request.POST['measure1']
                    second = request.POST['measure2']
                    input = request.POST['input']
                    answer = ''
                    if input and int(input) >= 0:
                        if first == 'pound' and second == 'kilogram':
                            answer = f'{input} pound = {int(input)*0.453592} kilogram'
                        if first == 'kilogram' and second == 'pound':
                            answer = f'{input} kilogram = {int(input)/2.20462} pound'
                    context = {

                    'form':form,
                    'm_form':measurement_form,
                    'input':True,
                    'answer':answer
                }

        else:
            form = ConversionForm()
            context = {
                'form':form,
                'input':False
            }
        return render(request,'dashboard/conversion.html',context)
    else:
        template = 'dashboard/logout.html'
        
        return render(request,template)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created For {username}!!")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/register.html',context)



#@login_required
#def logout(request):
    #del request.session['user_email']

     
    #return render(request,'dashboard/logout.html')





def user_login(request):
    #creating form object
    lf = LoginForm()
    template = 'dashboard/user_login.html'
    
    if request.method == "POST":
        #creating use object
        user = AppUser.objects.get(email=request.POST.get('email'))
        if request.POST.get('password') == user.password:
            request.session['user_email'] = user.email
            if request.session.has_key('user_email'):

                template = "dashboard/home.html"
                
                return render(request,template,)
           
            

        else:
            context = {
                'form' : lf,
                'msg_error' : 'Invalid email or password'
            }
            return render(request,template,context)
    else:

        context = {'form': lf}
        return render(request,template,context)




def logout(request):
    if request.session.has_key('user_email'):

    
        del request.session['user_email']

        
        template = "dashboard/front.html"
        return render(request, template,)
    else:
        template = "dashboard/front.html"
        return render(request, template,)


        
def admin_register(request):
    arf = AdminRegistrationForm
    template = 'dashboard/adminregister.html'
    if request.method == "POST":
        user = AppUser()
        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST.get('last_name')
        user.contact = request.POST.get('contact')
        user.email = request.POST.get('email')
        user.dob = request.POST.get('dob')
        

        #we can also use this process
        user.password1 = request.POST['password1']
        user.address = request.POST.get('address')
        user.created_at = datetime.now()
        #to store data
        user.save()

        context = {
            'form' :  arf,
            'success' : 'Registered Successfully'}

        return render(request,template,context)
    else:
        context = {'form': arf}
        return render(request, template, context)


def user_register(request):
    rf = CreateForm()
    template = 'dashboard/create.html'
    if request.method == "POST":
        user = AppUser()
        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST.get('last_name')
        user.contact = request.POST.get('contact')
        user.email = request.POST.get('email')
        user.dob = request.POST.get('dob')
        

        #we can also use this process
        user.password = request.POST['password']
        user.address = request.POST.get('address')
        user.created_at = datetime.now()
        #to store data
        user.save()

        context = {
            'form' :  rf,
            'success' : 'Registered Successfully'}

        return render(request,template,context)
    else:
        context = {'form': rf}
        return render(request, template, context)

        






def upload(request):
    if request.session.has_key('user_email'):
        context = {}
        if request.method == 'POST':
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)
        return render(request, 'dashboard/upload.html', context)
    else:
        template = 'dashboard/logout.html'
        
        return render(request,template)


def step_list(request):
    if request.session.has_key('user_email'):
        steps = Step.objects.all()
        return render(request, 'dashboard/step_list.html', {
            'steps': steps
        })
    else:
        template = 'dashboard/logout.html'
        
        return render(request,template)


def upload_step(request):
    if request.method == 'POST':
        form = StepForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('step_list')
    else:
        form = StepForm()
    return render(request, 'dashboard/upload_step.html', {
        'form': form
    })


def delete_step(request, pk):
    if request.method == 'POST':
        step = Step.objects.get(pk=pk)
        step.delete()
    return redirect('step_list')


class StepListView(ListView):
    model = Step
    template_name = 'dashboard/class_step_list.html'
    context_object_name = 'steps'


class UploadStepView(CreateView):
    model = Step
    form_class = StepForm
    success_url = reverse_lazy('class_step_list')
    template_name = 'dashboard/upload_step.html'

def step(request):
    if request.session.has_key('user_email'):
        steps = Step.objects.all()
        return render(request, 'dashboard/step.html', {
            'steps': steps
        })
    else:
        template = 'dashboard/logout.html'
        
        return render(request,template)

    
def admin_login(request):
    #creating form object
    af = AdminLoginForm()
    template = 'dashboard/adminlogin.html'
    
    if request.method == "POST":
        #creating use object
        user = AppUser.objects.get(email=request.POST.get('email'))
        if request.POST.get('password1') == user.password1:  
            request.session['user_email'] = user.email
            if request.session.has_key('user_email'):

                template = "dashboard/home1.html"
                
                return render(request,template,)
           
            

        else:
            context = {
                'form' : af,
                'msg_error' : 'Invalid email or password'
            }
            return render(request,template,context)
    else:

        context = {'form': af}
        return render(request,template,context)