from django.db import models

# Create your models here.
class User(models.Model):
	user_name=models.CharField(max_length=100)
	user_address=models.TextField()
	phone_number=models.CharField(max_length=15)
	email_address=models.EmailField(unique=True)
	def __unicode__(self):
		return self.user_name

class Book(models.Model):
	isbn=models.CharField(max_length=30)
	book_title=models.CharField(max_length=200)
	date_of_publication=models.DateField()
	def __unicode__(self):
		return self.book_title

class BooksBorrow(models.Model):
	user=models.ForeignKey(User)
	book=models.ForeignKey(Book)
	date_issued=models.DateField()
	date_due_for_return=models.DateField()
	date_returned=models.DateField()
	amount_of_fine=models.IntegerField(default=0)
	def __unicode__(self):
		return self.date_issued

class Author(models.Model):
	book=models.ManyToManyField(Book)
	first_name=models.CharField(max_length=60)
	last_name=models.CharField(max_length=60)
	def full_name(self):
		full_name="%s %s"%(self.first_name, self.last_name)
		return full_name
	def __unicode__(self):
		return self.full_name()

class Category(models.Model):
	book=models.ForeignKey(Book)
	category_name=models.CharField(max_length=100)
	def __unicode__(self):
		return self.category_name

