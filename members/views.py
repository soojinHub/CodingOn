from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Members
# Create your views here.

def login_after(request):
    return HttpResponse("세션읽기 & 세션 없으면 리다이렉션")

def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username=request.POST.get('username',None)
        useremail=request.POST.get('useremail', None)

        err = {}
        if not (username and useremail):
            err['err'] = '아이디와 이메일을 모두 입력해주세요.'
            return render(request, 'login.html', err)
        else:
            member = Members.objects.get(username=username)
            if username == member.username:
                request.session['user']=member.id
                return redirect('/members')
            else:
                err['err'] = '아이디 또는 이메일이 잘못되었습니다'
                return render(request, 'login.html', err)
            return HttpResponse(f"<h1>{member.username}</h1>")


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
