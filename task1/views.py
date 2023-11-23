from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .utils import create_and_upload_file
import json

def task1(request):
    #если данные пришли постом
    if request.method == 'POST':
        # забираем данные из тела запроса
        formdata = request.POST
        url_to_file = ''
        # есть ли в теле запроса есть нужные нам данные
        if 'name' in formdata and 'data' in formdata:
            #создаем файл, копируем файл в google drive
            create_and_upload_file(file_name=formdata['name'], file_content=formdata['data'])
        else:
            # смотрим в raw
            try:
                db = request.body
                db.decode()
                rawData = json.loads(db)
                if 'name' in rawData and 'data' in rawData:
                    create_and_upload_file(file_name=rawData['name'], file_content=rawData['data'])
                else:
                    return JsonResponse({'status': 'error', 'message': 'Name and data required!'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': 'body error'})
        #return HttpResponse('<h2>File created!</h2>')
        return JsonResponse({'status': 'success', 'message': f"file created {url_to_file}"})
    else:
    # если данные пришли не постом
        #return HttpResponse('<h2>Sorry! <br> Only POST method allowed!</h2>')
        #create_and_upload_file(file_name='test.txt', file_content='testtest')
        return JsonResponse({'status': 'error', 'message': 'Sorry! Only Post method allowed!'})
