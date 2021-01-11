from rest_framework import serializers
from gallery.models import Gallery, BulkFile

class GalerySerialize(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class BullFielSerialize(serializers.ModelSerializer):
    class Meta:
        model = BulkFile
        fields = "__all__"