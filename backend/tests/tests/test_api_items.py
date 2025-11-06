from clients.items import ItemsClient
from random import randint


def test_create_item(item_payload, items_authenticated_api_client: ItemsClient):
    response = items_authenticated_api_client.create_item(
        title=item_payload["title"],
        description=item_payload["description"],
    )
    assert response["title"] == item_payload["title"]
    assert response["description"] == item_payload["description"]


def test_get_item_by_id(item_payload, items_authenticated_api_client: ItemsClient):
    # создаём item
    created_item = items_authenticated_api_client.create_item(
        title=item_payload["title"],
        description=item_payload["description"],
    )
    # достаём этот же item по id
    item_id = created_item["id"]
    got = items_authenticated_api_client.get_item_by_id(item_id)

    # проверки — по аналогии с user-тестом
    assert got["id"] == item_id
    assert got["title"] == item_payload["title"]
    assert got["description"] == item_payload["description"]