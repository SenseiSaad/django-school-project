from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def oneBlog(request, pk):
    try:
        contact = Contact.objects.get(id=pk)
    except Contact.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=404)
    serializer = ContactSerializer(contact)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def allBlogs(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def createBlog(request):
    serializers=ContactSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)

@api_view(['PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])

def updateBlog(request, pk):
    contact = Contact.objects.get(id=pk)
    serializers = ContactSerializer(contact, data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)

@api_view(['DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def deleteBlog(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return Response({'message': 'Contact was deleted'})

