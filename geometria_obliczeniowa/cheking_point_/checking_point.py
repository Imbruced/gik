import csv
import math as mt
import operator


class Point:

    # creating point with given coordinates
    def __init__(self, nr, x, y):
        self._nr = nr
        self._x = x
        self._y = y

    # points are equal when both coordinates are the same
    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    # points are not equal when x coordinate or y coordinate are not equal to each other
    def __ne__(self, other):
        return self._x != other._x and self._y != other._y

    # showing x and y coordinate
    def __str__(self):
        return str(self._x) + ', ' + str(self._y)

    @property
    def nr(self):
        return self._nr

    @nr.setter
    def nr(self, value):
        self._nr = value

    @nr.getter
    def nr(self):
        return self._nr

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        if value < 0:
            print('unpropriate value')
        else:
            self._x = value

    @x.getter
    def x(self):
        return self._x

    @y.setter
    def y(self, value):
        if value < 0:
            print('unpropriate value')
        else:
            self._y = value

    @property
    def coordinates(self):
        return [self._nr, self._x, self._y]

    @coordinates.setter
    def coordinates(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            self._x = value[1]
            self._y = value[2]
            self._nr = value[0]
        if isinstance(value, dict):
            print('sth')
            self._x = value.get('x', 0)
            self._y = value.get('y', 0)
            self._nr = value.get('nr', 0)

    @coordinates.getter
    def coordinates(self):
        return [self._nr, self._x, self._y]


class Polygon:

    def __init__(self):
        self.list_of_points = []
        self._clockwise_order = []
        self._sorted_points = []

    def load_points_from_file(self, file_name, separator):
        self.list_of_points = []
        with open(file_name) as file:
            for index, line in enumerate(file):
                nr, x_point, y_point = line.split(separator)
                nr = int(nr)
                x_point = float(x_point)
                y_point = float(y_point)
                self.list_of_points.append(Point(index+1, x_point, y_point))
        self._clockwise_order = self.turn_points_in_clockwise()

    def load_points(self, list_of_points):
        self.list_of_points = []
        for index, point in enumerate(list_of_points):
            x_point, y_point = point
            self.list_of_points.append(Point(index+1, x_point, y_point))
        self._clockwise_order = self.turn_points_in_clockwise()

    def check_if_point_is_inside(self, point):
        sum_ = 0
        angle = 0
        for index, point_of_polygon in enumerate(self._sorted_points):

            if index == len(self._sorted_points)-1:
                line1 = Line(point, self._sorted_points[0])
                line2 = Line(point, self._sorted_points[index])
                az1 = line1.count_azimuth()
                az2 = line2.count_azimuth()
                angle = az2 - az1
                print(angle)

            elif index < len(self._sorted_points):
                line1 = Line(point, self._sorted_points[index])
                line2 = Line(point, self._sorted_points[index + 1])
                az1 = line1.count_azimuth()
                az2 = line2.count_azimuth()
                angle = az2 - az1
                print(angle)

            sum_ += angle
        return sum_

    @property
    def points(self):
        if self.list_of_points:
            return self.list_of_points
        else:
            print('Point List is empty, load points using loads_point_from_file \n'
                  'or using load_points ')

    @points.setter
    def points(self, value):
        self.list_of_points = []
        for index, point in enumerate(value):
            self.list_of_points.append(Point(index, point[0], point[1]))

    @points.getter
    def points(self):
        return [(point.nr, point.x, point.y) for point in self.list_of_points]

    def find_centroid(self):
        A = 0
        Cx = 0
        Cy = 0
        for index, points in enumerate(self.list_of_points):
            if index != len(self.list_of_points)-1:
                a = (points.x * self.list_of_points[index+1].y - points.y * self.list_of_points[index+1].x)
                A +=  a / 2
                Cx += (points.x + self.list_of_points[index+1].x) * a
                Cy += (points.y + self.list_of_points[index + 1].y) * a
            elif index == len(self.list_of_points)-1:
                a = (points.x * self.list_of_points[0].y - points.y * self.list_of_points[0].x)
                A +=  a / 2
                Cx += (points.x + self.list_of_points[0].x) * a
                Cy += (points.y + self.list_of_points[0].y) * a

        return Cx/(6*A), Cy/(6*A)

    def turn_points_in_clockwise(self):
        Cx, Cy = self.find_centroid()
        dictionary = {}
        centroid = Point(len(self.list_of_points), Cx, Cy)
        for point in self.list_of_points:
            line = Line(centroid, point)
            dictionary[point.nr] = line.count_azimuth()

        sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1))
        sorted_order = [x[0] for x in sorted_dictionary]
        self._clockwise_order = sorted_order
        return self._clockwise_order

    def sort_points(self):
        for number in self._clockwise_order:
            self._sorted_points.append(self.list_of_points[number-1])

    @property
    def spoints(self):
        return self._sorted_points

    @spoints.getter
    def spoints(self):
        return self._sorted_points

    @property
    def clockwise_order(self):
        return self._clockwise_order

    @clockwise_order.getter
    def clockwise_order(self):
        return self._clockwise_order

    @clockwise_order.setter
    def clockwise_order(self, value):
        raise AttributeError


class Line:

    def __init__(self, pointa, pointb):
        self.pointa = pointa
        self.pointb = pointb

    def count_azimuth(self):
        dx = self.pointb.x - self.pointa.x
        dy = self.pointb.y - self.pointa.y
        angle = mt.atan2(dy, dx)*180/mt.pi
        az = angle + 360 if angle < 0 else angle
        return az



new_polygon = Polygon()
new_polygon.load_points_from_file('Wielokat.csv', ',')
# new_polygon.load_points([[0, 0], [2, 0], [2, 2], [0, 2]])
Cx, Cy = new_polygon.find_centroid()
# print(Cx, Cy)
#
new_polygon.sort_points()
# for x in new_polygon.spoints:
#     print(x.nr, x.x, x.y)
#
print(new_polygon.check_if_point_is_inside(Point(20,10,100)))
# print(new_polygon.turn_points_in_clockwise())

# print(new_polygon.points)


