from django.core.management.base import BaseCommand
from restaurant.models import MenuItem


class Command(BaseCommand):
    help = 'Populate menu items from the restaurant menu card'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating menu items...')
        
        # Clear existing menu items (optional - comment out if you want to keep existing items)
        # MenuItem.objects.all().delete()
        
        menu_data = self.get_menu_data()
        
        created_count = 0
        updated_count = 0
        
        for item_data in menu_data:
            item, created = MenuItem.objects.update_or_create(
                name=item_data['name'],
                category=item_data['category'],
                defaults={
                    'description': item_data.get('description', ''),
                    'sub_category': item_data.get('sub_category'),
                    'sizes_and_prices': item_data['sizes_and_prices'],
                    'available': item_data.get('available', True),
                }
            )
            if created:
                created_count += 1
            else:
                updated_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated menu! Created: {created_count}, Updated: {updated_count}'
            )
        )

    def get_menu_data(self):
        """Returns all menu items from the menu card"""
        return [
            # CHINESE VEG STARTER - MOMOS
            {'name': 'VEG MOMOS', 'category': 'chinese_veg_starter', 'sub_category': 'momos', 
             'sizes_and_prices': [{'size': 'Steam', 'price': 140}, {'size': 'Fry', 'price': 160}]},
            {'name': 'PANEER MOMOS', 'category': 'chinese_veg_starter', 'sub_category': 'momos',
             'sizes_and_prices': [{'size': 'Steam', 'price': 180}, {'size': 'Fry', 'price': 210}]},
            {'name': 'CHEESE MOMOS', 'category': 'chinese_veg_starter', 'sub_category': 'momos',
             'sizes_and_prices': [{'size': 'Steam', 'price': 180}, {'size': 'Fry', 'price': 210}]},
            {'name': 'CHICKEN MOMOS', 'category': 'chinese_nonveg_starter', 'sub_category': 'momos',
             'sizes_and_prices': [{'size': 'Steam', 'price': 180}, {'size': 'Fry', 'price': 200}]},
            
            # CHINESE VEG STARTER - CHILLY
            {'name': 'CHILLY', 'category': 'chinese_veg_starter', 'sub_category': 'chilly',
             'sizes_and_prices': [{'size': 'Dry', 'price': 170}, {'size': 'Gravy', 'price': 220}]},
            {'name': 'CORN MANCHURIAN', 'category': 'chinese_veg_starter', 'sub_category': 'manchurian',
             'sizes_and_prices': [{'size': 'Dry', 'price': 170}, {'size': 'Gravy', 'price': 220}]},
            {'name': 'MANCHURIAN', 'category': 'chinese_veg_starter', 'sub_category': 'manchurian',
             'sizes_and_prices': [{'size': 'Dry', 'price': 170}, {'size': 'Gravy', 'price': 220}]},
            
            # CHINESE VEG STARTER - CRISPY
            {'name': 'CRISPY', 'category': 'chinese_veg_starter', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Dry', 'price': 200}, {'size': 'Gravy', 'price': 250}]},
            {'name': 'VEG BHEL', 'category': 'chinese_veg_starter', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Full', 'price': 180}]},
            {'name': 'SCHEZWAN VEG', 'category': 'chinese_veg_starter', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Dry', 'price': 200}, {'size': 'Gravy', 'price': 270}]},
            {'name': 'GREEN PEPPER SAUCE', 'category': 'chinese_veg_starter', 'sub_category': 'gravy',
             'sizes_and_prices': [{'size': 'Gravy', 'price': 270}]},
            
            # CHINESE VEG STARTER - ROLLS
            {'name': 'SPRING ROLL (3pcs)', 'category': 'chinese_veg_starter', 'sub_category': 'rolls',
             'sizes_and_prices': [{'size': 'Full', 'price': 190}, {'size': 'Half', 'price': 230}]},
            {'name': 'CRISPY CORN', 'category': 'chinese_veg_starter', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Full', 'price': 170}]},
            {'name': 'CIGGA ROLL (4pcs)', 'category': 'snacks', 'sub_category': 'rolls',
             'sizes_and_prices': [{'size': 'Full', 'price': 180}]},
            {'name': 'STEAM CORN (4pcs)', 'category': 'snacks', 'sub_category': 'steam',
             'sizes_and_prices': [{'size': 'Full', 'price': 180}]},
            {'name': 'LOLLIPOP (8pcs)', 'category': 'chinese_nonveg_starter', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Full', 'price': 170}]},
            {'name': 'CHANA KOLWADA', 'category': 'chinese_veg_starter', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Full', 'price': 170}]},
            
            # SOUPS
            {'name': 'MANCHOW SOUP', 'category': 'soups', 'sub_category': 'chinese_soup',
             'sizes_and_prices': [{'size': 'Veg', 'price': 130}, {'size': 'Chicken', 'price': 140}]},
            {'name': 'HOT AND SOUR SOUP', 'category': 'soups', 'sub_category': 'hot_sour_soup',
             'sizes_and_prices': [{'size': 'Veg', 'price': 130}, {'size': 'Chicken', 'price': 140}]},
            {'name': 'CLEAR SOUP', 'category': 'soups', 'sub_category': 'clear_soup',
             'sizes_and_prices': [{'size': 'Veg', 'price': 130}, {'size': 'Chicken', 'price': 140}]},
            {'name': 'SWEET CORN SOUP', 'category': 'soups', 'sub_category': 'chinese_soup',
             'sizes_and_prices': [{'size': 'Veg', 'price': 130}, {'size': 'Chicken', 'price': 140}]},
            {'name': 'LEMON CORIANDER SOUP', 'category': 'soups', 'sub_category': 'chinese_soup',
             'sizes_and_prices': [{'size': 'Veg', 'price': 130}, {'size': 'Chicken', 'price': 180}]},
            {'name': 'TOMATO SOUP', 'category': 'soups', 'sub_category': 'chinese_soup',
             'sizes_and_prices': [{'size': 'Full', 'price': 160}]},
            
            # SNACKS
            {'name': 'CIGGA ROLL', 'category': 'snacks', 'sub_category': 'rolls',
             'sizes_and_prices': [{'size': 'Steam', 'price': 130}, {'size': 'Fry', 'price': 140}]},
            {'name': 'STEAM CORN', 'category': 'snacks', 'sub_category': 'steam',
             'sizes_and_prices': [{'size': 'Steam', 'price': 140}, {'size': 'Fry', 'price': 160}]},
            {'name': 'SPRING ROLL', 'category': 'snacks', 'sub_category': 'rolls',
             'sizes_and_prices': [{'size': 'Steam', 'price': 140}, {'size': 'Fry', 'price': 160}]},
            {'name': 'ROAST CORN', 'category': 'snacks', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': 'Full', 'price': 200}, {'size': 'Half', 'price': 280}]},
            {'name': 'FRENCH FRIES', 'category': 'snacks', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': 'Full', 'price': 140}]},
            {'name': 'FRENCH CHEESE FRIES', 'category': 'snacks', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': 'Full', 'price': 160}]},
            
            # VEG INDIAN SNACKS
            {'name': 'VEG FINGER', 'category': 'veg_indian_snacks', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': '4PC', 'price': 220}]},
            {'name': 'VEG CHEESE FINGER', 'category': 'veg_indian_snacks', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': '4PC', 'price': 270}]},
            {'name': 'PANEER PAKODA', 'category': 'veg_indian_snacks', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': '4PC', 'price': 230}]},
            {'name': 'FRY PAPAD', 'category': 'veg_indian_snacks', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': '4PC', 'price': 90}]},
            {'name': 'MASALA PAPAD', 'category': 'veg_indian_snacks', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': '4PC', 'price': 70}]},
            {'name': 'CHEESE PAKODA', 'category': 'veg_indian_snacks', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': '10PC', 'price': 230}]},
            {'name': 'PANEER CHATPATA', 'category': 'veg_indian_snacks', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Full', 'price': 280}]},
            {'name': 'MUSHROOM CHATPATA', 'category': 'veg_indian_snacks', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': '10PC', 'price': 280}]},
            {'name': 'VEG PAPAD', 'category': 'veg_indian_snacks', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': 'Full', 'price': 120}]},
            
            # NON-VEG INDIAN SNACKS
            {'name': 'CHICKEN FINGER', 'category': 'nonveg_indian_snacks', 'sub_category': 'chicken',
             'sizes_and_prices': [{'size': '6PC', 'price': 260}]},
            {'name': 'CHICKEN CHEESE FINGER', 'category': 'nonveg_indian_snacks', 'sub_category': 'chicken',
             'sizes_and_prices': [{'size': '6PC', 'price': 310}]},
            {'name': 'EGG PAKODA', 'category': 'nonveg_indian_snacks', 'sub_category': 'egg',
             'sizes_and_prices': [{'size': '4PC', 'price': 140}]},
            
            # MOCKTAIL
            {'name': 'FRESH LIME SODA', 'category': 'mocktail', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 120}]},
            {'name': 'FRESH LIME WATER', 'category': 'mocktail', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 120}]},
            
            # CHINESE NON-VEG STARTER
            {'name': 'CHICKEN CHILLY', 'category': 'chinese_nonveg_starter', 'sub_category': 'chilly',
             'sizes_and_prices': [{'size': 'Dry', 'price': 210}, {'size': 'Gravy', 'price': 250}]},
            {'name': 'CHICKEN MANCHURIAN', 'category': 'chinese_nonveg_starter', 'sub_category': 'manchurian',
             'sizes_and_prices': [{'size': 'Dry', 'price': 210}, {'size': 'Gravy', 'price': 250}]},
            {'name': 'CHICKEN CRISPY', 'category': 'chinese_nonveg_starter', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Dry', 'price': 240}, {'size': 'Gravy', 'price': 280}]},
            {'name': 'CHICKEN SCHEZWAN', 'category': 'chinese_nonveg_starter', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Dry', 'price': 240}, {'size': 'Gravy', 'price': 280}]},
            {'name': 'CHICKEN LOLLIPOP (8 PC)', 'category': 'chinese_nonveg_starter', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Dry', 'price': 240}, {'size': 'Gravy', 'price': 280}]},
            {'name': 'CHICKEN EMPTY', 'category': 'chinese_nonveg_starter', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Full', 'price': 210}]},
            {'name': 'CHICKEN WINGS', 'category': 'chinese_nonveg_starter', 'sub_category': 'dry',
             'sizes_and_prices': [{'size': 'Full', 'price': 200}]},
            {'name': 'PRAWNS HONEY CHILLI', 'category': 'chinese_nonveg_starter', 'sub_category': 'chilly',
             'sizes_and_prices': [{'size': 'Full', 'price': 300}]},
            {'name': 'CHICKEN MANCHOW', 'category': 'chinese_nonveg_starter', 'sub_category': 'manchurian',
             'sizes_and_prices': [{'size': 'Full', 'price': 200}]},
            {'name': 'GARLIC PEPPER SAUCE', 'category': 'chinese_nonveg_starter', 'sub_category': 'gravy',
             'sizes_and_prices': [{'size': 'Gravy', 'price': 240}]},
            {'name': 'CHILI PEPPER SAUCE', 'category': 'chinese_nonveg_starter', 'sub_category': 'gravy',
             'sizes_and_prices': [{'size': 'Gravy', 'price': 310}]},
            {'name': 'SCHEZWAN SAUCE', 'category': 'chinese_nonveg_starter', 'sub_category': 'gravy',
             'sizes_and_prices': [{'size': 'Gravy', 'price': 310}]},
            {'name': 'GREEN PEPPER SAUCE', 'category': 'chinese_nonveg_starter', 'sub_category': 'gravy',
             'sizes_and_prices': [{'size': 'Gravy', 'price': 320}]},
            
            # CHINESE NON-VEG TANDOORI STARTER
            {'name': 'CHICKEN TANDOORI', 'category': 'chinese_nonveg_tandoori', 'sub_category': 'tandoori',
             'sizes_and_prices': [{'size': 'Half', 'price': 250}, {'size': 'Full', 'price': 410}]},
            {'name': 'CHICKEN TIKKA', 'category': 'chinese_nonveg_tandoori', 'sub_category': 'chicken_tikka',
             'sizes_and_prices': [{'size': '6PC', 'price': 280}]},
            {'name': 'CHICKEN TANDOORI LOLLIPOP', 'category': 'chinese_nonveg_tandoori', 'sub_category': 'tandoori',
             'sizes_and_prices': [{'size': '6PC', 'price': 230}]},
            
            # CHINESE VEG TANDOORI STARTER
            {'name': 'SUFYANA PANEER TIKKA', 'category': 'chinese_veg_tandoori', 'sub_category': 'paneer_tikka',
             'sizes_and_prices': [{'size': '4PC', 'price': 300}]},
            {'name': 'PANEER MALAI TIKKA', 'category': 'chinese_veg_tandoori', 'sub_category': 'paneer_tikka',
             'sizes_and_prices': [{'size': '4PC', 'price': 330}]},
            {'name': 'PANEER TIKKA', 'category': 'chinese_veg_tandoori', 'sub_category': 'paneer_tikka',
             'sizes_and_prices': [{'size': '4PC', 'price': 270}]},
            {'name': 'MUSHROOM TANDOORI', 'category': 'chinese_veg_tandoori', 'sub_category': 'tandoori',
             'sizes_and_prices': [{'size': '4PC', 'price': 250}]},
            {'name': 'ALOO TANDOORI', 'category': 'chinese_veg_tandoori', 'sub_category': 'tandoori',
             'sizes_and_prices': [{'size': '10PC', 'price': 220}]},
            
            # BOMBIL SEA FOOD
            {'name': 'BOMBIL', 'category': 'bombil_seafood', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 180}]},
            {'name': 'MANDLI', 'category': 'bombil_seafood', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 180}]},
            {'name': 'BANGDA', 'category': 'bombil_seafood', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 180}]},
            {'name': 'RAWAS KOLWADA', 'category': 'bombil_seafood', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 190}]},
            {'name': 'SURMAI (AS PER MKT)', 'category': 'bombil_seafood', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 0}]},  # Price varies
            
            # GINGER
            {'name': 'CHICKEN MALAI TIKKA', 'category': 'ginger', 'sub_category': 'chicken',
             'sizes_and_prices': [{'size': '6PC', 'price': 330}]},
            {'name': 'CHICKEN PAHADI', 'category': 'ginger', 'sub_category': 'chicken',
             'sizes_and_prices': [{'size': '6PC', 'price': 300}]},
            {'name': 'CHICKEN SEEKH KABAB', 'category': 'ginger', 'sub_category': 'chicken',
             'sizes_and_prices': [{'size': '6PC', 'price': 330}]},
            {'name': 'CHICKEN POKARE KABAB', 'category': 'ginger', 'sub_category': 'chicken',
             'sizes_and_prices': [{'size': '6PC', 'price': 330}]},
            {'name': 'CHICKEN CHEESE MALAI TIKKA', 'category': 'ginger', 'sub_category': 'chicken',
             'sizes_and_prices': [{'size': '6PC', 'price': 370}]},
            {'name': 'CHICKEN GINGER', 'category': 'ginger', 'sub_category': 'chicken',
             'sizes_and_prices': [{'size': '6PC', 'price': 340}]},
            
            # FISH TANDOORI
            {'name': 'PRAWNS TANDOORI', 'category': 'fish_tandoori', 'sub_category': 'prawns',
             'sizes_and_prices': [{'size': '4PC', 'price': 330}]},
            {'name': 'POMFRET TANDOORI', 'category': 'fish_tandoori', 'sub_category': None,
             'sizes_and_prices': [{'size': '4PC', 'price': 300}]},
            {'name': 'POMFRET TANDOORI (AS PER MKT SIZE)', 'category': 'fish_tandoori', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 0}]},  # Price varies
            {'name': 'KALMI TANDOORI (AS PER MKT)', 'category': 'fish_tandoori', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 0}]},  # Price varies
            
            # QUICK BITES
            {'name': 'BOILED EGG (2PC)', 'category': 'quick_bites', 'sub_category': 'egg',
             'sizes_and_prices': [{'size': 'Full', 'price': 60}]},
            {'name': 'EGG BHURJI (2PC)', 'category': 'quick_bites', 'sub_category': 'egg',
             'sizes_and_prices': [{'size': 'Full', 'price': 100}]},
            {'name': 'EGG FRY (2PC)', 'category': 'quick_bites', 'sub_category': 'egg',
             'sizes_and_prices': [{'size': 'Full', 'price': 80}]},
            {'name': 'EGG PAKODA (2PC)', 'category': 'quick_bites', 'sub_category': 'egg',
             'sizes_and_prices': [{'size': 'Full', 'price': 140}]},
            {'name': 'EGG CHEESE PAKODA (2PC)', 'category': 'quick_bites', 'sub_category': 'egg',
             'sizes_and_prices': [{'size': 'Full', 'price': 160}]},
            
            # CHINESE VEG RICE
            {'name': 'FRIED RICE', 'category': 'chinese_veg_rice', 'sub_category': 'fried_rice',
             'sizes_and_prices': [{'size': 'Veg', 'price': 170}, {'size': 'Mushroom', 'price': 200}, {'size': 'Paneer', 'price': 230}]},
            {'name': 'SCHEZWAN FRIED RICE', 'category': 'chinese_veg_rice', 'sub_category': 'schezwan_rice',
             'sizes_and_prices': [{'size': 'Veg', 'price': 200}, {'size': 'Mushroom', 'price': 230}, {'size': 'Paneer', 'price': 240}]},
            {'name': 'TRIPLE SCHEZWAN FRIED RICE', 'category': 'chinese_veg_rice', 'sub_category': 'triple_schezwan',
             'sizes_and_prices': [{'size': 'Veg', 'price': 210}, {'size': 'Mushroom', 'price': 240}, {'size': 'Paneer', 'price': 270}]},
            {'name': 'MANCHURIAN FRIED RICE', 'category': 'chinese_veg_rice', 'sub_category': 'manchurian_rice',
             'sizes_and_prices': [{'size': 'Veg', 'price': 230}, {'size': 'Mushroom', 'price': 240}, {'size': 'Paneer', 'price': 270}]},
            {'name': 'GREEN PEPPER FRIED RICE', 'category': 'chinese_veg_rice', 'sub_category': 'fried_rice',
             'sizes_and_prices': [{'size': 'Veg', 'price': 220}, {'size': 'Mushroom', 'price': 230}, {'size': 'Paneer', 'price': 280}]},
            {'name': 'BURNT GARLIC FRIED RICE', 'category': 'chinese_veg_rice', 'sub_category': 'burnt_garlic',
             'sizes_and_prices': [{'size': 'Veg', 'price': 220}, {'size': 'Mushroom', 'price': 230}, {'size': 'Paneer', 'price': 280}]},
            
            # CHINESE VEG NOODLES
            {'name': 'HAKKA NOODLES', 'category': 'chinese_veg_noodles', 'sub_category': 'hakka_noodles',
             'sizes_and_prices': [{'size': 'Veg', 'price': 170}, {'size': 'Mushroom', 'price': 200}, {'size': 'Paneer', 'price': 230}]},
            {'name': 'SCHEZWAN NOODLES', 'category': 'chinese_veg_noodles', 'sub_category': 'schezwan_noodles',
             'sizes_and_prices': [{'size': 'Veg', 'price': 190}, {'size': 'Mushroom', 'price': 220}, {'size': 'Paneer', 'price': 230}]},
            {'name': 'TRIPLE SCHEZWAN NOODLES', 'category': 'chinese_veg_noodles', 'sub_category': 'triple_schezwan_noodles',
             'sizes_and_prices': [{'size': 'Veg', 'price': 200}, {'size': 'Mushroom', 'price': 230}, {'size': 'Paneer', 'price': 310}]},
            {'name': 'MANCHURIAN NOODLES', 'category': 'chinese_veg_noodles', 'sub_category': 'manchurian_noodles',
             'sizes_and_prices': [{'size': 'Veg', 'price': 210}, {'size': 'Mushroom', 'price': 240}, {'size': 'Paneer', 'price': 270}]},
            {'name': 'CHEESE PEPPER NOODLES', 'category': 'chinese_veg_noodles', 'sub_category': 'cheese_noodles',
             'sizes_and_prices': [{'size': 'Veg', 'price': 220}, {'size': 'Mushroom', 'price': 240}, {'size': 'Paneer', 'price': 280}]},
            {'name': 'BURNT GARLIC NOODLES', 'category': 'chinese_veg_noodles', 'sub_category': 'burnt_garlic',
             'sizes_and_prices': [{'size': 'Veg', 'price': 220}, {'size': 'Mushroom', 'price': 230}, {'size': 'Paneer', 'price': 280}]},
            
            # CHINESE NON-VEG RICE
            {'name': 'EGG RICE', 'category': 'chinese_nonveg_rice', 'sub_category': 'egg',
             'sizes_and_prices': [{'size': 'Chick', 'price': 190}, {'size': 'Egg', 'price': 170}, {'size': 'Prawns', 'price': 240}]},
            {'name': 'SCHEZWAN FRIED RICE', 'category': 'chinese_nonveg_rice', 'sub_category': 'schezwan_rice',
             'sizes_and_prices': [{'size': 'Chick', 'price': 220}, {'size': 'Egg', 'price': 200}, {'size': 'Prawns', 'price': 310}]},
            {'name': 'TRIPLE SCHEZWAN FRIED RICE', 'category': 'chinese_nonveg_rice', 'sub_category': 'triple_schezwan',
             'sizes_and_prices': [{'size': 'Chick', 'price': 230}, {'size': 'Egg', 'price': 210}, {'size': 'Prawns', 'price': 320}]},
            {'name': 'MANCHURIAN FRIED RICE', 'category': 'chinese_nonveg_rice', 'sub_category': 'manchurian_rice',
             'sizes_and_prices': [{'size': 'Chick', 'price': 230}, {'size': 'Egg', 'price': 210}, {'size': 'Prawns', 'price': 320}]},
            {'name': 'GREEN PEPPER FRIED RICE', 'category': 'chinese_nonveg_rice', 'sub_category': 'fried_rice',
             'sizes_and_prices': [{'size': 'Chick', 'price': 250}, {'size': 'Egg', 'price': 230}, {'size': 'Prawns', 'price': 340}]},
            {'name': 'BURNT GARLIC FRIED RICE', 'category': 'chinese_nonveg_rice', 'sub_category': 'burnt_garlic',
             'sizes_and_prices': [{'size': 'Chick', 'price': 250}, {'size': 'Egg', 'price': 230}, {'size': 'Prawns', 'price': 340}]},
            
            # CHINESE NON-VEG NOODLES
            {'name': 'HAKKA NOODLES', 'category': 'chinese_nonveg_noodles', 'sub_category': 'hakka_noodles',
             'sizes_and_prices': [{'size': 'Chick', 'price': 190}, {'size': 'Egg', 'price': 170}, {'size': 'Prawns', 'price': 240}]},
            {'name': 'SCHEZWAN NOODLES', 'category': 'chinese_nonveg_noodles', 'sub_category': 'schezwan_noodles',
             'sizes_and_prices': [{'size': 'Chick', 'price': 200}, {'size': 'Egg', 'price': 200}, {'size': 'Prawns', 'price': 310}]},
            {'name': 'TRIPLE SCHEZWAN NOODLES', 'category': 'chinese_nonveg_noodles', 'sub_category': 'triple_schezwan_noodles',
             'sizes_and_prices': [{'size': 'Chick', 'price': 220}, {'size': 'Egg', 'price': 200}, {'size': 'Prawns', 'price': 310}]},
            {'name': 'MANCHURIAN NOODLES', 'category': 'chinese_nonveg_noodles', 'sub_category': 'manchurian_noodles',
             'sizes_and_prices': [{'size': 'Chick', 'price': 210}, {'size': 'Egg', 'price': 240}, {'size': 'Prawns', 'price': 270}]},
            {'name': 'CHEESE PEPPER NOODLES', 'category': 'chinese_nonveg_noodles', 'sub_category': 'cheese_noodles',
             'sizes_and_prices': [{'size': 'Chick', 'price': 220}, {'size': 'Egg', 'price': 240}, {'size': 'Prawns', 'price': 280}]},
            {'name': 'BURNT GARLIC NOODLES', 'category': 'chinese_nonveg_noodles', 'sub_category': 'burnt_garlic',
             'sizes_and_prices': [{'size': 'Chick', 'price': 220}, {'size': 'Egg', 'price': 230}, {'size': 'Prawns', 'price': 280}]},
            
            # VEG - INDIAN MAIN COURSE
            {'name': 'DAL FRY', 'category': 'veg_indian_main', 'sub_category': 'dal',
             'sizes_and_prices': [{'size': 'Full', 'price': 160}]},
            {'name': 'DAL TADKA', 'category': 'veg_indian_main', 'sub_category': 'dal',
             'sizes_and_prices': [{'size': 'Full', 'price': 180}]},
            {'name': 'DAL MAKHANI', 'category': 'veg_indian_main', 'sub_category': 'dal',
             'sizes_and_prices': [{'size': 'Full', 'price': 230}]},
            
            # VEGETABLE
            {'name': 'CHANA MASALA', 'category': 'vegetable', 'sub_category': 'masala',
             'sizes_and_prices': [{'size': 'Full', 'price': 200}]},
            {'name': 'VEG KADHAI', 'category': 'vegetable', 'sub_category': 'curry',
             'sizes_and_prices': [{'size': 'Full', 'price': 220}]},
            {'name': 'VEG KOLHAPURI', 'category': 'vegetable', 'sub_category': 'curry',
             'sizes_and_prices': [{'size': 'Full', 'price': 220}]},
            {'name': 'VEG JAIPURI', 'category': 'vegetable', 'sub_category': 'curry',
             'sizes_and_prices': [{'size': 'Full', 'price': 220}]},
            {'name': 'BHINDI FRY MASALA', 'category': 'vegetable', 'sub_category': 'masala',
             'sizes_and_prices': [{'size': 'Full', 'price': 220}]},
            {'name': 'BHINDI FRY', 'category': 'vegetable', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': 'Full', 'price': 230}]},
            {'name': 'VEG HANDI', 'category': 'vegetable', 'sub_category': 'curry',
             'sizes_and_prices': [{'size': 'Full', 'price': 220}]},
            {'name': 'VEG KORMA', 'category': 'vegetable', 'sub_category': 'curry',
             'sizes_and_prices': [{'size': 'Full', 'price': 270}]},
            {'name': 'MUSHROOM MASALA', 'category': 'vegetable', 'sub_category': 'masala',
             'sizes_and_prices': [{'size': 'Full', 'price': 220}]},
            
            # DUM
            {'name': 'DUM ALOO', 'category': 'dum', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 270}]},
            {'name': 'ALOO MUTTER', 'category': 'dum', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 200}]},
            {'name': 'ALOO MUTTER', 'category': 'dum', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 200}]},
            {'name': 'ALOO GOBI MASALA', 'category': 'dum', 'sub_category': None,
             'sizes_and_prices': [{'size': 'Full', 'price': 200}]},
            
            # PANEER
            {'name': 'SHAHI PANEER', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 280}]},
            {'name': 'PANEER LABABDAAR', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 330}]},
            {'name': 'PANEER TIKKA MASALA', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 280}]},
            {'name': 'PANEER BUTTER MASALA', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 300}]},
            {'name': 'KAJU PANEER MASALA (4PCS)', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 330}]},
            {'name': 'PANEER TIKKA MASALA (4PCS)', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 350}]},
            {'name': 'PANEER KADHAI', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 300}]},
            {'name': 'PANEER PALAK', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 260}]},
            {'name': 'PANEER MUSHROOM MASALA', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 300}]},
            {'name': 'PANEER KOLHAPURI', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 300}]},
            {'name': 'PANEER MUTTER', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 300}]},
            {'name': 'PANEER PASANDA', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 280}]},
            {'name': 'PANEER DO PATAKA', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 290}]},
            
            # Additional items from menu card
            {'name': 'GOBI KEEMA MUTTER', 'category': 'vegetable', 'sub_category': 'curry',
             'sizes_and_prices': [{'size': 'Full', 'price': 230}]},
            {'name': 'BHINDI FRY', 'category': 'vegetable', 'sub_category': 'fry',
             'sizes_and_prices': [{'size': 'Full', 'price': 220}]},
            {'name': 'PANEER BHURJI', 'category': 'paneer', 'sub_category': 'paneer_dishes',
             'sizes_and_prices': [{'size': 'Full', 'price': 300}]},
            
            # CHINESE NON-VEG NOODLES (Hakka Noodles variations)
            {'name': 'HAKKA NOODLES', 'category': 'chinese_nonveg_noodles', 'sub_category': 'hakka_noodles',
             'sizes_and_prices': [{'size': 'Chicken', 'price': 190}, {'size': 'Egg', 'price': 170}, {'size': 'Prawns', 'price': 280}]},
            {'name': 'SCHEZWAN NOODLES', 'category': 'chinese_nonveg_noodles', 'sub_category': 'schezwan_noodles',
             'sizes_and_prices': [{'size': 'Chicken', 'price': 220}, {'size': 'Egg', 'price': 200}, {'size': 'Prawns', 'price': 310}]},
            {'name': 'TRIPLE SCHEZWAN NOODLES', 'category': 'chinese_nonveg_noodles', 'sub_category': 'triple_schezwan_noodles',
             'sizes_and_prices': [{'size': 'Chicken', 'price': 200}, {'size': 'Egg', 'price': 230}, {'size': 'Prawns', 'price': 310}]},
        ]
