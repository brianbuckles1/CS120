import tbc

class Combat():
    @staticmethod
    def take_turn(attacker:tbc.Character, defender:tbc.Character):
        """ characters turn to apply damage and returns a
            boolean if character wins.  This is true if 
            the defender's hit points are 0.
        """
        print(f"\n{attacker.get_name()} turn:")
        defender.apply_damage(attacker.get_attack())
        if defender.get_hit_points() == 0:
            print(f"{attacker.get_name()} wins!")
        
    @staticmethod
    def fight(character1:tbc.Character, character2:tbc.Character):
        """ pit two characters together and have them fight
            until one character run out of hit points.
            Returns the winning character"""

        character1.print_stats()
        character2.print_stats()
        
        keepGoing = True
        round = 1

        while(keepGoing):
            print(f"\nRound {round}:")

            Combat.take_turn(character1, character2)
            if character2.get_hit_points() == 0:
                keepGoing = False
            else:
                Combat.take_turn(character2, character1)
                
                if character1.get_hit_points() == 0:
                    keepGoing = False
            input("press any key to continue.")
            round += 1 

def main():
    hero = tbc.Character("Hero",10,50,5,2)
    monster = tbc.Character("Monster",20,30,5,0)
    Combat.fight(hero,monster)

if __name__ == "__main__":
    main()