from address import Address
from mailing import Mailing

to_address = Address("3587", "Санкт-Петербург", "Невский проспект", "1", "1")
from_address = Address("1234", "Краснодар", "Красная улица", "10", "5")
mailing = Mailing(to_address, from_address, 1000, "3587")

print(mailing)