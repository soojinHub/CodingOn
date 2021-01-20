from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members
# Create your views here.
def index(request):
    return HttpResponse("hello")

def test(request):
    return HttpResponse("<h2> Test </h2>")

def git(request):
    return HttpResponse("<h2>git version</h2>")

def signup(request):
    if request.method=='POST':
       username = request.POST['username']
       email = request.POST['email']

      # if username == 'exit':
      #    return HttpResponse("<h2>"+나가기+"</h2>")
      # elif username == 'soojin':
      #     return render(request, 'adminUser.html')
       member = Members(
            username = username,
            useremail = email
       )
       member.save()

       res_data = {}
       res_data['res'] = '등록성공'

       return render(request, 'index.html', res_data)
    return render(request, 'index.html')

def schedule(request):
    return render(request, 'schedule.html')
