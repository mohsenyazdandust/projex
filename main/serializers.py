from rest_framework import serializers

from . import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'telegram_id': {'write_only': True}
        }
        fields = [
            'username',
            'first_name',
            'last_name',
            'telegram_id',
            'is_accepted',
        ]
        model = models.Student

    def get_or_create(self):
        return models.Student.objects.get_or_create(**self.validated_data)
