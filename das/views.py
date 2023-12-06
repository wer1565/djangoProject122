from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from das.models import TestModel


def index (request):
    return render(request, 'index.html')

@csrf_exempt
def reg(request):
        sasha = TestModel()
        if request.method == 'POST':
            data = TestModel.objects.all()
            for i in data:
                if request.POST['email'] == i.email: return render(request, 'forma.html', {"err": "Данный Email занят"})
            sasha.email = request.POST['email']
            sasha.password = request.POST['password']
            sasha.save()
            return render(request, 'index.html')
        return render(request, 'forma.html')


@csrf_exempt
def login(request):
    if request.method == 'put':
            Base.metadata.create_all(engine)
            print('Bot started!')
            asyncio.run(main())
            return HttpResponse('Бот запущен!')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data = TestModel.objects.all()
        for i in data:
            if email == i.email:
                if password == i.password:
                    return render(request, 'test.html')
                else:
                    return HttpResponse("Пароль неверный")
        return HttpResponse("Такого пользователя не существует")
    return render(request, 'login.html')
