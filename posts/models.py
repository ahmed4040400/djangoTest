""" a model is like a database scheme
    (a blue print of the info)

    and to actualy apply this scheme to the database
    we have to do some thing called migrations

    we do this in the terminal
    and then you can notice the migrations file in the apply
    (posts app)
  """

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 250)
    date = models.DateTimeField()
    image = models.ImageField(upload_to = "media/")
    body = models.TextField()
    #the return value  of this method
    #show in the admin console ad a post title
    # in posts list
    def __str__(self):
        return self.title


    def dateFormate(self):
        return self.date.strftime('%b %e %y')



    def bodyThumpnail(self):
        return self.body[:70] + "...."
