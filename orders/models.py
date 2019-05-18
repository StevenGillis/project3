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

class Buyer(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name})"

#class Order(models.Model):
   # time = models.CharField(max_length=64, default="now")
   # totalamount = models.CharField(max_length=64, default=0)
    #buyer_id = models.ForeignKey(Buyer, default=1, on_delete=models.CASCADE, related_name="boughtby")

   # def __str__(self):
        #return f"{self.time})"

