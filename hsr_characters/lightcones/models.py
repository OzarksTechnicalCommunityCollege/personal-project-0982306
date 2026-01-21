'''
AUTHOR: Cameron Butler
DATE:   1/20/2026

DESCRIPTION: Models will be used to display the light cones in hit game 
            Honkai: Star Rail
'''
from django.db import models

# Light Cone Model
# a light cone is similar to a weapon
class LightCone(models.Model):
    '''     VARIABLES      '''
    name = models.CharField(max_length=50)
    rarity = models.CharField(max_length=1)
    path = models.CharField(max_length=10)
    description = models.TextField()

    '''     CLASSES      '''
    # meta class to order the light cones by name
    class Meta:
        ordering = ['-name']

    '''     FUNCTIONS      '''
    # default method to return the light cone's name
    def __str__(self):
        return self.name