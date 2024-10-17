import tbc
import combat

def main():
    hero = tbc.Character("Hero",10,50,5,2)
    monster = tbc.Character("Monster",20,30,5,0)
    combat.Combat.fight(hero,monster)

if __name__ == "__main__":
    main()