from django.db import models


class Url ( models . Model ):
    Url_text= models.CharField(max_length=200)

    def __str__(self):
        return self. Url_text