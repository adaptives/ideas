from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import _get_queryset
from ideas.ideasm import models
import logging

logger = logging.getLogger(__name__)

def home(request):
    ideas = models.Idea.objects.all()
    ga = models.KVPairs.objects.get(k='ga')
    ctx = {'ideas': ideas, 'ga': ga.v}
    return render_to_response('home.html', ctx)

def idea(request, idea_id, slug):
    idea = models.Idea.objects.get(id=idea_id)

    try:
        ga = models.KVPairs.objects.get(k='ga')
    except BaseException:
        logger.error('Could not find value for ga... using default')
        ga = ''
    
    try:
        ce = models.KVPairs.objects.get(k='ce')
    except BaseException:
        logger.error('Could not find value for ce... using default')
        ce = ''
    
    ctx = {'idea': idea, 'ga': ga, 'ce': ce.v}
    return render_to_response('idea.html', ctx)


