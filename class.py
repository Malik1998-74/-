# # class Point:
# #     x = 0
# #     y = 0

# #     def coordinates(self):
# #         print(f'Координаты: x {self.x}, y {self.y}')  # аргумент self, с помощью которого мы можем получать доступ к другим атрибутам и методам.
# class Point:
#     def __init__(self, x, y):  # __init__ конструкция для передачи параметров
#         self.x = x
#         self.y = y
#     def coordinates(self):
#         print(f'coordinates are: {self.x}, {self.y}')
    

#     def __repr__(self):
#         return f'<Point x: {self.x}, y: {self.y}'

    


# my_point = Point(1, 3)
# # print(my_point.x)  #обращаемся  к атрибуту Х
# # my_point.coordinates()
# print(my_point)
# my_point.x = 10  # меняем значения Х
# my_point.y = -5
# my_point.coordinates()
class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Наззванный товар должен быть больше 2-х символов') #создаем искуственную ошибку 
        self.price = abs(float(price))
        self.stock = abs(float(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError ('Слишком больша яскидка')  #создаем искуственную ошибку
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def discounted(self):
        return self.price - self.price * self.discount / 100

    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        # Здесь мы можем как-то взаимодействовать с учетной/бухгалтерской системой
        self.stock -= items_count

    def get_color(self):
        raise NotImplementedError  # Метод не реализован для основного класс для наследовании


    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>'

# product1 = Product('ТОвар', 100, stock=10)
# product1.sell(5)
# print(product1)

class Phone(Product):
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)  # Из наследника можно получить доступ к оригинальным методам класса-родителя через вызов super()
        self.color = color
    
    def get_color(self):  #функция для вывода цвета
        return f'Цвет корпуса: {self.color}'

    def get_memory_size(self):  # for memory
        pass

    def __repr__(self):
         return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'


class Sofa(Product):
    def __init__(self, name, price, color, texture, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.texture = texture

    def get_color(self):
        return f'цвет дивана: {self.color}, материал {self.texture}'

    def __repr__(self):
         return f'<Sofa name: {self.name}, price: {self.price}, stock: {self.stock}>'


my_phone = Phone('iPhone', 60000, 'black')
# print(my_phone)
# print(my_phone.color)
print(my_phone.get_color())
        
sofa1 = Sofa('big sofa', 23000, 'white', 'velours')
# print(sofa1)
# print(sofa1.color)
# print(sofa1.texture)
print(sofa1.get_color())
# print(sofa1.get_)

# Памятка
# Название классов пишется в одно слово, каждое слово с большой буквы: Flask или MessageHandler
# Методы и атрибуты вызываются через точку
# Инкапсуляция - все необходимое для работы класс содержит в себе
# Наследование - мы наследуем функционал родителя, переопределяем только то, что нужно. И добавляем то, чего в родительском классе не было
# Полиморфизм - одинаковые методы разных классов могут работать по-разному
