from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Snippet
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
import ast


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
        user = request.user
        title  = request.POST.get('title')
        description = request.POST.get('description')
        snippet = request.POST.get('snippet')
        language = request.POST.get('language')
        Snippet.objects.create(user=user, title=title, description=description, snippet=snippet, snippet_language=language)
        return HttpResponseRedirect(reverse('home'))

    return render(request, 'app/pages/add.html')


@login_required
def profile(request):
    user = request.user
    snippets = Snippet.objects.filter(user=request.user)
    context = {
        'user':user,
        'snippets':snippets,
    }
    return render(request, 'app/pages/profile.html', context)



def get_snippets_data(request):
    snippets = Snippet.objects.all()
    snippet_data = []
    
    for s in snippets:
        body = ast.literal_eval(s.snippet_body)
        snippet = json.dumps(body)
        data = {
            'body':snippet,
            'description':s.description,
            'language':s.snippet_language
        }
        snippet_data.append(data)
    
    response = {

        'data':snippet_data,
    }
    return JsonResponse(response)


