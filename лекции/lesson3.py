from user import User
from card import Card

amanda = User("Amanda")

amanda.sayName()
amanda.setAge(33)
amanda.sayAge()

card = Card("3335 3335 3335 3335", 11/28, "Amanda R")
amanda.addCard(card)
amanda.getCard().pay(1000)

