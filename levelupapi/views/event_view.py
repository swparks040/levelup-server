"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Game, Gamer


class EventView(ViewSet):
    """Level up events view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event

        Returns:
            Response -- JSON serialized event
        """
        game_type = Event.objects.get(pk=pk)
        serializer = EventSerializer(game_type)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        game = Game.objects.get(pk=request.data["game"])
        organizer = Gamer.objects.get(user=request.auth.user)
        event = Event.objects.create(
            game=game,
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            organizer=organizer,
        
        )
        serializer = EventSerializer(event)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an event

        Returns:
            Response -- Empty body with 204 status code
        """

        event = Event.objects.get(pk=pk)
        event.game = Game.objects.get(pk=request.data["game"])
        event.description = request.data["description"]
        event.date = request.data["date"]
        event.time = request.data["time"]
        event.organizer = Gamer.objects.get(user=request.auth.user)
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer' )
