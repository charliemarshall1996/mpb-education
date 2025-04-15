
import pytest
from curricula import models


@pytest.mark.django_db
def test_subject_creates():
    data = {'name': 'science'}

    subject = models.Subject(**data)
    subject.save()
    assert subject.name == data['name']
    assert subject.created_at
    assert subject.updated_at
