class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale / exhale")
class fish(Animal):#it will inherit the properties of the class Animal
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("doing this underwater")
    def swin(self):
        print("Moving in the water")

nemo = fish()
nemo.swin()
nemo.breathe()
print(nemo.num_eyes)

