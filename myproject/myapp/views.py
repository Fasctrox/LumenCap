# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

import exifread

def list(request , username):
    # Handle file upload
    loggeduser = request.user.username
    editmode = False
    if loggeduser == username:
        editmode = True
    if request.method == 'POST':
        print('Entra1')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print('Entra')
            print(request.user.username)
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.setFotografo(request.user)
            newdoc.save()
            newdoc.makeinfo()
            newdoc.save()
            # Redirect to the document list after POST

            return HttpResponseRedirect('/myapp/list/' + request.user.username)
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    print(request.user.username)
    documents = Document.objects.filter(fotografo = getUserByUrl(username))
    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form, 'loggeduser' : loggeduser ,'editmode' : editmode}
    )
def getUserByUrl(username):

    users = User.objects.all()

    for currentuser in users:

        if currentuser.username == username:
            return currentuser 

def feed(request):
    # Handle file upload
    documents = Document.objects.all()
    loggeduser = request.user.username

    for doc in documents:
        print(doc.fotografo.username)
    # Render list page with the documents and the form
    return render(
        request,
        'feed.html',
        {'documents': documents, 'loggeduser' : loggeduser}
    )   
def list_delete(request,question_id):
    print('question_id ->',question_id)
    Document.objects.get(pk=question_id).delete()
    return HttpResponseRedirect('/myapp/list/' + request.user.username)
def view_image(request,question_id, mode,username):
    close = ''
    image = Document.objects.get(pk = question_id)
    print(question_id)
    if mode == 'list':
        close = '/myapp/list/' + username
    elif mode == 'feed':
        close = '/myapp/feed' 

    nextimg = getIdNext(question_id, mode,username)
    previmg = getIdPrev(question_id, mode, username)

    print(nextimg , previmg)
    return render(
        request,
        'bigpicture.html',
        { 'image' : image, 'previmg' : previmg,'nextimg' : nextimg , 'previmg' : previmg , 'close' : close, 'mode' : mode })  
def getIdNext(n, mode, username):
    documents = ''
    if mode == 'feed':
        documents = Document.objects.all()
    elif mode == 'list':
        documents = Document.objects.filter(fotografo = getUserByUrl(username))
    print('Len' , len(documents))
    for i in range(len(documents)-1):
        
        
        if (str(documents[i].id) == n):
                
                return documents[i+1]
    return documents[len(documents)-1]    

def getIdPrev(n, mode, username):

    documents = ''
    if mode == 'feed':
        documents = Document.objects.all()
    elif mode == 'list':
        documents = Document.objects.filter(fotografo = getUserByUrl(username))
    print('Len' , len(documents))

    for i in range(1 , len(documents)):
        print('I:' , i )    
        
        if (str(documents[i].id) == n):
                
                return documents[i-1]
    return documents[0]  

    
