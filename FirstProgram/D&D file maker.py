#Matthew Walker
#1/22/19

class DnD(object):

    def __init__(self,pcClass,barbarianSub,bardSub,clericSub,druidSub,fighterSub,monkSub,paladinSub,rangerSub,rogueSub,sorcererSub,warlockSub,wizardSub,pcRaces):
        self.pcClass = ["barbarian","bard","cleric","druid","fighter","monk","paladin","ranger","rogue","sorcerer","warlock","wizard"]
        self.barbarianSub = ["path of the Ancestral Guardian","Path of the Battlerager","path of the berserker","path of the storm herald","path of the totem warrior","path of the zealot"]
        self.bardSub = ["college of glamour","college of lore","college of satire","college of swords","college of valor","college of whispers"]
        self.clericSub = ["arcana domain","ambition domain","city domain","death domain","forge domain","grave domain","knowledge domain","life domain","light domain","light domain","nature domain","order domain","protection domain",
                          "solidarity domain","strength domain","tempest domain","trickery domain","war domain","zeal domain"]
        self.druidSub = ["circle of dreams","circle of the land","circle of the moon","circle of the shepherd","circle of spores","circle of twilight"]
        self.fighterSub = ["arcane archer","battle master","brute","cavalier","champion","eldritch knight","monster hunter","purple dragon knight","samurai","scout","sharpshooter"]
        self.monkSub = ["way of the drunken master","way of the four elements","way of the kensei","way of the long death","way of the open hand","way of shadow","way of the sun soul","way of tranquility"]
        self.paladinSub = ["oath of the ancients","oath of conquest","oath of the crown","oath of devotion","oath of redemption","oath of vengeance"]
        self.rangerSub = ["beast master","gloom stalker","horizon walker","hunter","monster slayer","primeval guardian"]
        self.rogueSub = ["arcane trickster","assassin","inquisitive","mastermind","scout","swashbuckler","thief"]
        self.sorcererSub = ["divine soul","draconic bloodline","giant soul","poenix sorcery","pyromancer","sea sorcery","shadow magic","stone sorcery","storm sorcery","wild magic"]
        self.warlockSub = ["the archfey","the celestial","the fiend","the ghost in the machine","the great old one","the hexblade","the raven queen","the seeker","the undying"]
        self.wizardSub = ["artificer","bladesinger","loremastery","school of abjuration","school of conguration","school of divination","school of enchantment","school of evocation","school ofillusion",
                          "school of invention","shool of necromancy","school of transmutation","technomancy","theurgy","war magic"]
        self.pcRaces = ["dragonborn","dwarf","elf","gnome","halfElf","halfOrc","halfling","human","tiefling"]

    def pickClass(self):
        yourClass = input("Type in the name of one of the following classes to choose it for your class",self.pcClass)
        while yourClass.lower() not in self.pcClass:
            print("thats not one of the classes that was specified.\nPlease make sure that it is spelled the same")
            yourClass = input("Type in the name of one of the following classes to choose it for your class",self.pcClass)