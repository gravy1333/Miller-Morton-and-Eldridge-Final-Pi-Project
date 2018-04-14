# monsters by CR
# 'Monster Name': [ "Stats", "Challenge Rating number", Experience points, Armor Class, Hp, Specs, Actions]

Monster_Dictionary = {
    "Awakend Shrub":["STR 3(-4) DEX 8(-1) CON 11(0) WIS 10(0) CHA 6(-2)","0", "10","AC 9","10", "Speed 20ft weakness:fire Damage Resistance:Piercing, Senses: passive Perception: 10 Languages: One language Know By its Creator","1d20 +1d4-1"],
    "Baboon":["STR 8(-1) DEX 14(+2) CON 11(0) INT 4(-3) WIS 12(+1) CHA 6(-2)","0","10","12","3","Speed 30ft climb 30ft Senses: passive Percption 11","bite 1d20 +1d4-1"],
    "Badger":["STR 4(-3) DEX 11(0) CON 12(+1) INT 2(-4) WIS 12(+1) CHA 5(-3)","0","10","10","3","Speed 20ft burrow 5ft Senses: Darkvision 30ft. passive Perception 11","bite 1d20+2d1"],
    "Bat":["STR 2(-4) DEX 15(+2) CON 8(-1) INT 2(-4) WIS 12(+1) CHA 4(-3)","0","10","12","1","Speed 5ft fly 30ft Senses Blindsight 60ft passive Perception 11","bite 1d20+0d1"],
    "Cat":["STR 3(-4) DEX 15(+2) CON 10(+0) INT 3(-4) WIS 12(+1) CHA 7(-2)","0","10","12","2","Speed 40ft climb 30ft Skills Perception +3 Stealth +4 Senses passive Perception 13","1d20+0d1"],
    "Commoner":["STR 10(+0) DEX 10 CON 10 INT 10 WIS 10 CHA 10","0","10","10","4","Speed 30ft Senses passive Perception 10 Langauages any one language(usually Common)","1d20+2d4"],
    "Crab":["STR 2(-4) DEX 11(0) CON 10(0) INT 1(-5) WIS 8(-1) CHA 2(-4)","0" "10", "11","2","Speed 20ft, swim 20ft Skills stealth +2 Senses Blindsight 30ft passive Perception 9","claw 1d20+0d1"],
    "Deer":["STR 11(0) DEX 16(+3) CON 11(+0) INT2(-4) WIS 14(+2) CHA 5(-3)","0","10","13","4","Speed 50ft Senses passive Perception 12","Bite 1d20+2d4"],
    "Eagle":["STR 6(-2) DEX 15(+2) CON 10(0) INT 2(-4) WIS 14(+2) CHA 7(-2)","0","10","12","3","Speed 10ft fly 60ft Skills Perception +4 Senses passive Perception 14","Talons 1d20+4 +1d4+2"],
    "Frog":["STR 1(-5) DEX 13(+2) CON 8(-1) INT 1(-5) WIS 8(-1) CHA 3(-4)","0","10","11","1","Speed Perception +1, Stealth +3 Senses Darkvision 30ft passive Perception 11","None"],
    "Giant Fire Bettle":["STR 8(-1) DEX 10(0) CON 12(+1) INT 1(-5) WIS 7(-2) CHA 3(-4)","0","10","13","4","Speed 30ft Blindsight 30ft passive Perception 8","Bite 1d20+1 + 1d6-1"],
    "Goat":["STR 12(+1) DEX 10(0) CON 11(+0) INT 2(-4) WIS 10(0) CHA 5(-3)","0","10","10","4","Speed 40ft Senses passive Perception 10","Ram 1d20+3 + 1d4+1"],
    "Hawk":["STR 5(-3) DEX 16(+3) CON 8(-1) INT 2(-4) WIS 14(+2) CHA 6(-2)","0","10","13","1","Speed 10ft fly 60ft Skills Perception +4 Senses passive Perception 14","Talons 1d20+5+0d1"],
    "Homunculus":["STR 4(-3) DEX 15(+2) CON 11(+0) INT 10(+0) WIS 10(+0) CHA 7(-2)","0","10","13","5","Speed 20ft 40ft Damage Immunities (Poison) Condition Immunities (Charmed Poisned) Senses Darkvision 60ft passive Perception 10 Languages (understands the languages of its Creator but can't speak","Bite 1d20+4 + 0d1"],
    "Heyna":["STR 11(0) DEX 13(+1) CON 12(+1) INT 2(-4) WIS 12(+1) CHA 5(-3)","0","10","11","5""Speed 50ft Skills Perception +3 Senses passive Perception 13","Bite 1d20+2 +1d6"],
    "Jackal":["STR 8(-1) DEX 15(+2) CON 11(0) INT 3(-4) WIS 12(+1) CHA 6(-2)","0","10","12","3","Speed 40ft Skills Perception +3 Senses passive Perception 13","Bite 1d20 +1 +1d4-1"],
    "Lemure":["STR 10(+0) DEX 5(-3) CON 11(0) INT 1(-5) WIS 11(+0) CHA 3(-4)","0","10","7","13","Speed 15ft Damage Resistance (cold) Damage Immunities (fire poison) Condition Immunities (Charmed, Frightened, Poisoned) Senses Darkvision 120ft passive Perception 10 Languagues (understands infernal but can't speak","None"],
    "Lizard":["STR 2(-4) DEX 11(+0) CON 10(0) INT 1(-5) WIS 8(-1) CHA 3(-4)","0","10","10","2","Speed 20ft climb 20ft Senses Darkvison 30ft passive Perception 9","Bite 1d20 +0d1"],
    "Octopus":["STR 4(-3) DEX 15(+2) CON 11(+0) INT 3(-4) WIS 10(0) CHA 4(-3)","0","10","12","3","Speed 5ft 30ft swim Skills Perception +2 Stealth +4 Senses Darkvison 30ft passive Perception 12","Tentacles 1d20 +4 +0d1"],
    "Owl":["STR 3(-4) DEX 13(+1z) CON 8(-1) INT 2(-4) WIS 12(+1) CHA 7(-2)","0","10","11","1","Speed 5ft. fly 60ft Skills Perception +3 Stealth +3 Senses Darkvision 120ft passivePerception 13","Talons 1d20 +3d1"],
    "Quipper":["STR 2(-4) DEX 16(+3) CON 9(-1) INT 1(-5) WIS 7(-2) CHA 2(-4)","0","10","13","1","Speed swim 40ft Senses Darkvision 60ft passive PErception 8","Bite 1d20+ 5d1"],
    "Rat":["STR 2(-4) DEX 11(0) CON 9(-1) INT 2(-4) WIS 10(0) CHA 4(-3)","0","10","10","1","Speed 20ft Senses Darkvision 30ft passive Perception 10","Bite 1d20 + 0d1"],
    "Raven":["STR 2(-4) DEX 14(+2) CON 8(-1) INT 2(-4) WIS 12(+1) CHA 6(-2)","0","10","12","1","Speed 10ft fly 50ft Skills Perception +3 Senses passive Perception 13","None"],
    "Scorpion":["STR 2(-4) DEX 11(+0) CON 8(-1) INT 1(-5) WIS 8(-1) CHA 2(-4)","0","10","11","1","Speed 10ft Senses Blindsight 10f passive Perception 9","Sting 1d20 +2d1"],
    "Sea Horse":["STR 1(-5) DEX 12(+1) CON 8(-1) INT 1(-5) WIS 10(+0) CHA 2(-4)","0","10","11","1","Speed swim 20ft Senses passive Perception 10","None"],
    "Shrieker":["STR 1(-5) DEX 1(-5) CON 10(+0) INT 1(-5) WIS 3(-4) CHA 1(-5)","0","10","5","13","Speed 0ft Condition Immunities Blinded, Deafened, Frightened Senses Blindsight 30ft.(Blind beyond this Radius) passive Perception 6","None"],
    "Spider":["STR 2(-4) DEX 14(+2) CON 8(-1) INT 1(-5) WIS 10(+0) CHA 2(-4)","0","10","12","1","Speed 20ft climb 20ft Skills Stealth +4 Senses Darkvison 30ft. passive Perception 12","Bite 1d20 +4d1"],
    "Vulture":["STR 7(-2) DEX 10(0) CON 13(+1) INT 2(-4) WIS 12(+1) CHA 4(-3)","0","10","10","5","Speed 10ft fly 50ft Skills Perception +3 Senses passive Perception 13","Beak 1d20 +2 1d4"],
    "Weasel":["STR 3(-4) DEX 16(+3) CON 8(-1) INT 2(-4) WIS 12(+1) CHA 3(-4)","0","10","13","1","Speed 30ft Skills Perception +3, Stealth +5 Senses passive Perception 13","Bite 1d20 +5d1"]
    "Bandit":["STR 11(+0) DEX 12(+1) CON 12(+1) INT 10(+0) WIS 10(+0) CHA 10(+0)","1/8","25","12","11","Speed 30ft Senses passive Percption 10 Languages any one language (usually common)","1d20+3 1d6+1, 1d20 +3 1d8+1"]
    
