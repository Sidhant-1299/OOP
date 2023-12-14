class Parent:
    def __init__(self) -> None:
        self.species = 'Human'
        self.name = 'Parent'
        self.group = 'Adult'
    def __str__(self) -> str:
        return f"SPECIES = {self.species} NAME = {self.name} GROUP = {self.group}"
    
class Child(Parent):
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        self.group = "Children"
        self.name = "Child"

c = Child()
print(c)
