from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from .models import Board,Topic,Post
from django.contrib.auth.models import User
from .forms import NewTopicForm

def home(request):
	boards = Board.objects.all()
	print(boards.reverse)
	return render(request,'home.html',{"boards":boards})

def board_topics(request,pk):
	# try:
	#     board = Board.objects.get(id=pk)
	# except Board.DoesNotExist:
	# 	raise Http404
	board = get_object_or_404(Board,pk=pk)
	return render(request,'topics.html',{'board':board})
	
def new_topic(request,pk):
	board = Board.objects.get(pk=pk)
	user = User.objects.first()
	if request.method == 'POST':
	    form = NewTopicForm(request.POST)
	    if form.is_valid():
	        topic = form.save(commit=False)
	        topic.board = board
	        topic.starter = user
	        topic.save()
	        post = Post.objects.create(
	            message=form.cleaned_data.get('message'),
	            topic=topic,
	            created_by=user
	        )
	        return redirect('board_topics', pk=board.pk)
	else:
	    form = NewTopicForm()
	return render(request, 'new_topic.html', {'board': board, 'form': form})