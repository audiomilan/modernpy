items = [
    ("Shirt" , 15),
    ("Pants" , 19),
    ("Accessories" , 6),
    ("Shoes" , 32),

]

filtered = list(filter(lambda item: item[1] >= 15 , items))
print(filtered)
