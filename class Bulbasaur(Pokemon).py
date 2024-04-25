class Pokemon:  # use a capital letter for class name
    def __init__(self):
        """A special method (function) called the
        Constructor. Contains all the properties/variables
        that describe a Pokemon."""
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "normal"
        self.actual_cry = "Roooooooooooooar!"

        print("A new Pokémon is born!")

    def cry(self) -> str:
        """Represents the sound a Pokemon makes

        Returns:
           - string representing the sound it makes"""
        return f'{self.name} says, "{self.actual_cry}"!'

    def eat(self, food: str) -> str:
        """Represents feeding the Pokemon

        Params:
            - food: what food you feed it

        Return:
            - what it says after eating it"""
        if food.lower() == "berry":
            return f'{self.name} ate the berry and says, "YUM!"'
        elif food.lower() == "potion":
            return f"{self.name} consumed the potion and feels healthier!"
        else:
            return f"{self.name} batted the {food} away."

class Bulbasaur(Pokemon):
    def __init__(self, name ="Bulbasaur") :
        super().__init__()

        self.name = name
        self.id=1
        self.type="Grass"
        self.actual_cry = "Roarrrr"

    def Overgrow(self, defender: Pokemon) ->str:
        response = f"{self.name} used Overgrow on {defender.name}!"

        if defender.type.lower() in ["fire","ice"]:
            response = response + " It was super effective."

        return response