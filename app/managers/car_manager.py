from app.utils.Car import Car
from app.utils.Point import Point
from copy import deepcopy
from itertools import filterfalse
from math import inf


# singleton for operations with cars
class CarManager:
    _initial_cars_state = dict([(i, Car(i, Point(0, 0))) for i in range(1, 4)])
    _cars = deepcopy(_initial_cars_state)

    @staticmethod
    def book_nearest_available_car(source: Point, destination: Point) -> dict:
        available_cars = list(filterfalse(lambda item: not item[1].is_available(), CarManager._cars.items()))

        result = {
            'car_id': -1,
            'total_time': inf
        }

        for id, car in available_cars:
            drive_time = abs(source - car.location) + abs(destination - source)
            if drive_time < result['total_time']:
                result['car_id'] = id
                result['total_time'] = drive_time

                CarManager._cars[id].go_to(destination)

        return {} if result['car_id'] == -1 else result

    @staticmethod
    def tick():
        for car in CarManager._cars.values():
            car.tick()

    @staticmethod
    def reset():
        CarManager._cars = deepcopy(CarManager._initial_cars_state)