from django.shortcuts import render
from django.http import HttpResponse
from .models import Poll
from time import timezone

# Create your views here.
def index(request):
    return render(request, 'polls/index.html')

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

# CRUD
def create(request):
    newPoll = Poll(question="What's up?", pub_date=timezone.now())
    newPoll.save()
    return HttpResponse("You're creating a new poll with id %s."  % newPoll.id)

def update(request, poll_id):
    response = HttpResponse("You must send data using POST")
    if request.method == 'POST':
        response = HttpResponse("You're updating poll %s." % poll_id)
        myPoll = Poll.objects.get(id=poll_id)
        myPoll.question = request.POST['question']
        myPoll.save()
    return response

def delete(request, poll_id):
    return HttpResponse("You're deleting poll %s." % poll_id)

def read(request):
    return HttpResponse("You're reading a poll.")