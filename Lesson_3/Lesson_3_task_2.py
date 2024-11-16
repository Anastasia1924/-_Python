from smartphone import Smartphone
catalog = [
    Smartphone("Samsung", "Galaxy A14", "+79174562352"),
    Smartphone("Samsung", "Galaxy Z flip6", "+79245635465"),
    Smartphone("Samsung", "Galaxy S24+", "+79379879878"),
    Smartphone("Sony", "Xperia 10V", "+79517777777"),
    Smartphone("Xiaomi", "14T Pro", "+79037898989")
]
for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. "{smartphone.number}".')