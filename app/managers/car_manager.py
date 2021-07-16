from app.utils.Car import Car
from app.utils.Point import Point
from copy import copy
from itertools import filterfalse
from math import inf


class CarManager:
    _initial_cars_state = [Car(i, Point(0, 0)) for i in range(3)]
    _cars = copy(_initial_cars_state)

    @staticmethod
    def book_nearest_available_car(source: Point, destination: Point) -> dict:
        available_cars = filterfalse(lambda car : not car.is_available(), CarManager._cars)

        result = {
            'car_id': -1,
            'total_time': inf
        }

        for car in available_cars:
            rec_drive_time = abs(car.location - source)
            if rec_drive_time < result['total_time']:
                result['car_id'] = car.id
                result['total_time'] = rec_drive_time


        return {} if result['car_id'] == -1 else result

    @staticmethod
    def tick():
        for car in CarManager._cars:
            car.tick()

    @staticmethod
    def reset():
        CarManager._cars = copy(CarManager._initial_cars_state)