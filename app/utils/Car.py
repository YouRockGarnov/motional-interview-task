from app.utils.Point import Point


class Car:
    def __init__(self, id: int, location: Point) -> None:
        self._id = id
        self._location = location
        self._destination = None

    @property
    def id(self) -> int:
        return self._id

    @property
    def location(self) -> Point:
        return self._location

    def is_available(self) -> bool:
        return self._destination is None

    def go_to(self, destination: Point) -> bool:
        if self.is_available():
            self._destination = destination
            return True
        else:
            return False

    def tick(self):
        if self._destination is not None:
            if self._destination.y == self._location.y:
                self._location.x += 1 if self._destination.x > self._location.x else -1

                if self._destination.x == self._location.x:
                    self._destination = None

            else:
                self._location.y += 1 if self._destination.y > self._location.y else -1
