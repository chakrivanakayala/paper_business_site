from django.contrib import admin
from .models import PaperOrder

class PaperOrderAdmin(admin.ModelAdmin):
    # Admin panel lo columns laaga kanipisthundi
    list_display = ('customer_name', 'paper_type', 'quantity', 'order_date')
    # Search bar add chesthundhi
    search_fields = ('customer_name', 'paper_type')

admin.site.register(PaperOrder, PaperOrderAdmin)