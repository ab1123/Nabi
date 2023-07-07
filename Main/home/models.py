from django.db import models



class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField()

