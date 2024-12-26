from django.shortcuts import redirect, render
from .models import Communitie
from . import forms
from django.contrib.auth.decorators import login_required

def communities_list(request):
    communities = Communitie.objects.all().order_by('date')
    return render(request, 'communities/communities_list.html',{'communities':communities})

def communitie_page(request, slug):
    communitie = Communitie.objects.get(slug=slug)
    return render(request, 'communities/communitie_page.html', {'communitie': communitie})

@login_required(login_url="/users/login/")
def communities_new(request):
    if request.method == 'POST': 
        form = forms.CreateCommunitie(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.save()
            return redirect('communities:list')
    else:
        form = forms.CreateCommunitie()
    return render(request, 'communities/communitie_new.html', { 'form': form })