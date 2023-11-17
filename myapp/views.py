from multiprocessing import context
from django.shortcuts import render
from .models import Skill
# from django.http import HttpResponse


def index(request):
    skill1 = Skill()
    skill1.id = 0
    skill1.name = 'Data Analyst'
    skill1.progress = '80%'

    skill2 = Skill()
    skill2.id = 1
    skill2.name = 'HTML'
    skill2.progress = '100%'

    skill3 = Skill()
    skill3.id = 2
    skill3.name = 'CSS'
    skill3.progress = '90%'

    skill4 = Skill()
    skill4.id = 3
    skill4.name = 'Javascript'
    skill4.progress = '75%'

    skill5 = Skill()
    skill5.id = 4
    skill5.name = 'Python'
    skill5.progress = '80%'
    
    skill6 = Skill()
    skill6.id = 5
    skill6.name = 'QA'
    skill6.progress = '80%'

    return render(request, 'index.html', {'skill1':skill1,'skill2':skill2,'skill3':skill3,'skill4':skill4,'skill5':skill5,'skill6':skill6})

# def index(request):
#     context = {
#         'name': 'Roby Afrizal',
#         'age': 37,
#         'alamat': 'Sekeloa',
#     }
#     return render(request, 'index.html', context)

def counter(request):
    text = request.POST['text']
    jumlahKata = len(text.split())
    jumlahHuruf = len(text)
    return render(request, 'counter.html',{'word':jumlahKata, 'huruf':jumlahHuruf})

# def index(request):
#     name = "Roby Afrizal"
#     return render(request, 'index.html', {'name': name})

# def index(request):
#     return HttpResponse('<h1>Welcome Roby</h1>')
