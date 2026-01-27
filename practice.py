

def yandex_taxi():
    whether =input("whats whether like today?(rain/sun/snow): ")
    user=input("where we going?")
    location =["city","mardakan","sea breaze"]
    price = 5
    if user in location and whether == "rain":
        price *= 5
    if user in location and whether == "sun":
        price *= 2.5
    if user in location and whether == "snow":
        price *= 10
    return f"you  price is {price} you agree?"

print(yandex_taxi())
