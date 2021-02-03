
class Character:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Character, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.race = 'Elf'

if __name__ == '__main__':
    s = Character()
    print(s.race)
    d = Character()
    d.race = 'Ork'
    print(s.race)
    print(d.race)



# class Singleton:
#
#     _instance = None
#     def __init__(self):
#         if not Singleton._instance:
#             print('__init__ method called')
#         else:
#             print('Instance is already created:', self.getInstance())
#
#     @classmethod
#     def getInstance(cls):
#         if not cls._instance:
#             cls._instance = Singleton()
#         return cls._instance
#
# s = Singleton()
# print("Object created", Singleton.getInstance())
# s1 = Singleton()
