# Dela Vega, Althea Janika M., 247553
# QUinto, Nathaniel Josh B., 246329
# February 16, 2026

"""
I have not discussed the Python language code with anyone other than my instructor or the teaching
assistants assigned to this course. I have not used Python language code obtained from another student, or any other unauthorized source, either
modified or unmodified.

If any Python language code or documentation used in my program was obtained from another source, such as a
textbook or course notes, that has been clearly noted with a proper citation in the comments of my program.
"""


from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return f"{self.name} - {self.city}, {self.country} created at: {self.created_at}"


class WaterBottle(models.Model):
    sku = models.CharField(max_length=50, primary_key=True)
    brand = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    mouth_size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    current_quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.sku}: {self.brand}, {self.mouth_size}, {self.size}, {self.color}, supplied by {self.supplied_by.name}, {self.cost} : {self.current_quantity}"

