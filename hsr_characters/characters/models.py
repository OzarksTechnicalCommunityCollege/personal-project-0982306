'''
AUTHOR: Cameron Butler
DATE:   1/20/2026

DESCRIPTION: Models will be used to display the characters in hit game
            Honkai: Star Rail
'''
from django.db import models

# Character Model
class Character(models.Model):
    '''     VARIABLES      '''
    name = models.CharField(max_length=30)
    rarity = models.CharField(max_length=1)
    path = models.CharField(max_length=15)
    element = models.CharField(max_length=10)
    description = models.TextField()

    '''     CLASSES      '''
    # meta class to order the characters by name
    class Meta:
        ordering = ['-name']

    '''     FUNCTIONS      '''
    # default method to return the character's name
    def __str__(self):
        return self.name


