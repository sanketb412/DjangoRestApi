#A Serializer transforms model instances into JSON. This the real "magic" that Django Rest Framework
#provides for us. Consider that the end result of a traditional website is a page of HTML, CSS, and content
#from the database. But an API doesn't care about that: it's only raw data at endpoints, which means 
#JSON, and accompanying HTTP verbs that tell the API what actions can be taken.

# snippets/serializers
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos',
                  'language', 'style', )