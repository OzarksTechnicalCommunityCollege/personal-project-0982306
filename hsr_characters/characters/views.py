from django.shortcuts import render
from .models import Character

# function to display the characters
def character_list(request):
    lists = Character.all()
    return render(
        request,
        'characters/post/list.html',
        {'lists': lists}
    )