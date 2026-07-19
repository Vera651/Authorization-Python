rate = input("оцените работу оператора от 1 до 5")
rate_as_number = int(rate)

print(rate_as_number)

if(rate_as_number<1):
    rate_as_number = 1

if(rate_as_number>5):
    rate_as_number = 5

print(rate_as_number)

feedback = ""

if rate_as_number ==1:
    feedback = input("что улучшить?")
elif rate_as_number == 2:
    feedback = input("расскажите, что вас смутило?")
elif rate_as_number == 3:
    feedback = input("что не так?")
elif rate_as_number == 4:
    feedback = input("как можно стать лучше?")
else:
    feedback = input("Спасибки!")

print(feedback)
