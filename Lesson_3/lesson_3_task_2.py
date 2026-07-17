from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 17", "+79094550099"),
    Smartphone("Samsung", "Galaxy S", "+79184554300"),
    Smartphone("Xiaomi", "Redmi Note 14", "+79180065535"),
    Smartphone("Honor", "X5d Plus", "+79558976543"),
    Smartphone("Nokia", "3310", "+79282280133")
]

for smartphone in catalog:
    print(f"{smartphone.phone_mark} - {smartphone.phone_model}. {smartphone.phone_number}")