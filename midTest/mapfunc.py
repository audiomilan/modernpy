#Learning how to use map functions

items = [
    ("Cieba Macho" , 21),
    ("Vencedor", 7),
    ("Anamu" ,    6),
    ("Rompe Camisa" , 9),
]

prices = list(map(lambda item: item[1] , items))
print(prices)
