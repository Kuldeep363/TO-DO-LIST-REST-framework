from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    def makeSlug(self,*args, **kwargs):
        self.slugID = self.id
        return
    class Meta:
        model = Tasks
        fields = '__all__'
