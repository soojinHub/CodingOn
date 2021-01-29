from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("주인공 두 명의 이름을 입력해주세요.")

def my_novel(request, character1, character2):
	context = {"ch_1":character1,"ch_2":character2}
	return render(request, 'novel.html', context)