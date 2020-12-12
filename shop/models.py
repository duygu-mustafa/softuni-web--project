from django.db import models

from accounts.models import Profile


class Item(models.Model):
    EARRINGS = 'ER'
    RING = 'RI'
    NECKLACE = 'NL'
    TYPE_CHOICES = [
        (EARRINGS, 'earrings'),
        (RING, 'ring'),
        (NECKLACE, 'necklace')
    ]

    name = models.CharField(max_length=30)
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
    )
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='items/')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}# {self.type}: {self.name}'


class Favorite(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
