class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 average_rating: float, clean_power: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        comfort_factor = car.comfort_class
        clean_difference = self.clean_power - car.clean_mark
        total_score = comfort_factor * clean_difference * self.average_rating
        return round(total_score / self.distance_from_city, 1)

    def rate_service(self, rate: float) -> None:
        new_count = self.count_of_ratings + 1
        total = self.count_of_ratings * self.average_rating + rate
        self.average_rating = round(total / new_count, 1)
        self.count_of_ratings = new_count


bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=9, brand="Audi")
ws = CarWashStation(6, 3.9, 8, 11)
ws.rate_service(5)
print(ws.calculate_washing_price(bmw))
print(ws.serve_cars([bmw, audi]))
print(audi.clean_mark)
print(ws.count_of_ratings)
print(ws.average_rating)
