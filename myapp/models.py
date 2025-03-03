from django.db import models

class Link(models.Model):
    # get the name field instead of getting objct of this(self)
    def __str__(self):
        return self.name

    address =    models.CharField(max_length=1000,null=True,blank=True)
    name =      models.CharField(max_length=1000,null=True,blank=True)