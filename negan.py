import random
students =[["nicaaaat",200],["broshka",380],["araaa",100],["fara",220],["abdulah",100]]
gifts =["iphone 17","iphone 17 pro","iphone 17 pro max"]
university1= "baku state university"
university2= "azmiu"
university3= "aztu"
for student in students: 
    if student[1] >= 350:
        gifts = random.choice(gifts)
        print("congrulations",student[0],"you got into",university3,"and you won",gifts)
    elif student[1] >= 200:
        print("congrulations",student[0],"you got into",university1)
    elif student[1] >= 210:
        print("congrulations",student[0],"you got into",university2)
    else:
        print("sen getdin bloka",student[0])
