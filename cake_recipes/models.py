from django.db import models

# Create your models here.
class Cake(models.Model):
    """The cakes name."""
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Show the cakes name."""
        return self.text


class Recipe(models.Model):
    """The cake's recipe."""
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Show the cakes recipe."""
        return self.text 