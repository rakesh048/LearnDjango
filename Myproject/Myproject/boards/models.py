from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Board(models.Model):
	name = models.CharField(max_length=100,unique=True)
	description = models.CharField(max_length=100)

	def __str__(self):    ##### String representation of objects in query like before  [<Board: Board object>, <Board: Board object>]> after <QuerySet [<Board: Django>, <Board: Python>]>
		return self.name

class Topic(models.Model):
	subject = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board,related_name='topics')   #### Related Name used for reverse relationship here when Board make ralation with Topic
	starter = models.ForeignKey(User,related_name='topics')

class Post(models.Model):
	message = models.TextField(max_length=4000)
	topic = models.ForeignKey(Topic,related_name='posts')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User,related_name='posts')
	updated_by = models.ForeignKey(User,null=True,related_name='+') #### + for does not make reverse relationship


### We use the model Manager to query in database like Board.objects.all()
### Carefully use of get query - 
###  1. if item in db then use the get otherwise raise exception
###  2. generally used in PK because it return the single object not multiple 
###  3. match should be case sensitive