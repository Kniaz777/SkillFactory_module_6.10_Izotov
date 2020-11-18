class Corporative:
    def __init__(self, name, soname, adress, status):
        self.name = name
        self.soname = soname
        self.adress = adress
        self.status = status

    def __str__(self):
        return 'Имя: "{0} {1}", г. "{2}", Статус: "{3}"'.format(self.name, self.soname, self.adress, self.status)

vol_1 = Corporative('Иван', 'Петров', 'Москва', 'наставник')
vol_2 = Corporative('Жорик', 'Вартанов', 'Пятигорск', 'падаван')
vol_3 = Corporative('Снежанна', 'Денисова', 'Омск', 'неизвестен')


print(vol_1)
print(vol_2)
print(vol_3)