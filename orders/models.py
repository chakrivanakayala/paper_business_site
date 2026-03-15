from django.db import models

class PaperOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    paper_type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.paper_type}"