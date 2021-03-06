from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import _get_queryset
from ideas.ideasm import models
import logging

logger = logging.getLogger(__name__)

def home(request):
    ideas = models.Idea.objects.all()
    try:
        ga = models.KVPairs.objects.get(k='ga')
        ga = ga.v
    except BaseException:
        logger.error('Could not find value for ga... using default')
        ga = ''
    ctx = {'ideas': ideas, 'ga': ga}
    return render_to_response('home.html', ctx)

def idea(request, idea_id, slug):
    idea = models.Idea.objects.get(id=idea_id)

    try:
        ga = models.KVPairs.objects.get(k='ga')
        ga = ga.v
    except BaseException:
        logger.error('Could not find value for ga... using default')
        ga = ''
    
    try:
        ce = models.KVPairsLarge.objects.get(k='ce')
        ce = ce.v
    except BaseException:
        logger.error('Could not find value for ce... using default')
        ce = ''
    
    ctx = {'idea': idea, 'ga': ga, 'ce': ce}
    return render_to_response('idea.html', ctx)


