from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSetializer

@api_view(['GET'])
def getnote(request,pk):
    note=Note.objects.get(id=pk)
    serializer=NoteSetializer(note)
    return Response(serializer.data)

@api_view(['GET'])
def allnotes(request):
    notes=Note.objects.all()
    serializer=NoteSetializer(notes,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def adanote(request):
    serializer=NoteSetializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)    

@api_view(['POST'])
def updatenote(request,pk):
    note=Note.objects.get(id=pk)
    serializer=NoteSetializer(note,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)   

@api_view(['DELETE'])
def deletenote(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return Response('Note Deleted')
