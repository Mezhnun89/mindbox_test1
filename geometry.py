import math

class GeometryCalculator:
    @staticmethod
    def circle_area(radius):
        """
        Calculate the area of a circle given its radius.
        """
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        """
        Calculate the area of a triangle given its three sides.
        """
        # Using Heron's formula
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        """
        Check if a triangle with given sides is a right triangle.
        """
        sides = sorted([side1, side2, side3])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

if __name__ == "__main__":
    # Example usage:
    radius = 5
    side1, side2, side3 = 3, 4, 5

    print("Circle area:", GeometryCalculator.circle_area(radius))
    print("Triangle area:", GeometryCalculator.triangle_area(side1, side2, side3))
    print("Is it a right triangle?", GeometryCalculator.is_right_triangle(side1, side2, side3))
