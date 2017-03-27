from rest_framework import serializers
from uploadtocloud.models import Uploadtoimage
import random
from random import randint
import json
import time


import cloudinary
import cloudinary.uploader
import cloudinary.api


cloudinary.config( 
  cloud_name = "mdsrk",
  api_key = "135644475722638",
  api_secret = "pLoACHW0Yrak1XWyam6TSw-omMw"
)
class UploadtoimageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Uploadtoimage
        fields = ('pk','c_type','photo','img_name','img_type','link')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        import sys
       # link=[]
        # image="image"+str(random.randint(100, 999))
        public_id='id'+str(random.randint(100000, 999999))

        

        if(bool(validated_data.get('photo')) == True):
         cloudinary.uploader.upload(validated_data.get('photo'),public_id ="testimage/"+public_id)

        if(bool(validated_data.get('photo')) == True):
         link=public_id+".jpg"

        objects=Uploadtoimage.objects.create(c_type=validated_data.get('c_type'),photo=link,link=link,img_name=validated_data.get('img_name'),img_type=validated_data.get('img_type'))

        return objects


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.c_type = validated_data.get('c_type', instance.c_type)
        instance.image_name = validated_data.get('image_name', instance.image_name)
        instance.link = validated_data.get('link',instance.link)
        instance.save()
        return instance


