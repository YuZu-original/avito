import pytest


@pytest.mark.django_db
def test_ads_create(client, user, category):
    response = client.post(
        "/ad/create/",
        {
            "author": user.id,
            "name": "super test ad",
            "price": 100,
            "description": "test desc",
            "is_published": False,

            "category": category.id
        },
        content_type="application/json")
    print(response.data)
    assert response.status_code == 201
    assert response.data == {
        'id': 1,
        'author': user.id,
        'category': category.id,
        'description': 'test desc',
        'image': None,
        'is_published': False,
        'name': 'super test ad',
        'price': 100,
    }