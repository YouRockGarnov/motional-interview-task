import pytest
from app.utils.Point import Point


__test_data = ({'x1': 1, 'y1': 2, 'x2': 3, 'y2': 4, 'sub_result': Point(-2, -2), 'abs_result': 3})


@pytest.mark.parametrize('x1,y1', [(__test_data['x1'], __test_data['y1'])])
def test_xy(x1: int, y1: int):
    point = Point(x1, y1)
    assert point.x == x1
    assert point.y == y1


@pytest.mark.parametrize('x1,y1,x2,y2,sub_result', [(__test_data['x1'], __test_data['y1'],
                                                    __test_data['x2'], __test_data['y2'],
                                                    __test_data['sub_result'])])
def test_sub(x1: int, y1: int, x2: int, y2: int, sub_result: Point):
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)

    assert point1 - point2 == sub_result


@pytest.mark.parametrize('x1,y1,abs_result', [(__test_data['x1'], __test_data['y1'],
                                                    __test_data['abs_result'])])
def test_sub(x1: int, y1: int, abs_result: Point):
    point1 = Point(x1, y1)

    assert abs(point1) == abs_result

