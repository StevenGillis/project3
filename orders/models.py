from django.db import models

# Create your models here.


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

    def __str__(self):
        return f"{self.foodtype})"

class Topping(models.Model):
    name = models.CharField(max_length=64)
    pizza = models.ManyToManyField(Pizza, blank=True, related_name="toppings")

    def __str__(self):
        return f"{self.name} ({self.pizza})"

### Order related classes
