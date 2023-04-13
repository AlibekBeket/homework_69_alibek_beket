import json

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Only GET request are allowed {request.method}')


def json_add_number(request, *args, **kwargs):
    response_data = {'detail': 'Нет входных данных'}
    response = JsonResponse(response_data)
    response.status_code = 200
    if request.body:
        number = json.loads(request.body)
        try:
            a = int(number.get('A'))
            b = int(number.get('B'))
            answer = {'answer': a + b}
            response = JsonResponse(answer)
            response.status_code = 201
        except Exception:
            response_data = {'error': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
    return response


def json_subtract_number(request, *args, **kwargs):
    response_data = {'detail': 'Нет входных данных'}
    response = JsonResponse(response_data)
    response.status_code = 200
    if request.body:
        number = json.loads(request.body)
        try:
            a = int(number.get('A'))
            b = int(number.get('B'))
            answer = {'answer': a - b}
            response = JsonResponse(answer)
            response.status_code = 201
        except Exception:
            response_data = {'error': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
    return response


def json_multiply_number(request, *args, **kwargs):
    response_data = {'detail': 'Нет входных данных'}
    response = JsonResponse(response_data)
    response.status_code = 200
    if request.body:
        number = json.loads(request.body)
        try:
            a = int(number.get('A'))
            b = int(number.get('B'))
            answer = {'answer': a * b}
            response = JsonResponse(answer)
            response.status_code = 201
        except Exception:
            response_data = {'error': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
    return response