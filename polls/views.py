from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Poll
from time import timezone
from datetime import date



# Create your views here.
def index(request):
    myTemplate = get_template('./index.html')
    print(myTemplate)
    return render(request, myTemplate)

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

# CRUD
def create(request):
    newPoll = Poll(question="What's up?", pub_date= date.today())
    newPoll.save()
    return HttpResponse("You're creating a new poll with id %s."  % newPoll.id)

def update(request, id):
    response = HttpResponse("You must send data using POST")
    if request.method == 'POST':
        response = HttpResponse("You're updating poll %s." % id)
        myPoll = Poll.objects.get(id=id)
        myPoll.question = request.POST['question']
        myPoll.save()
    return response

def delete(request, id):
    myPoll = Poll.objects.get(id=id)
    myPoll.delete()
    return HttpResponse("You're deleting poll %s." % id)

def read(request, id):
    myPoll = Poll.objects.get(id=id)
    return HttpResponse("You're reading a poll. %s " % myPoll)


#### SECURITY PENDING TOPICS
# Toda conexion con el back deberia tener un token.
# Todo API/CRUD tiene que tener un limite de queries...