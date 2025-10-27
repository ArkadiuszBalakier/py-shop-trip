import json
from typing import Any

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def load_config_data(file_path: str) -> dict[str, Any]:
    try:
        with open(file_path, "r", encoding="utf-8") as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found.")
    except json.decoder.JSONDecodeError:
        print("File has wrong JSON format.")

    fuel_price = config_data["FUEL_PRICE"]

    shops = []
    for shop_data in config_data["shops"]:
        shop = Shop(
            name=shop_data["name"],
            location=tuple(shop_data["location"]),
            products=shop_data["products"],
        )
        shops.append(shop)

    customers = []
    for customer_data in config_data["customers"]:

        car_data = customer_data["car"]
        car = Car(
            brand=car_data["brand"],
            fuel_consumption=car_data["fuel_consumption"],
        )

        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=tuple(customer_data["location"]),
            money=customer_data["money"],
            car=car,
        )
        customers.append(customer)

    return {
        "fuel_price": fuel_price,
        "shops": shops,
        "customers": customers
    }