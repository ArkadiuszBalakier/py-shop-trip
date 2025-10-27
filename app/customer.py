from dataclasses import dataclass


from car import Car
from shop import Shop

@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: tuple
    money: float
    car: Car

    def total_product_cost(self, shop: Shop) -> float:
        total_cost = 0
        for product , quantity in self.product_cart.items():
            if product in shop.products:
                total_cost += shop.products[product] * quantity
        return total_cost

    def total_trip_cost(
            self,
            shop_position: tuple[float, float],
            fuel_price: float,
    ) -> float:
        distance = (((self.location[0] - shop_position[0]) ** 2)
                    + (self.location[1] - shop_position[1]) ** 2 ) ** 0.5
        liters_one_way = distance * (self.car.fuel_consumption / 100)
        cost_one_way = liters_one_way * fuel_price
        total_cost = cost_one_way * 2
        return total_cost
