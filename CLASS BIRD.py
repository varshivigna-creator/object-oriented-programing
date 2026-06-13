class parrot:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

blu=parrot("blu",2)
woo=parrot("woo",5)

print("blue is",format(blu.species))          
print("woo is ",format(woo.species))

print(blu.name,blu.age)
print(woo.name,woo.age)