#I love the fact that List comprehensions are much more simplified than using the filter function.


items = [
    ("Waffles" , 5),
    ("Pancakes" , 7),
    ("Blueberries" , 3),
    ("Cake" , 2),
    ("Protein Shake" , 9),
    ("Tomahawk Steak" , 109),

]

prices = [item[1] for item in items]
print(prices)
