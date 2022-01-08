from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Snippet
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'app/pages/about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, "Congratulations !!! New Account created successfully :)")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserRegisterForm()
    return render(request, 'app/pages/register.html', {'form': form})



@login_required
def add_snippet(request):
    if request.method=="POST":
        title  = request.POST.get('title')
        description = request.POST.get('description')
        snippet = request.POST.get('snippet')
        Snippet.objects.create(title=title, description=description, snippet=snippet)
        return HttpResponseRedirect(reverse('profile'))
    return render(request, 'app/pages/add.html')


@login_required
def profile(request):
    return render(request, 'app/pages/profile.html')


def get_snippets_data(request):
    snippets = Snippet.objects.all()
    snippet_data = []
    
    for s in snippets:
        data = {
            'body':s.snippet_body,
            'description':s.description,
            'language':s.snippet_language
        }
        snippet_data.append(data)
    
    response = {

        'data':snippet_data,
    }
    return JsonResponse(response)
