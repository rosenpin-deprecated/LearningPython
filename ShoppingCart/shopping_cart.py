from string import Template

cart = []
cart.append(dict(item="Fish", price=15, qty=3))
cart.append(dict(item="Banana", price=6, qty=3))
cart.append(dict(item="Powder", price=112, qty=5))
t = Template("$item costs $price$$ for $qty")
total = 0
for item in cart:
    print(t.substitute(item))
    total += item["price"]
