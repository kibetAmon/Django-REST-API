from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import person
from .serializers import personSerializer
from rest_framework.response import Response


# Create your views here.
class PersonAPIView(APIView):

    # READ a single person
    def get_object(self, pk):
        try:
            return person.objects.get(pk=pk)
        except person.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = personSerializer(data)

        else:
            data = person.objects.all()
            serializer = personSerializer(data, many=True)
            return Response(serializer.data)

    # A function to create a person
    def post(self, request, format=None):
        data = request.data
        serializer = personSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create person in the database
        serializer.save()

        # Return response to user
        response = Response()
        response.data = {
            'message': 'Person added successfully',
            'data': serializer.data
        }
