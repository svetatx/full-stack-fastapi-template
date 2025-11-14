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

def test_update_item(item_payload, items_authenticated_api_client: ItemsClient):
    # создаём item
    created = items_authenticated_api_client.create_item(
        title=item_payload["title"],
        description=item_payload["description"],
    )
    # новые данные
    new_title = "updated title"
    new_description = "updated description"

    # обновляем item
    updated = items_authenticated_api_client.update_item(
        item_id=created["id"],
        title=new_title,
        description=new_description,
    )
    assert updated["id"] == created["id"]
    assert updated["title"] == new_title
    assert updated["description"] == new_description

def test_delete_item(item_payload, items_authenticated_api_client: ItemsClient):
    created = items_authenticated_api_client.create_item(
        title=item_payload["title"],
        description=item_payload["description"],
    )

    deleted = items_authenticated_api_client.delete_item(created["id"])

    assert "message" in deleted