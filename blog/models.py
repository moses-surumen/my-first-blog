from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User') #this is a link to another model.
	title = models.CharField(max_length=200) #this is how you define text with a limited number of characters.
	text = models.TextField() #this is for long texts without a limit. It will be ideal for a blog post content.
	created_date = models.DateTimeField(default=timezone.now) #this is a date and time.
	published_date = models.DateTimeField(blank=True, null=True) #this is a date and time.

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title