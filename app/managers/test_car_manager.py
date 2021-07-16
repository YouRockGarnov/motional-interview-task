import pytest

from app.managers.car_manager import CarManager
from app.utils.Point import Point


def test_book():
    CarManager.reset()
    book_data = (
            ({'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'car_id': 1, 'total_time': 2}),
            ({'x': 1, 'y': 1}, {'x': 5, 'y': 5}, {'car_id': 2, 'total_time': 10}),
            ({'x': -1, 'y': 1}, {'x': 5, 'y': 10}, {'car_id': 3, 'total_time': 17})
    )

    for source, destination, expected in book_data:
        actual = CarManager.book_nearest_available_car(Point(**source), Point(**destination))
        __check_car(expected, actual)


def __check_car(expected, actual):
    test_string = 'expected: {}, actual: {}'.format(expected, actual)

    assert 'car_id' in actual or 'total_time' in actual, \
        'FAILED!!! - {} - car_id or total_time missing'.format(test_string)

    assert actual['car_id'] == expected['car_id'], 'wrong car_id'
    assert actual['total_time'] == expected['total_time'], 'wrong total_time'


def test_tick():
    CarManager.reset()

    CarManager.book_nearest_available_car(Point(1, 1), Point(2, 2))
    CarManager.tick()

    assert CarManager._cars[1].location == Point(0, 1)


def test_reset():
    test_book()

    CarManager.reset()
    for car1, car2 in zip(CarManager._cars, CarManager._initial_cars_state):
        assert car1 == car2
