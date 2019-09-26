from django.db import models

# Create your models here.

class tvManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        new_title=Show.objects.filter(title=postData['title'])
        if  new_title:
            errors["title"] = "Title already exists"
        if len(postData['network']) < 2:
            errors["network"] = "Network should be at least 2 characters"
        if len(postData['release_date']) < 0:
            errors["release_date"] = "Realease Date cannot be blank"
        if len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = tvManager()
    # authors = a list of authors associated with a given book
    def __repr__(self):
        return f"<Show object: {self.title} {self.network} {self.release_date} {self.description} ({self.id})>"