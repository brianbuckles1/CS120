import random

class Character():
    """ basic character class for storing various information
        for a turn based rpg style game."""
    
    def __init__(self, name:str, hit_points:int, hit_chance:int, 
                 max_damage:int, armor:int):
        """ class default constructor that will set the initial
            stats for a character """
        self.__name = name
        self.__hit_points = self.testInt(hit_points,min=1,default=1)
        self.__hit_chance = self.testInt(hit_chance,min=1)
        self.__max_damage = self.testInt(max_damage,min=1)
        self.__armor = self.testInt(armor, min=1)

    def get_name(self)->str:
        """ returns the character name 
            as integer """
        return self.__name

    def get_hit_points(self)->int:
        """ returns the character hit points 
            as integer """
        return self.__hit_points
    
    def _set_hit_points(self, new_hit_points):
        """ set the hitpoints to the
            new specified value. """
        self.__hit_points = new_hit_points
    
    def get_hit_chance(self)->int:
        """ returns the character hit chance 
            as integer """
        return self.__hit_chance
    
    def get_max_damage(self)->int:
        """ returns the character max damage 
            as integer """
        return self.__max_damage
    
    def get_armor(self)->int:
        """ returns the character armor as 
            an integer """
        return self.__armor

    def print_stats(self):
        """ Returns the character stats
            in a nice pretty string."""
        print(f"""
        =========================
        {self.get_name()}
        =========================
        Hit Points: {self.get_hit_points():>5}
        Hit Chance: {self.get_hit_chance():>5}
        Max Damage: {self.get_max_damage():>5}
             Armor: {self.get_armor():>5}
        =========================
        """)

    def testInt(self, value, min = 0, max = 100, default = 0)->int:
        """ takes in value 
            checks to see if it is an int between
            min and max.  If it is not a legal value
            set it to default """

        out = default

        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")

        return out
    
    def get_attack(self)->int:
        """ returns the characters damage.  It will
            calculate if the character hits and if 
            a hit will generate a random number
            between 1 and max damage """
        damage = 0
        calculated_hit = random.randint(1,100)

        if calculated_hit > self.get_hit_chance():
            damage = random.randint(1,self.get_max_damage())
            print(f"{self.get_name()} hit for {damage}!")
        else:
            print(f"{self.get_name()} missed!")

        return damage
    
    def apply_damage(self, incoming_damage):
        """ Calculates how much damage is taken and adjusts
            the hit points accordingly.  Note: Hitpoints do
            not go below 0. If damage exceeds hit points 
            then hit points is set to 0"""
        total_damage_taken = 0
        total_absorbed = 0
        if incoming_damage > self.get_armor():
            total_damage_taken = incoming_damage - self.get_armor()

        total_absorbed = incoming_damage - total_damage_taken
        print(f"{self.get_name()} armor absorbed {total_absorbed}")
        print(f"{self.get_name()} takes {total_damage_taken}")

        if total_damage_taken > self.get_hit_points():
            self._set_hit_points(0)
        else:
            new_hit_points = self.get_hit_points() - total_damage_taken
            self._set_hit_points(new_hit_points)
        
        print(f"{self.get_name()} has {self.get_hit_points()} hit points left!")

def main():
    hero = Character("Hero",10,50,5,2)

if __name__ == "__main__":
    main()
