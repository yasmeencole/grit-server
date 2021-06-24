"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gritapi.models import NearEathObject, near_earth_object
from django.contrib.auth.models import User



class NearEarthObjectView(ViewSet):
    """Near Earth Objects"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized NEO instance
        """

        # Uses the token passed in the `Authorization` header

        # Create a new Python instance of the Game class
        # and set its properties from what was sent in the
        # body of the request from the client.
        near_earth_object = NearEathObject()
        near_earth_object.user = request.auth.user
        near_earth_object.neo_reference = request.data["neo_reference"]
        near_earth_object.name = request.data["name"]
        near_earth_object.image = request.data["image"]
        near_earth_object.estimated_diameter = request.data["estimated_diameter"]
        near_earth_object.is_potentially_hazardous = request.data["is_potentially_hazardous"]
        near_earth_object.close_approach_date = request.data["close_approach_date"]
        near_earth_object.miles_per_hour = request.data["miles_per_hour"]
        near_earth_object.orbiting_body = request.data["orbiting_body"]

        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed as the
        # `gameTypeId` in the body of the request.
        # game_type = GameType.objects.get(pk=request.data["game_type_id"])
        # game.game_type = game_type

        # Try to save the new game to the database, then
        # serialize the game instance as JSON, and send the
        # JSON as a response to the client request
        try:
            near_earth_object.save()
            serializer = NearEarthObjectSerializer(near_earth_object, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single NEO

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/nearearthobjects/2
            #
            # The `2` at the end of the route becomes `pk`
            near_earth_object = NearEathObject.objects.get(pk=pk)
            serializer = NearEarthObjectSerializer(near_earth_object, context={'request': request})
            return Response(serializer.data)
        except NearEathObject.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        user = request.auth.user

        # Do mostly the same thing as POST, but instead of
        # creating a new instance of Game, get the game record
        # from the database whose primary key is `pk`
        near_earth_object = NearEathObject.objects.get(pk=pk)
        
        # if gamer is not gmae.gamer:
        #     return Response{({}, status=status.HTTP_403_FORBIDDEN)
        near_earth_object.neo_reference = request.data["neo_reference"]
        near_earth_object.name = request.data["name"]
        near_earth_object.image = request.data["image"]
        near_earth_object.estimated_diameter = request.data["estimated_diameter"]
        near_earth_object.is_potentially_hazardous = request.data["is_potentially_hazardous"]
        near_earth_object.close_approach_date = request.data["close_approach_date"]
        near_earth_object.miles_per_hour = request.data["miles_per_hour"]
        near_earth_object.orbiting_body = request.data["orbiting_body"]

        try:
            near_earth_object.save()
        except ValidationError as ex:
            return Response({ 'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single NEO

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            near_earth_object = NearEathObject.objects.get(pk=pk)
            near_earth_object.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except NearEathObject.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to NEO resource
        
        Returns:
            Response -- JSON serialized list of NEO's
        """
        # Get all NEO records from the database
        near_earth_object = NearEathObject.objects.all()
        
        user = request.auth.user
        # looking for anything after ? user=me
        list_params = self.request.query_params.get("user", None)
        
        if list_params is not None:
            near_earth_object = near_earth_object.filter(user=user)
        

        serializer = NearEarthObjectSerializer(near_earth_object, many=True, context={'request': request})
        return Response(serializer.data)

# serializer class determines how the Python data should be serialized as JSON to be sent back to the client. 
class NearEarthObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearEathObject
        fields = ('id', "user_id", 'neo_reference', 'name', 'image', 'estimated_diameter', 'is_potentially_hazardous', 'close_approach_date', 'miles_per_hour', 'orbiting_body')
        depth = 1