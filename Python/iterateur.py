#coding:utf-8
""" --------------------------------------------------------
class R:
        def __init__(self, end):
            if end <=0:
                raise ValueError("Point d'arrêt de l'intervalle invalide")
            self.current = 0
            self.end = end 

        def __iter__(self):
            return self 

        def __next__(self):
                self.current +=1

                if self.current > self.end:
                    raise StopIteration

                return self.current - 1

ran = R(5)

for v in ran:
    print(v)
""" 
class Inventory:
        def __init__(self, name):
            self.name = name
            self.content = []

        def __iter__(self):
            return iter(self.content)

        def __next__(self):
            return next(self.content)

        def add(self, item):
            self.content.append(item)
    
chest = Inventory("Large malle")

chest.add("Epée en bois")
chest.add("Potion de soins mineurs")
chest.add("Marque d'honneur")

for item in chest:
    print(item)





