from uploadtocloud.models import Uploadtoimage
from uploadtocloud.serializers import UploadtoimageSerializer
from rest_framework import generics
# from category.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class UploadtoimageList(generics.ListCreateAPIView):
 queryset = Uploadtoimage.objects.all()
 serializer_class = UploadtoimageSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class UploadtoimageDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Uploadtoimage.objects.all()
 serializer_class = UploadtoimageSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)

