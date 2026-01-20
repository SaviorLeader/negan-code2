                                                                                                         
import random

def found_average(*args,**kwargs):
    name = kwargs.get("name","fara")
    gifts =["iphone 17","iphone 17 pro","iphone 17 pro max","iphone 17 air"]
    if args:
        average = sum(args)/len(args)
    if average >= 30:
        gifts = random.choice(gifts)
    return f"{name} your total {average} and you won {gifts}"
print(found_average(30,40,60, name="fara"))


