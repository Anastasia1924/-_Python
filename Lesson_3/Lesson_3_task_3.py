from address import Address
from mailing import Mailing

address_to = Address("432064", "г. Ульяновск", "ул. Ленина", "д. 10", "кв. 12")
address_from = Address("555555", "г. Сочи", "ул. Фруктовая", "д. 25", "кв. 10")

track = Mailing(address_to, address_from, "1500,00", "CA123466789RU")

print(track)