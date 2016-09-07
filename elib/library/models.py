from django.db import models

# Create your models here.
class Ebook(models.Model):
	barcode_number=models.CharField(max_length=30)
	book_title=models.CharField(max_length=200)
	book_author=models.CharField(max_length=80)
	date_published=models.DateField()
	publisher=models.CharField(max_length=200)
	date_add=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	
