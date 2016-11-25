# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from myproject.myapp.models import Document , Comment
from myproject.myapp.forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.templatetags.staticfiles import static
import datetime
import exifread
import json

@login_required(login_url='/login/')
def list(request , username):
    # Handle file upload
    loggeduser = request.user.username
    print(username)
    editmode = False
    followed = False
    if loggeduser == username:
        editmode = True
    if request.method == 'POST':
        print('Entra1')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print('Entra')
            print(request.user.username)
            newdoc = Document(docfile=request.FILES['docfile'])
            print(newdoc.docfile)
            newdoc.setFotografo(request.user)
            newdoc.save()
            newdoc.makeinfo()
            newdoc.save()
            # Redirect to the document list after POST

            return HttpResponseRedirect('/list/' + request.user.username)
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.filter(fotografo = getUserByUrl(username))
    if getUserByUrl(username).userprofile in request.user.userprofile.follows.all() :
        followed = True
    print(followed)
    for seguidos in getUserByUrl(username).userprofile.follows.all():
        print(seguidos.user.username)
    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form, 'loggeduser' : loggeduser ,'editmode' : editmode, 'username': username, 'followed' : followed }
    )
def getUserByUrl(username):

    users = User.objects.all()

    for currentuser in users:

        if currentuser.username == username:
            return currentuser 

@login_required(login_url='/login/')
def feed(request):
    # Handle file upload
    if request.method == "GET" and request.is_ajax():
        data = []
        aux = {}
        query = request.GET.get("q")
        print(query)
        users = User.objects.filter(username__contains=query)[:5]
        for i in range(len(users)):
            aux["name"] = users[i].username
            aux["pk"] = users[i].pk
            data.append(dict(aux))
        print (data)
        jsonify(data)
        return HttpResponse(json.dumps(data),content_type="aplication/json")

    users = User.objects.all()
    documentsall = Document.objects.all()
    loggeduser = request.user
    documents = []
    for doc in documentsall:
        if doc.fotografo.userprofile  in loggeduser.userprofile.follows.all():
            documents.append(doc)
        print (documents, loggeduser.userprofile.follows.all())


    return render(
        request,
        'feed.html',
        {'documents': documents, 'loggeduser' : loggeduser, 'users' : users }
    )   
def list_delete(request,question_id):
    print('question_id ->',question_id)
    Document.objects.get(pk=question_id).delete()
    return HttpResponseRedirect('/list/' + request.user.username)
def view_image(request,question_id, mode,username):
    close = ''
    image = Document.objects.get(pk = question_id)
    print(question_id)
    if mode == 'list':
        close = '/list/' + username
    elif mode == 'feed':
        close = '/feed/' 

    comment_list = Comment.objects.filter( foto = question_id)

    for i in comment_list:
        print(i.text)
    nextimg = getIdNext(question_id, mode,username)
    previmg = getIdPrev(question_id, mode, username)

    print(nextimg , previmg)
    return render(
        request,
        'bigpicture.html',
        { 'image' : image, 'previmg' : previmg,'nextimg' : nextimg , 'previmg' : previmg , 'close' : close, 'mode' : mode , 'comment_list' : comment_list })  

def save_comment(request , question_id , mode):

    txt = request.POST["text"]

    comment = Comment()

    documents = Document.objects.all()

    comment.text = txt

    comment.date = datetime.datetime.now()

    comment.autor = request.user

    comment.foto = question_id

    comment.save()
    currentuser =  Document.objects.get(pk=question_id).fotografo.username



    return HttpResponseRedirect('/' +  mode +'/view/' +  currentuser + '/' + question_id)


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

def follow(request, username):
        
    loggeduser = request.user
    currentuser = getUserByUrl(username)
    loggeduser.userprofile.follows.add(currentuser.userprofile)
    return HttpResponseRedirect('/list/' + username)
def unfollow(request, username):
        
    loggeduser = request.user
    currentuser = getUserByUrl(username)

    loggeduser.userprofile.follows.remove(currentuser.userprofile)
    return HttpResponseRedirect('/list/' + username)

def jsonify(queryset):


    with open( '/home/vmartini/Documentos/Lumencapvm-master/src/for_django_1-9/myproject/myproject/myapp/static/json/usernames.json', 'w') as outfile:
        json.dump(queryset, outfile)

    print(json.dumps(queryset, ensure_ascii=False), "Funcaism")