from django.db import models

# Create your models here.
SIZES = (
    ("Small", "Small"),
    ("Large", "Large")
)

TOPPINGS = (
    ('one', 'One'),
    ('two', 'two'),
    ('three', 'three'),
    ('Cheese', 'Cheese')
)

STYLES = (
    ('Regular', 'Regular'),
    ('Sicilian', 'Sicilian')
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

class Sub(Dish):
    foodtype = "sub"
    size = models.CharField(max_length=10, choices=SIZES)

    def __str__(self):
        return f"{self.foodtype})"

class Platter(Dish):
    foodtype = "Dinner Platter"
    size = models.CharField(max_length=10, choices=SIZES)

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
class Order(models.Model):
    username = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id} {self.username} {self.created_at} )"


class OrderItem(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    DishID = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="orderitems")
    def __str__(self):
        return f"{self.id} ({self.orderID})"