from .models import Product
from random import randrange

def insert_product(db):
    names = ['M-TV Hoodie', 'Spongebob Hoodie', 'Simpsons Hoodie', 'MCMXLVII Hoodie', 'UCLA Hoodie', 'Star Wars Hoodie',
             'Fantasia Hoodie', 'North Ocean Hoodie', 'NASA Hoodie', 'Disney Hoodie - Brown', 'Hope Hoodie', 'Hogwarts Hoodie',
             'Casual Hoodie - Black', 'Disney Hoodie - Baby Blue', 'Casual Hoodie - Beige', 'Casual Hoodie - Grey',
             'NYC Hoodie', 'Neon Hoodie', 'Disney Hoodie - Emerald', 'Le Weekend Hoodie', 'Marvel Hoodie', 'Squidward Hoodie']

    price = [299000 for x in range(22)]

    stock = [randrange(30) for x in range(22)]

    discount = [0 for x in range(22)]
    discount[4] = 25

    img = []
    for i in range(22):
        img.append('../static/images/hood-' + str(i+1))

    products = []

    for i in range(22):
        products.append(Product(name=names[i], price=price[i], stock=stock[i], discount=discount[i], img=img[i]))

    return products