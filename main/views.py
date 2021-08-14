from django.core import serializers
from django.db.models import Q

def status(status, message):
    data = {'status': status, 'message': message}
    return data

def createJsonResponse(data):
    from ast import literal_eval

    datas = literal_eval(serializers.serialize('json', data))
    response = [{}]
    index = 0
    
    for x in datas:
        response[0][x['pk']] = {}
        fields = list(x['fields'].keys())

        for key in fields:
            response[0][x['pk']][key] = x['fields'][key]
        response[0][x['pk']]['author'] = str(data[index].author.username)
        index+=1
    
    return response

def createQuery(request, user=False):
    query = Q()
    if 'id' in request.GET:
        query &= Q(pk=request.GET['id'])

    if 'q' in request.GET:
        words = request.GET['q'].split(" ")

        for word in words:
            query |= Q(description__icontains=word)
            query |= Q(title__icontains=word)
    
    if 'date' in request.GET:
        words = request.GET['date'].split(",")
        query &= Q(created__range=words)
    
    return query