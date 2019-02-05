#alien blaster
#demonstrates object interaction

class Player(object):
    """A player in a shooter game."""
    def blast(self,enemy):
        print("the player blasts the enemy.\n")
        enemy.die()

class Alien(object):
    """an aliien in a shooter game."""
    def die(self):
        print("the alien gasps and says,'oh this is it. This is the big one.\n"
              "yes, it's gettin dark now. Tell my 1.6 million larvae that I loved them...\n"
              "Good-bye, cruel universe.")

#main
print("\t\tDeath of an alien\n")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress the enter key to exit")