from rest_framework import serializers
from .models import Inventory
from datetime import date

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['entry_id', 'title', 'author', 'genre', 'publication_date', 'isbn']

    def validate_isbn(self, value):
        if len(value) not in [10, 13] or not value.isdigit():
            raise serializers.ValidationError('ISBN must be either 10 or 13 digits long')
        return value

    def validate_publication_date(self, value):
        if value > date.today():
            raise serializers.ValidationError('Publication date cannot be in the future')
        return value
