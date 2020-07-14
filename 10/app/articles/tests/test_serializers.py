from rest_framework import serializers

from articles.models import Article


class SampleSerializer(serializers.Serializer):
    sample_number = serializers.IntegerField(required=True)


def test_validation():
    valid_serializer = SampleSerializer(data={"sample_number": 1})
    assert valid_serializer.is_valid()
    invalid_serializer = SampleSerializer(data={"sample_number": "ab"})
    assert not invalid_serializer.is_valid()
    assert "sample_number" in invalid_serializer.errors
    valid_serializer = SampleSerializer(data={"sample_number": "1"})
    assert valid_serializer.is_valid()


def test_data_field():
    valid_serializer = SampleSerializer(data={"sample_number": "1"})
    valid_serializer.is_valid()
    assert valid_serializer.data["sample_number"] == 1
