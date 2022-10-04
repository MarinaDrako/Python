class StorageError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class AddStorageError(StorageError):
    def __init__(self, txt):
        self.txt = f"Невозможно добавить товар на склад:\n {txt}"


class TransferStorageError(StorageError):
    def __init__(self, txt):
        self.txt = f"Ошибка прередачи товара:\n {txt}"


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "PharmacyWarehouse"):
        if not isinstance(item, PharmacyWarehouse):
            raise AddStorageError(f"{item} не аптечный товар")

        self.__storage.append(item)

    def transfer(self, i: int, department: str):
        if not isinstance(i, int):
            raise TransferStorageError(f"Для перемещения товара укажите номер позиции этого товара на складе")

        item: PharmacyWarehouse = self.__storage[i]

        if item.department:
            raise TransferStorageError(f"Товар {item} уже отправлен в отдел {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for ind, item in enumerate(self):
            i: PharmacyWarehouse = item
            if all([i.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield ind, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"На складе сейчас товаров: {len(self.__storage)}"


class PharmacyWarehouse:

    def __init__(self, name: str, series: str, manufacturer: str, price: float):
        self.name = name
        self.series = series
        self.manufacturer = manufacturer
        self.price = price

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f'Наименование товара: {self.name} Серия: {self.series} ' \
               f'Производитель, страна производства: {self.manufacturer} Цена за единицу(BYN): {self.price}'


class Drugs(PharmacyWarehouse):
    def __init__(self, name, series, manufacturer, price, atc, inn, best_before_day):
        super().__init__(name, series, manufacturer, price)
        self.atc = atc
        self.inn = inn
        self.best_before_day = best_before_day

    def __str__(self):
        return 'Лекарственный препарат: ' + PharmacyWarehouse.__str__(self) + \
               ' Классификация АТХ: ' + str(self.atc) + \
               ' Международное непатентованное наименование: ' + str(self.inn) + \
               ' Срок годности: ' + str(self.best_before_day)


class MedicalDevices(PharmacyWarehouse):
    def __init__(self, name, series, manufacturer, price, garantee_period):
        super().__init__(name, series, manufacturer, price)
        self.garantee_period = garantee_period

    def __str__(self):
        return 'Медицинское изделие: ' + PharmacyWarehouse.__str__(self) + \
               ' Гарантийный срок: ' + str(self.garantee_period)


class PharmacyRangeGoods(PharmacyWarehouse):
    def __init__(self, name, series, manufacturer, price, quality_certificate):
        super().__init__(name, series, manufacturer, price)
        self.quality_certificate = quality_certificate

    def __str__(self):
        return 'Товар аптечного ассортимента: ' + PharmacyWarehouse.__str__(self) + \
               ' Сертификат качества: ' + str(self.quality_certificate)


storage = Storage()
storage.add(Drugs("Предуктал МВ таблетки покрытые оболочкой ретард 35мг N60", "031219", "Сервье, Франция",
                  115.28, "C01EB15", 'Trimetazidine', '03122023'))
storage.add(MedicalDevices("Грелка резиновая 2л", "22", "ООО Киевгума, Украина", 11.03, '1 год'))
storage.add(PharmacyRangeGoods("БАД Черника форте с лютеином таблетки 250мг N50", "3615AS", "Эвалар, Россия", 7.20,
                               'BY 01.01 2122310'))
print(storage)

last_index = None
for index, itm in storage.filter_by(department=None):
    print(index, itm)
    last_index = index

print("Из приемного отдела передаем 1 позицию товара")

storage.transfer(last_index, '13 отдел - косметика')

for index, itm in storage.filter_by(department=None):
    print(index, itm)

print(storage)
print("Передали 1 позицию товара, из приемного отдела позицию можно удалить")
del storage[last_index]
print(storage)
