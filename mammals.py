class Mammals:
    def __init__(self,sound,digits) -> None:
        self.class_name = "Mammals"
        self.sound = sound
        self.digits = digits
        self.breast_feed = True

    def __repr__(self) -> str:
        return f"Class {self.class_name} , sound = {self.sound} , digits = {self.digits}, breast_feed = {self.breast_feed}"

class Dogs(Mammals):
    def __init__(self):
        super().__init__(sound = 'Bark',digits = 'Paws')
        self.class_name = "Dogs"       

class Cats(Mammals):
    def __init__(self):
        super().__init__(sound='Meow',digits='Retractable claws')
        self.class_name = "Cats"


cat = Cats()
dog = Dogs()

print(cat)
print(dog)