from django.shortcuts import render
from .models import Character

# function to display the characters
def character_list(request):
    # issue is on the line below
    lists = Character
    return render(
        request,
        'characters/character/list.html',
        {'lists': lists}
    )