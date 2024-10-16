import tbc

def main():
    hero = tbc.Character("Hero",10,50,5,2)
    monster = tbc.Character("Monster",20,30,5,0)
    tbc.fight(hero,monster)

if __name__ == "__main__":
    main()