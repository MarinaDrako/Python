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
        self.txt = f"Ошибка прередачи товарв:\n {txt}"


class ValidPharmacyWarehouseError(StorageError):
    pass


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, products):
        if not all([isinstance(product, PharmacyWarehouse) for product in products]):
            raise AddStorageError(f"Вы пытаетесь принять на аптечный склад неподходящие товары")

        self.__storage.append(products)

    def transfer(self, i: int, department: str):
        if not isinstance(i, int):
            raise TransferStorageError(f"Для перемещения товара укажите номер позиции этого товара на складе")

        item: PharmacyWarehouse = self.__storage[i]

        if item.department:
            raise TransferStorageError(f"Товар {item} уже отправлен в отдел {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for ind, item in enumerate(self):
            ind: PharmacyWarehouse = item
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
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
    __main_parameters = ('name', 'series', 'manufacturer', 'price')

    value_added_tax = 0.2
    wholesale_markup = 0.05
    retail_allowance = 0.1

    def __init__(self, name: str, series: str, manufacturer: str, price: float):
        self.name = name
        self.series = series
        self.manufacturer = manufacturer
        self.price = price

        self.department = None

    @property
    def wholesale_price(self):
        return self.price * (1 + self.value_added_tax) * (1 + self.wholesale_markup)

    @property
    def retail_price(self):
        return self.wholesale_price * (1 + self.retail_allowance)

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __setattr__(self, key, value):
        if key in self.__main_parameters and not value:
            raise AttributeError(f"'{key}' должен иметь значение отличное от false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f'Наименование товара: {self.name} Серия: {self.series} ' \
               f'Производитель, страна производства: {self.manufacturer} Цена за единицу(BYN): {self.price}'

    @staticmethod
    def validate(quantity):
        if not isinstance(quantity, int):
            ValidPharmacyWarehouseError(f"'{type(quantity)}'; количество экземпляров должно быть целым числом и "
                                        f"принадлежать классу 'int'")

    @classmethod
    def create(cls, quantity, **kwargs):
        cls.validate(quantity)
        return [cls(**kwargs) for _ in range(quantity)]


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
storage.add(Drugs.create(1000, name="Гелисал сироп 100мл N1", series="56A1236B",
                         manufacturer="Медана Фарма С.А., Польша", price=7.90,
                         atc='R05CA', inn='Expectorants', best_before_day='20102024'))
storage.add(MedicalDevices.create(50, name="Omron comp AIR С28 NE С28 E ингалятор компрессорный N1",
                                  series="123B", manufacturer="Омрон Хэлскэр Лтд., Япония ",
                                  price=234.05, garantee_period='5 лет'))
storage.add(PharmacyRangeGoods.create(100, name="Гигиеническая помада с защитой SPF 20 гигиеническая помада 4г N1",
                                      series="251121", manufacturer="ООО Лаборатория Бабе, Испания ",
                                      price=17.15, quality_certificate='BY 05.01 1154620'))

print(storage)
