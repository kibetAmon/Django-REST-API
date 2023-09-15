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

    # A function to CREATE a person
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

        return response

    # UPDATE a person
    def put(self, request, pk=None, format=None):

        # Get the person to update
        person_to_update = person.objects.get(pk=pk)

        # Pass the instance to update to the serializer, and the data and also partial to the serializer
        # Passing partial will allow us to update without passing the entire person object

        serializer = personSerializer(instance=person_to_update, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Person updated successfully',
            'data': serializer.data
        }

        return response

    # DELETE a person
    def delete(self, request, pk, format=None):
        person_to_delete = person.objects.get(pk=pk)

        # delete the person
        person_to_delete.delete()
        return Response({
            'message':'Person deleted successfully'
        })
