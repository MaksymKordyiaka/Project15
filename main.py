'''
1.Дано клас, при створенні об’єкту якого відбувається перевірка переданого атрибуту
(передбачено тільки один атрибут об’єкту) але на перевірку передається три.

В якості атрибуту може виступати тільки стрічка, при цьому цифра записана у форматі
«str» не вважається стрічкою. Якщо жоден з аргументів не відповідає вказаним
вимогам- викликаємо помилку типів. Реалізація- через @staticmethod.

2.Дано словник, ключами якого є кортежі та стрічки, а значеннями- списки з двох
елементів (один з яких є стрічкою, інший- цифрою).

Створити список з об’єктів класу, в якості яких можуть виступати ключі словника
(за умови, що це стрічка), а в якості атрибутів об’єкту- використовуємо стрічку
зі значення ключа. Реалізація- через @classmethod.
'''


class MyClass:
    def __init__(self, attribute):
        self.attribute = attribute

    @staticmethod
    def check_attribute(attribute):
        if not isinstance(attribute, str):
            raise TypeError("Атрибут повинен бути стрічкою")
        elif attribute.isdigit():
            raise TypeError("Атрибут не може бути цифрою у форматі 'str'")

    @classmethod
    def create_objects(cls, dictionary):
        objects = []
        for key in dictionary.keys():
            if isinstance(key, str):
                attribute = str(key)
                objects.append(cls(attribute))
        return objects

dictionary = {("key1",): ["value1", 1],
              "key2": ["value2", 2],
              123: ["value3", 3]}

objects_list = MyClass.create_objects(dictionary)
print(objects_list)