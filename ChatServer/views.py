from django.shortcuts import render


def index(request):
    return render(request, "ChatServer/index.html")

def room(request, room_name):
    username=request.session['username']
    return render(request, "ChatServer/room.html", {"room_name": room_name,'user_name':username})