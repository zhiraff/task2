from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import MyFiles

def task1(request):
    #если данные пришли постом
    if request.method == 'POST':
        # забираем данные из тела запроса
        mydata = request.POST
        url_to_file = ''
        # есть ли в теле запроса есть нужные нам данные
        if 'name' in mydata and 'data' in mydata:
            #создаем файл
            new_file = open(mydata['name'], 'w+')
            new_file.write(mydata['data'])
            new_file.close()
            # копируем файл в google drive

        else:
        #    return HttpResponse('<h2>Name and data required!</h2>')
            return JsonResponse({'status': 'error', 'message': 'Name and data required!'})
        #return HttpResponse('<h2>File created!</h2>')
        return JsonResponse({'status': 'success', 'message': f"file created {url_to_file}"})
    else:
    # если данные пришли не постом
        #return HttpResponse('<h2>Sorry! <br> Only POST method allowed!</h2>')
        new_file = MyFiles(file_name='test.txt', file_data='test data')
        print(new_file)
        new_file.save()
        print(new_file)
        return JsonResponse({'status': 'error', 'message': 'Sorry! Only Post method allowed!'})
