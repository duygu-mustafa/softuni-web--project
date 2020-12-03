from django.db import models

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
        return f'{self.type}: {self.name}'