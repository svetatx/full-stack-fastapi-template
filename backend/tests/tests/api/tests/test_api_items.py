from api.clients.items import create_item
from random import randint


def test_create_item(auth_headers, item_payload):
    response = create_item(
        title=item_payload["title"],
        description=item_payload["description"],
        headers=auth_headers,
    )
    assert response["title"] == item_payload["title"]
    assert response["description"] == item_payload["description"]


def test_get_item_by_id(auth_headers, item_payload):
    # создаём item
    created_item = create_item(
        title=item_payload["title"],
        description=item_payload["description"],
        headers=auth_headers,
    )
# достаём этот же item по id
    item_id = created_item["id"]
    got = get_item_by_id(item_id, headers=auth_headers)

    # проверки — по аналогии с user-тестом
    assert got["id"] == item_id
    assert got["title"] == item_payload["title"]
    assert got["description"] == item_payload["description"]