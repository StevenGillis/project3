from django.db import models

# Create your models here.
SIZES = (
    ("S", "Small"),
    ("L", "Large")
)

TOPPINGS = (
    ('one', 'One'),
    ('two', 'two'),
    ('three', 'three'),
    ('Cheese', 'Cheese')
)

STYLES = (
    ('R', 'Regular'),
    ('S', 'Sicilian')
)

### Food related classes
class Dish(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} ({self.price})"


class Pasta(Dish):
    foodtype = "Pasta"

    def __str__(self):
        return f"{self.foodtype})"


class Salad(Dish):
    foodtype = "Salad"

    def __str__(self):
        return f"{self.foodtype})"


class Pizza(Dish):
    foodtype = "Pizza"
    style = models.CharField(max_length=10, choices=STYLES)
    size = models.CharField(max_length=10, choices=SIZES)
    toppings = models.CharField(max_length=10, choices=TOPPINGS)
    def __str__(self):
        return f"{self.foodtype} {self.style} {self.size} {self.toppings})"

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name})"

### Order related classes