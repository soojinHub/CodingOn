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

def gugu(request):
    num = request.GET.get('num','')
    return HttpResponse(f"<h1>구구단 : {num}<br>{num_gugu(num)}</h1>")

           

def num_gugu(num):
    str=""
    for i in range (2,10):
        str += f"{num}*{i}={int(num)*i}<br>"
    return str
        


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
