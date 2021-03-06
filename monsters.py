# monsters by Challenge Rating
# 'Monster Name': [ "Stats", "Challenge Rating number", Experience points, Armor Class, Hp, Specs, Actions]

Monster_Dictionary = {
    "Awakend Shrub":["STR 3(-4) DEX 8(-1) CON 11(0) WIS 10(0) CHA 6(-2)",0, 10,9,10,"Speed 20ft weakness:fire Damage Resistance:Piercing, Senses: passive Perception: 10 Languages: One language Know By its Creator","1d20 +1d4-1"],
    "Baboon":["STR 8(-1) DEX 14(+2) CON 11(0) INT 4(-3) WIS 12(+1) CHA 6(-2)",0,10,12,3,"Speed 30ft climb 30ft Senses: passive Percption 11","bite 1d20 +1d4-1"],
    "Badger":["STR 4(-3) DEX 11(0) CON 12(+1) INT 2(-4) WIS 12(+1) CHA 5(-3)",0,10,10,3,"Speed 20ft burrow 5ft Senses: Darkvision 30ft. passive Perception 11","bite 1d20+2d1"],
    "Bat":["STR 2(-4) DEX 15(+2) CON 8(-1) INT 2(-4) WIS 12(+1) CHA 4(-3)",0,10,12,1,"Speed 5ft fly 30ft Senses Blindsight 60ft passive Perception 11","bite 1d20+0d1"],
    "Cat":["STR 3(-4) DEX 15(+2) CON 10(+0) INT 3(-4) WIS 12(+1) CHA 7(-2)",0,10,12,2,"Speed 40ft climb 30ft Skills Perception +3 Stealth +4 Senses passive Perception 13","1d20+0d1"],
    "Commoner":["STR 10(+0) DEX 10 CON 10 INT 10 WIS 10 CHA 10",0,10,10,4,"Speed 30ft Senses passive Perception 10 Langauages any one language(usually Common)","1d20+2d4"],
    "Crab":["STR 2(-4) DEX 11(0) CON 10(0) INT 1(-5) WIS 8(-1) CHA 2(-4)",0,10, 11,2,"Speed 20ft, swim 20ft Skills stealth +2 Senses Blindsight 30ft passive Perception 9","claw 1d20+0d1"],
    "Deer":["STR 11(0) DEX 16(+3) CON 11(+0) INT2(-4) WIS 14(+2) CHA 5(-3)",0,10,13,4,"Speed 50ft Senses passive Perception 12","Bite 1d20+2d4"],
    "Eagle":["STR 6(-2) DEX 15(+2) CON 10(0) INT 2(-4) WIS 14(+2) CHA 7(-2)",0,10,12,3,"Speed 10ft fly 60ft Skills Perception +4 Senses passive Perception 14","Talons 1d20+4 +1d4+2"],
    "Frog":["STR 1(-5) DEX 13(+2) CON 8(-1) INT 1(-5) WIS 8(-1) CHA 3(-4)",0,10,11,1,"Speed Perception +1, Stealth +3 Senses Darkvision 30ft passive Perception 11","None"],
    "Giant Fire Bettle":["STR 8(-1) DEX 10(0) CON 12(+1) INT 1(-5) WIS 7(-2) CHA 3(-4)",0,10,13,4,"Speed 30ft Blindsight 30ft passive Perception 8","Bite 1d20+1 + 1d6-1"],
    "Goat":["STR 12(+1) DEX 10(0) CON 11(+0) INT 2(-4) WIS 10(0) CHA 5(-3)",0,10,10,4,"Speed 40ft Senses passive Perception 10","Ram 1d20+3 + 1d4+1"],
    "Hawk":["STR 5(-3) DEX 16(+3) CON 8(-1) INT 2(-4) WIS 14(+2) CHA 6(-2)",0,10,13,1,"Speed 10ft fly 60ft Skills Perception +4 Senses passive Perception 14","Talons 1d20+5+0d1"],
    "Homunculus":["STR 4(-3) DEX 15(+2) CON 11(+0) INT 10(+0) WIS 10(+0) CHA 7(-2)",0,10,13,5,"Speed 20ft fly 40ft Damage Immunities (Poison) Condition Immunities (Charmed Poisned) Senses Darkvision 60ft passive Perception 10 Languages (understands the languages of its Creator but can't speak","Bite 1d20+4 + 0d1"],
    "Heyna":["STR 11(0) DEX 13(+1) CON 12(+1) INT 2(-4) WIS 12(+1) CHA 5(-3)",0,10,11,5,"Speed 50ft Skills Perception +3 Senses passive Perception 13","Bite 1d20+2 +1d6"],
    "Jackal":["STR 8(-1) DEX 15(+2) CON 11(0) INT 3(-4) WIS 12(+1) CHA 6(-2)",0,10,12,3,"Speed 40ft Skills Perception +3 Senses passive Perception 13","Bite 1d20 +1 +1d4-1"],
    "Lemure":["STR 10(+0) DEX 5(-3) CON 11(0) INT 1(-5) WIS 11(+0) CHA 3(-4)",0,10,7,13,"Speed 15ft Damage Resistance (cold) Damage Immunities (fire poison) Condition Immunities (Charmed, Frightened, Poisoned) Senses Darkvision 120ft passive Perception 10 Languagues (understands infernal but can't speak","None"],
    "Lizard":["STR 2(-4) DEX 11(+0) CON 10(0) INT 1(-5) WIS 8(-1) CHA 3(-4)",0,10,10,2,"Speed 20ft climb 20ft Senses Darkvison 30ft passive Perception 9","Bite 1d20 +0d1"],
    "Octopus":["STR 4(-3) DEX 15(+2) CON 11(+0) INT 3(-4) WIS 10(0) CHA 4(-3)",0,10,12,3,"Speed 5ft 30ft swim Skills Perception +2 Stealth +4 Senses Darkvison 30ft passive Perception 12","Tentacles 1d20 +4 +0d1"],
    "Owl":["STR 3(-4) DEX 13(+1z) CON 8(-1) INT 2(-4) WIS 12(+1) CHA 7(-2)",0,10,11,1,"Speed 5ft. fly 60ft Skills Perception +3 Stealth +3 Senses Darkvision 120ft passivePerception 13","Talons 1d20 +3d1"],
    "Quipper":["STR 2(-4) DEX 16(+3) CON 9(-1) INT 1(-5) WIS 7(-2) CHA 2(-4)",0,10,13,1,"Speed swim 40ft Senses Darkvision 60ft passive PErception 8","Bite 1d20+ 5d1"],
    "Rat":["STR 2(-4) DEX 11(0) CON 9(-1) INT 2(-4) WIS 10(0) CHA 4(-3)",0,10,10,1,"Speed 20ft Senses Darkvision 30ft passive Perception 10","Bite 1d20 + 0d1"],
    "Raven":["STR 2(-4) DEX 14(+2) CON 8(-1) INT 2(-4) WIS 12(+1) CHA 6(-2)",0,10,12,1,"Speed 10ft fly 50ft Skills Perception +3 Senses passive Perception 13","None"],
    "Scorpion":["STR 2(-4) DEX 11(+0) CON 8(-1) INT 1(-5) WIS 8(-1) CHA 2(-4)",0,10,11,1,"Speed 10ft Senses Blindsight 10f passive Perception 9","Sting 1d20 +2d1"],
    "Sea Horse":["STR 1(-5) DEX 12(+1) CON 8(-1) INT 1(-5) WIS 10(+0) CHA 2(-4)",0,10,11,1,"Speed swim 20ft Senses passive Perception 10","None"],
    "Shrieker":["STR 1(-5) DEX 1(-5) CON 10(+0) INT 1(-5) WIS 3(-4) CHA 1(-5)",0,10,5,13,"Speed 0ft Condition Immunities Blinded, Deafened, Frightened Senses Blindsight 30ft.(Blind beyond this Radius) passive Perception 6","None"],
    "Spider":["STR 2(-4) DEX 14(+2) CON 8(-1) INT 1(-5) WIS 10(+0) CHA 2(-4)",0,10,12,1,"Speed 20ft climb 20ft Skills Stealth +4 Senses Darkvison 30ft. passive Perception 12","Bite 1d20 +4d1"],
    "Vulture":["STR 7(-2) DEX 10(0) CON 13(+1) INT 2(-4) WIS 12(+1) CHA 4(-3)",0,10,10,5,"Speed 10ft fly 50ft Skills Perception +3 Senses passive Perception 13","Beak 1d20 +2 1d4"],
    "Animated Armor":["STR 14(+2) DEX 11(+0) CON 13(+10 INT 1(-5) WIS 3(-4) CHA1(-5)",1,200,18,33,25,"Speed 25 Damage Immunities Poison, Physchic Condition Immunities Blinded,Charmed,Deafened,Exhaustion,Paralyzed,Petrified,Poisoned Senses Blindsight 60ft(Blind beyound this radius) passive Perception 6","1d20+4 16+2"],
    "Brass Dragon Wyrmling":["STR 15(+2) DEX 10(+0) CON +13(+1) INT 10(+0) WIS 10(+0) CHA 13(+1)",1,200,16,16,"Speed 30ft burrow 15ft fly 60ft Saving Throws Dex+2 Con+2 Wis+2 Cha +3 Skills Perception+4 Stealth+2 Damage Immunities Fire Sense Blindsight 10 Darkvision 60ft Passive Perception 14 Langauges Draconic","Bite 1d20+4 1d10+2 Fire Breath 1d20 4d6"],
    "Brown Bear":["STR 19(+4) DEX 10(+0) C0N 16(+3) INT 2(-4) WIS 13(+1) CHA 7(-2)",1,200,11,34,"Speed 40ft climb 30ft Skills Perception +3 Senses passive Perception +13","Bite 1d20+5 1d8+4 Claws 1d20+5 2d6+4"],
    "Bugbear":["STR 15(+2) DEX 14(+2) CON 13(+1) INT 8(-1) WIS 11(+0) CHA 9(-1)",1,200,16,27,"Speed 30ft Skills stealth +6 survival +2 Senses Darkvision 60 passive Perception 10 Languages Common, Goblin","Moringstar 120+4 2d8+2 Melee 1d20+4 2d6+2 Ranged 1d20+4 1d6+2"],
    "Copper Dragon Wyrmling":[" STR 15(+2) DEX 12(+1) CON 13(+1) INT 14(+2) WIS 11(+0) CHA 13(+1)",1,200,16,22,"Speed 30ft fly 60ft Savingthrows Dex+3 Con+3 Wis+2 Cha+3 Skills Percpetion+4 Stealth+3 Damage Immunities Acid Senses Blindsight 10ft Darkvision 60ft passive Percpertion 14 Languages Draconic","Bite 1d20+4 1d10+2 Acid Breath 1d20+0 4d8"],
    "Ghoul":["STR 13(+1) DEX 15(+2) CON 10(+0) INT 7(-2) WIS 10(+0) CHA 6(-2)",1,200,12,30,"Speed 30ft Damage Immunities Poison Condition Immunities Charmed, Exhaustion, Poisoned Senses Darkvision 60ft Perception 10 Languages Common","Bite 1d20+2 2d6+2"],
    "Harpy":["STR 12(+1) DEX 13(+1) CON 12(+1) INT 7(-2) WIS 10(+0) CHA 13(+1)",1,200,11,38,"Speed 20ft fly 40ft Senses passive Perception 10 Languages Common","1d20+3 2d4+1 1d20+3 1d4+1"],
    }

class Monster(object):
    def __init__(self, val=10):
        #temp is here to fix player instanciation issue
        self.maxH = val
        self.currentH = val

    @property
    def maxH(self):
        return self._maxH

    @maxH.setter
    def maxH(self, val):
        if (val > 0):
            self._maxH = val

    @property
    def currentH(self):
        return self._currentH

    @currentH.setter
    def currentH(self, val):
        if (val <= 0):
            self._currentH = 0
        elif (val >= self.maxH):
            self._currentH = self.maxH
        else:
            self._currentH = val

    def getHealthPercent(self):
        return (float(self.currentH) / self.maxH) * 100

    def __str__(self):
        return "{}/{}".format(self.currentH, self.maxH)
