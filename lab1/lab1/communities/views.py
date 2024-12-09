from django.shortcuts import render
from .models import Communitie

def communities_list(request):
    communities = Communitie.objects.all().order_by('date')
    return render(request, 'communities/communities_list.html',{'communities':communities})

def communitie_page(request, slug):
    communitie = Communitie.objects.get(slug=slug)
    return render(request, 'communities/communitie_page.html', {'communitie': communitie})
