class Storage:
    pass


class PharmacyWarehouse:

    def __init__(self, name: str, series: str, manufacturer: str, price: float):
        self.name = name
        self.series = series
        self.manufacturer = manufacturer
        self.price = price

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


omez = Drugs("Омез капсулы 20мг N30", '12092022', "Др. Редди`с/Индия, Несвижский ЗМП, Беларусь", 15.98,
             'A02BC01', 'Omeprazole', '12092025')
print(omez)
tonometer = MedicalDevices('Microlife BP A3 плюс тонометр автоматический N1', '3214621', 'Микролайф АГ, Швейцария',
                           197.01, '3 года')
print(tonometer)
pacifier = PharmacyRangeGoods('Соска антиколиковая NUK ортодонтической формы из латекса размер М First Choice Plus',
                              '986532ABC23', 'NUK, Германия', 11.90, 'BY/112 01.01 1070045')
print(pacifier)
