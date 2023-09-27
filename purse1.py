class Purse:

    # метод-конструктор исполняет свой код,
    # во время создания объекта класс x = Purse() изначально.
    def __init__(self, valuta, name='Unknown'):
        if valuta not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00  # инкапсуляция __данных (защита)
        self.valuta = valuta
        self.name = name

    # метод пополнения кошелька
    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    # метод списания с кошелька
    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print('Не достаточно средств')
            raise ValueError('Не достаточно средств')
        self.__money = self.__money - howmany
        return howmany

    def info(self):
        print(self.__money, self.valuta, self.name)

    # метод-ДЕструктор
    # def __del__(self):
    #     print('Кошелек удален')


x = Purse('USD', 'Michael')
y = Purse('USD')
x.top_up_balance(int(input()))
y.top_up_balance(int(input()))
y.top_up_balance(x.top_down_balance(7))
x.info()
y.info()
x.top_up_balance(int(input()))
x.info()
y.info()
