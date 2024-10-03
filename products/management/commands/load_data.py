import csv
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Load product data from a CSV file'

    def handle(self, *args, **kwargs):
        with open('amazon_laptop_prices_v01.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                price = row['price'].replace('$', '').replace(',', '').strip()
                price = float(price) if price else 0.0
                Product.objects.create(
                    brand=row['brand'],
                    model=row['model'],
                    price=price
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
