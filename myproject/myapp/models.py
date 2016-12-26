# -*- coding: utf-8 -*-
from django.db import models
import exifread
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField


class UserProfile(models.Model):
    user = AutoOneToOneField('auth.user')
    follows = models.ManyToManyField('UserProfile', related_name='followed_by')

    def __unicode__(self):
        return self.user.username

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    modelo = models.TextField()
    apertura = models.TextField()
    dfocal = models.TextField()
    edsoft = models.TextField()
    tiempexp = models.TextField()
    iso = models.TextField()
    fotografo = models.ForeignKey('auth.User')

    def setFotografo(self , autor):
        self.fotografo = autor
    
    def makeinfo(self):


        f = open('/home/VMartini/LumenCap/myproject/' + self.docfile.url, 'rb')
        tags = exifread.process_file(f)
        a = []
        modelo = 'Desconocido'
        edsoft = 'Desconocido'
        print(tags.keys())
        for tag in tags.keys():
            if tag == 'Image Model':
                self.modelo = tags[tag]
                print(self.modelo)
                
            if tag == 'Image Software':
                
                self.edsoft = tags[tag]              


            if tag == 'EXIF FNumber':
                
                self.apertura = tags[tag]    
                    
            if tag == 'EXIF FocalLength':
                
                self.dfocal = tags[tag]    
                print(self.dfocal)
            if tag == 'EXIF ExposureTime':
                
                self.tiempexp = tags[tag]    
                print(self.dfocal)

            if tag == 'EXIF ISOSpeedRatings':
                
                self.iso = tags[tag]    
                print(self.iso)

class Comment(models.Model):

    foto = models.TextField()
    autor = models.ForeignKey('auth.User')
    date = models.DateTimeField()
    text = models.TextField(blank = True)
    
