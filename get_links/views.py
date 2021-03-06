from rest_framework import generics
from uploadtocloud.models import Uploadtoimage
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

class StatusCode(object):
    OK = 200
    NOT_FOUND = 404
    
import json
from django.http import HttpResponse
 
def JSONResponse(data = None, status = StatusCode.OK):
    if data is None:
        return HttpResponse(status)
    if data and type(data) is dict:
        return HttpResponse(json.dumps(data, indent = 4, encoding = 'utf-8', sort_keys = True), \
            mimetype = 'application/json', status = status)
    else:
        return HttpResponse(status = StatusCode.NOT_FOUND)

def get_queryset(request, format=None):

  from django.http import JsonResponse

  import sys
  

  details=[]

  objects=Uploadtoimage.objects.all()

  for obj in objects:
   print sys.stderr,obj.link

   if(obj.link != ""):
    if(Uploadtoimage.objects.filter(link=obj.link).exists()):
     image_details=Uploadtoimage.objects.get(link=obj.link)
     image_link='http://res.cloudinary.com/mdsrk/image/upload/v1490081508/testimage/'+image_details.link
    else:
     image_link=""
   else:
    image_link=''
  
   # # if(obj.pk != ""):
   # if(Uploadtoimage.objects.filter(link=obj.link).exists()):
   #  image_details=Uploadtoimage.objects.get(link=obj.link)
   #  image_link='http://res.cloudinary.com/mdsrk/image/upload/v1490081508/testimage/'+image_details.link
   # else:
    #image_link=""
   # else:
   #  image_link=''
  
   details.append({
              'Categories':Uploadtoimage.objects.filter(link=obj.link).values('pk','c_type')[0],
              'image_link' : image_link
          })


  from django.http import JsonResponse
  return JsonResponse(details,safe=False)


