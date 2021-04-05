from django.shortcuts import render, get_object_or_404
from  django.http import HttpResponse, Http404
from .models import Board
from django.contrib.auth.models import User
from .models import Topic, Post

# Create your views here.

def home(request):
    boards =Board.objects.all()

    return  render(request,'home.html',{'boards':boards})
    # boards_name = []
    # for board in boards:
    #     boards_name.append(board.name)
    # res_ht = '<br>'.join(boards_name)
    # return  HttpResponse(res_ht)

def board_topics(request,board_id):
    # try:
    #     board = Board.objects.get(pk=board_id)
    # except:
    #     raise Http404
    board=get_object_or_404(Board, pk=board_id)
    return render(request, 'topics.html',{'board':board})

def new_topic(request,board_id):
    board=get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        user = User.objects.first()

        topic = Topic.objects.create(
            subject = subject,
            board =board_id,
            created_by =user,
        )
        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
    return render(request,'new_topic.html',{'board':board})






















def about(request):
    return HttpResponse("Hello")



