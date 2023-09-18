# 1
"""The function area() accepts the argument radius and calculates the area of a circle. Write three tests using assert statements for the following conditions:

Assert that area(1) returns a float;

Assert that area(0) returns a value of 0;

Assert that area(5) is approximately equal to 78.5 (hint: math.isclose(..., abs_tol=0.1))"""

import math

def area(radius):
    return math.pi * radius ** 2

assert type(area(1)) == float
assert area(0) == 0
assert math.isclose(area(5), 78.5, abs_tol=0.1)

# 2 
"""In the spirit of the EAFP (easier to ask for forgiveness than permission) philosophy. Modify the code of the function area() and add a try/except statement to catch the type error raised by passing a string to area() as shown below:
area('10')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-28e1bc493b84> in <module>
----> 1 area('10')

<ipython-input-2-13e66cca8177> in area(radius)
      1 def area(radius):
      2     #Calculate the area of a circle based on the given radius.
----> 3     return math.pi * radius ** 2

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'"""

def area(radius):
    try:
        return math.pi * radius ** 2
    except TypeError:
        return 0
    
print(area('10'))

# 3
# In the spirit of the LBYL (look before you leap) philosophy. Modify the code of the function area() and add a conditional if/else statement to make sure that a user has passed a number (int or float) to the area() function. If they pass something else, raise a TypeError.

def area(radius):
    if type(radius) not in [int, float]:
        raise TypeError
    return math.pi * radius ** 2

print(area('10'))

# 4
"""For this exercise I want you to create a class called Circle. It should have the following characteristics:

It should be initiated with the argument radius and store this as an instance attribute.

Have a method area() which calculates the area of the circle.

Have a method circumference() which calculates the circumference of the circle.

Have the method __str__() which is a special method in Python and controls what is output to the screen when you print() an instance of your class (learn more here). The print() statement should print the string f"A Circle with radius {self.radius}".

I’ve provided some tests for you to check your class.

class Circle:
    #A circle with a radius r.

    pass # Remove this line and add your answer here.
    
assert Circle(3).radius == 3, "Test 1 failed."
assert math.isclose(Circle(3).area(), 28.3, abs_tol=0.1), "Test 2 failed."
assert math.isclose(Circle(3).circumference(), 18.8, abs_tol=0.1), "Test 3 failed."
assert Circle(3).__str__() == "A Circle with radius 3", "Test 4 failed."

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-5dbdbcaa4346> in <module>
----> 1 assert Circle(3).radius == 3, "Test 1 failed."
      2 assert math.isclose(Circle(3).area(), 28.3, abs_tol=0.1), "Test 2 failed."
      3 assert math.isclose(Circle(3).circumference(), 18.8, abs_tol=0.1), "Test 3 failed."
      4 assert Circle(3).__str__() == "A Circle with radius 3", "Test 4 failed."

TypeError: Circle() takes no arguments"""

class Circle:
    """A circle with a radius r."""
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"A Circle with radius {self.radius}"
    
assert Circle(3).radius == 3, "Test 1 failed."
assert math.isclose(Circle(3).area(), 28.3, abs_tol=0.1), "Test 2 failed."
assert math.isclose(Circle(3).circumference(), 18.8, abs_tol=0.1), "Test 3 failed."
assert Circle(3).__str__() == "A Circle with radius 3", "Test 4 failed."

