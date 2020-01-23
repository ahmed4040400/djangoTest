import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from . import models


v= models.Post.objects.order_by('date')



def home(req):

    response = {}

    for i in v :
        response[i.title] = {
        "title": i.title,
        "date&time":i.dateFormate(),
        "image":i.image.url,
        "body":i.bodyThumpnail(),
        }
    return JsonResponse(response)


def post_info(req,post_id):
    #get_object_or_404()is simple method
    #that we uses instade of db.objects.get()
    #that method tries to get the an specific object from the db
    #if it didn't it return an 404 status code
    db  = get_object_or_404(models.Post,pk=post_id)
    return JsonResponse({
            "title": db.title,
            "date&time":db.dateFormate(),
            "image":db.image.url,
            "body":db.body,
        })
