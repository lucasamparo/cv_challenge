from sympy.geometry import Point2D, Segment2D, Line

class StarModel:

    def __init__(self, current_position, old_position):
        curr = Point2D(current_position[0],current_position[1])
        old = Point2D(old_position[0],old_position[1])
        self.seg = Segment2D(Point2D(curr), Point2D(old))

    def get_line(self):
      bis = self.seg.perpendicular_bisector()
      return Line(bis.points[0],bis.points[1])