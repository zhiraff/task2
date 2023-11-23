from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .utils import create_and_upload_file

def task1(request):
    #если данные пришли постом
    if request.method == 'POST':
        # забираем данные из тела запроса
        mydata = request.POST
        url_to_file = ''
        # есть ли в теле запроса есть нужные нам данные
        if 'name' in mydata and 'data' in mydata:
            #создаем файл, копируем файл в google drive
            create_and_upload_file(file_name=mydata['name'], file_content=mydata['data'])

        else:
        #    return HttpResponse('<h2>Name and data required!</h2>')
            return JsonResponse({'status': 'error', 'message': 'Name and data required!'})
        #return HttpResponse('<h2>File created!</h2>')
        return JsonResponse({'status': 'success', 'message': f"file created {url_to_file}"})
    else:
    # если данные пришли не постом
        #return HttpResponse('<h2>Sorry! <br> Only POST method allowed!</h2>')
        create_and_upload_file(file_name='test.txt', file_content='testtest')
        return JsonResponse({'status': 'error', 'message': 'Sorry! Only Post method allowed!'})