# 5
"""Now, let’s create a new class sphere that inherits from the circle class we created above. It should have the following characteristics:

It should be initiated exactly the same as Circle was, with the single argument radius which is stored as an instance attribute.

Have a method volume() which calculates the volume of the sphere (43πr3
).

Outputs the string f"A Sphere with volume 4.19" when you call print(Sphere(1)) (hint: recall the __str__() method from the previous question).

I’ve provided some tests for you to check your class.

assert Sphere(3).radius == 3, "Test 1 failed."
assert math.isclose(Sphere(3).area(), 28.3, abs_tol=0.1), "Test 2 failed."
assert math.isclose(Sphere(3).circumference(), 18.8, abs_tol=0.1), "Test 3 failed."
assert math.isclose(Sphere(3).volume(), 113.1, abs_tol=0.1), "Test 3 failed."
assert Sphere(1).__str__() == "A Sphere with volume 4.19", "Test 4 failed."

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-10-605d8a1c6bb6> in <module>
----> 1 assert Sphere(3).radius == 3, "Test 1 failed."
      2 assert math.isclose(Sphere(3).area(), 28.3, abs_tol=0.1), "Test 2 failed."
      3 assert math.isclose(Sphere(3).circumference(), 18.8, abs_tol=0.1), "Test 3 failed."
      4 assert math.isclose(Sphere(3).volume(), 113.1, abs_tol=0.1), "Test 3 failed."
      5 assert Sphere(1).__str__() == "A Sphere with volume 4.19", "Test 4 failed."

NameError: name 'Sphere' is not defined"""

class Sphere(Circle):
    """A sphere with a radius r."""
    
    def volume(self):
        return 4/3 * math.pi * self.radius ** 3
    
    def __str__(self):
        return f"A Sphere with volume {self.volume():.2f}"
    
assert Sphere(3).radius == 3, "Test 1 failed."
assert math.isclose(Sphere(3).area(), 28.3, abs_tol=0.1), "Test 2 failed."
assert math.isclose(Sphere(3).circumference(), 18.8, abs_tol=0.1), "Test 3 failed."
assert math.isclose(Sphere(3).volume(), 113.1, abs_tol=0.1), "Test 3 failed."
assert Sphere(1).__str__() == "A Sphere with volume 4.19", "Test 4 failed."

# 6
"""Imagine that users of our Sphere class often want to instantiate our class with a circumference instead of a radius. Add a class method called from_circ() to the Sphere class that allows users to do this. The method should calculate the radius from the passed circumference, and then use that radius to make an instance of Sphere.

I’ve provided some tests for you to check your modified class.

assert Sphere.from_circ(0).radius == 0, "Test 1 failed."
assert Sphere.from_circ(3 * math.pi).radius == 1.5, "Test 2 failed." 
assert math.isclose(Sphere.from_circ(6).radius, 0.95, abs_tol=0.1), "Test 3 failed."
assert math.isclose(Sphere.from_circ(6).volume(), 3.65, abs_tol=0.1), "Test 4 failed."
assert Sphere.from_circ(6).__str__() == "A Sphere with volume 3.65", "Test 5 failed."

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-12-c64f2af0ae75> in <module>
----> 1 assert Sphere.from_circ(0).radius == 0, "Test 1 failed."
      2 assert Sphere.from_circ(3 * math.pi).radius == 1.5, "Test 2 failed."
      3 assert math.isclose(Sphere.from_circ(6).radius, 0.95, abs_tol=0.1), "Test 3 failed."
      4 assert math.isclose(Sphere.from_circ(6).volume(), 3.65, abs_tol=0.1), "Test 4 failed."
      5 assert Sphere.from_circ(6).__str__() == "A Sphere with volume 3.65", "Test 5 failed."

NameError: name 'Sphere' is not defined"""

class Sphere(Circle):
    """A sphere with a radius r."""
    
    def volume(self):
        return 4/3 * math.pi * self.radius ** 3
    
    def __str__(self):
        return f"A Sphere with volume {self.volume():.2f}"
    
    @classmethod
    def from_circ(cls, circ):
        return cls(circ / (2 * math.pi))
    
assert Sphere.from_circ(0).radius == 0, "Test 1 failed."
assert Sphere.from_circ(3 * math.pi).radius == 1.5, "Test 2 failed."
assert math.isclose(Sphere.from_circ(6).radius, 0.95, abs_tol=0.1), "Test 3 failed."
assert math.isclose(Sphere.from_circ(6).volume(), 3.65, abs_tol=0.1), "Test 4 failed."
assert Sphere.from_circ(6).__str__() == "A Sphere with volume 3.65", "Test 5 failed."