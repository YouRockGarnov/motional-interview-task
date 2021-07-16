from app.utils.Car import Car
from app.utils.Point import Point
import pytest


__test_data = {'id': 1, 'location': Point(0, 0), 'destination': Point(2, 2), 'location_after_tick': Point(0, 1)}


@pytest.mark.parametrize('id,location', [(__test_data['id'], __test_data['location'])])
def test_id(id, location):
    car = Car(id, location)
    assert car.id == id


@pytest.mark.parametrize('id,location', [(__test_data['id'], __test_data['location'])])
def test_location(id, location):
    car = Car(id, location)
    assert car.location == location


@pytest.mark.parametrize('id,location,destination', [(__test_data['id'], __test_data['location'],
                                                     __test_data['destination'])])
def test_go_to(id, location, destination):
    car = Car(id, location)
    assert car.is_available()

    assert car.go_to(destination)
    assert not car.is_available()
    assert not car.go_to(destination)


@pytest.mark.parametrize('id,location,destination,location_after_tick', [(__test_data['id'], __test_data['location'],
                                                     __test_data['destination'], __test_data['location_after_tick'])])
def test_tick(id, location, destination, location_after_tick):
    car = Car(id, location)
    assert car.go_to(destination)

    car.tick()
    assert car.location == location_after_tick
