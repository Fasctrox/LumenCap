from django.shortcuts import render

# Create your views here.
from comments.models import Comment

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render_to_response

import datetime

from django.template import RequestContext




# Create your views here.

def comments(request):

    comment_list = Comment.objects.order_by("-date")
    
    return render_to_response('comments.html', {'comment_list': comment_list})


@csrf_exempt
def save(request):

    txt = request.POST["text"]

    title = request.POST["title"]

    comment = Comment()

    comment.text = txt

    comment.date = datetime.datetime.now()

    comment.title = title

    comment.save()

    return render_to_response('save.html', RequestContext(request, {}))