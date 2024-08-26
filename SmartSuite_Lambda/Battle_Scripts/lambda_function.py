import json
import random

def lambda_handler(event, context):

    #creating 2 dictionaries to pull info into another function later one. 
    fighter1 = {
        "id" : event["Fighter1"]["ID"],
        "name" : event["Fighter1"]["Name"],
        "race" : event["Fighter1"]["Race"],
        "hp" : event["Fighter1"]["HP"],
        "class" : event["Fighter1"]["Class"],
        "lvl" : event["Fighter1"]["LVL"],
        "karma" : event["Fighter1"]["Karma"],
        "affinity" : event["Fighter1"]["Affinity"],
        "str" : event["Fighter1"]["STR"],
        "wis" : event["Fighter1"]["WIS"],
        "dex" : event["Fighter1"]["DEX"],
        "stl" : event["Fighter1"]["STL"]
                # "int" : ( #ternary style - all conditionals live on "one" line | UPDATE - Lambda didn't like syntax so using other style
                #     (fighter1["str"] *.5) + fighter1["lvl"] + random.randit(1,6) if fighter1["class"] == "Warrior"
                #     else (fighter1["wis"] *.5) + fighter1["lvl"] + random.randit(1,6) if fighter1["class"] == "Wizard"
                #     else (fighter1["dex"] *.5) + fighter1["lvl"] + random.randit(1,6) if fighter1["class"] == "Ranger"
                #     else (fighter1["stl"] *.5) + fighter1["lvl"] + random.randit(1,6) if fighter1["class"] == "Assassin")
        } 
        
    if fighter1["class"] == "Warrior":
        #appends a new key called intiative, with value defined by the right of the =, to fighter1 dictionary 
        fighter1["initiative"] = round(fighter1["str"] *.5) + fighter1["lvl"] + random.randint(1,6)
    elif fighter1["class"] == "Wizard":
        fighter1["initiative"] = round(fighter1["wis"] *.5) + fighter1["lvl"] + random.randint(1,6)
    elif fighter1["class"] == "Ranger":
        fighter1["initiative"] = round(fighter1["dex"] *.5) + fighter1["lvl"] + random.randint(1,6)
    elif fighter1["class"] == "Assassin": #or you can say else and the F2 = assassin is assumed
        fighter1["initiative"] = round(fighter1["stl"] *.5) + fighter1["lvl"] + random.randint(1,6)
            
            
    
    fighter2 = {
        "id" : event["Fighter2"]["ID"],
        "name" : event["Fighter2"]["Name"],
        "race" : event["Fighter2"]["Race"],
        "hp" : event["Fighter2"]["HP"],
        "class" : event["Fighter2"]["Class"],
        "lvl" : event["Fighter2"]["LVL"],
        "karma" : event["Fighter2"]["Karma"],
        "affinity" : event["Fighter2"]["Affinity"],
        "str" : event["Fighter2"]["STR"],
        "wis" : event["Fighter2"]["WIS"],
        "dex" : event["Fighter2"]["DEX"],
        "stl" : event["Fighter2"]["STL"]
        }         
    # using if and elif blocks
    if fighter2["class"] == "Warrior":
        #appends a new key called intiative, with value defined by the right of the =, to fighter2 dictionary 
        fighter2["initiative"] = round(fighter2["str"] *.5) + fighter2["lvl"] + random.randint(1,6)
    elif fighter2["class"] == "Wizard":
        fighter2["initiative"] = round(fighter2["wis"] *.5) + fighter2["lvl"] + random.randint(1,6)
    elif fighter2["class"] == "Ranger":
        fighter2["initiative"] = round(fighter2["dex"] *.5) + fighter2["lvl"] + random.randint(1,6)
    elif fighter2["class"] == "Assassin": #or you can say else and the F2 = assassin is assumed
        fighter2["initiative"] = round(fighter2["stl"] *.5) + fighter2["lvl"] + random.randint(1,6)


    battle_numbers = {}
    battle_data = {}
    battle_data["stats"] = []
    #adds a key called stats with a value of an empty list to battle_data
    #was {} for the string interpelation method using {}
    
    #step 1: compare initiative numbers to see who attacks first
    #Step 2: while either fighter's HP > 0, do this sequence
    #STEP 3: attacker main stat + random number(1,6) + class bonus(if applicable) - defenders matching attack stat
    #Step 4: swtich attacker and defender
    
    #terinary statement to assign attacker and defender
    attacker = fighter1 if fighter1["initiative"] > fighter2["initiative"] or fighter1["initiative"] == fighter2["initiative"] else fighter2 #assumes the reverse logic, and only 2 options
    defender = fighter1 if fighter1["initiative"] < fighter2["initiative"] or fighter2["initiative"] == fighter1["initiative"] else fighter2

    def battle_sequence(attacker, defender, round_number):
        """
        calculates the sequence of "attacks" using random numbers plus chracters pre-stated statistics. NOTE: as per above, attacker and defender will point
        towards a dictorionary. Calculates the damage number, hit, by class stat, random number, and class advantage (if applicable). Calculates the defender's
        defense stat, which is the defenders matching stat to the attack stat.
        """
        hit = None
        if attacker["class"] == "Warrior":
            if defender["class"] == "Wizard":
                hit = attacker["str"] + random.randint(1,6) + 1
            else:
               hit = attacker["str"] + random.randint(1,6)
            defense = defender["str"]
        
        if attacker["class"] == "Wizard":
            if defender["class"] == "Ranger":
               hit = attacker["wis"] + random.randint(1,6) + 1
            else:
                hit = attacker["wis"] + random.randint(1,6)
            defense = defender["wis"]
                
        if attacker["class"] == "Ranger":
            if defender["class"] == "Assasin":
                hit = attacker["dex"] + random.randint(1,6) + 1
                
            else:
                hit = attacker["dex"] + random.randint(1,6)
            defense = defender["dex"]
            
        if attacker["class"] == "Assassin":
            if defender["class"] == "Warrior":
                hit = attacker["stl"] + random.randint(1,6) + 1
                
            else:
                hit = attacker["stl"] + random.randint(1,6)
            defense = defender["stl"]

        defender["hp"] -= (hit - defense) # like saying defenderHP = defenderHP - (hit-defense)
        
        
        #this syntax is string interpelation 
        battle_numbers[f"round_{round_number}"] = {
            "round": round_number, 
            "attacker": attacker["name"], 
            "attacker_hp": attacker["hp"], 
            "attack_number": hit, 
            "defender": defender["name"], 
            "defense": defense, 
            "defender_hp": defender["hp"]
        
        }
       
       
    """
    runs battle sequence while both fighters are alive. 
    """
    round_number = 1
    while fighter1["hp"] > 0 and fighter2["hp"] > 0:
        if fighter1["hp"] <= 0 or fighter2["hp"] <=0:
            break
        else: #swaps attacker with defender
            battle_sequence(attacker = attacker, defender = defender, round_number=round_number)
            round_number += 1
        if fighter1["hp"] <= 0 or fighter2["hp"] <=0:
            break
        else: #resets original attacker and defender
            battle_sequence(attacker = defender, defender = attacker, round_number=round_number)
            round_number += 1
    
    winner = fighter1 if fighter1["hp"] > 0 else fighter2 #the while loop makes sure that only 1 fighter has hp > 0
    loser = fighter1 if fighter1["hp"] <= 0 else fighter2
    
    lu_list = []
    if winner["karma"] > loser["karma"]: #this will do nothing if karma is equal
        if winner["karma"] < 11:
            winner["karma"] += 1
            lu_list.append("Karma has increased by 1 to " + str(winner["karma"]))
    else:
        if winner["karma"] > 1:
            winner["karma"] -= 1
            lu_list.append("Karma has decreased by 1 to " + str(winner["karma"]))
    
    #checks winner karma and assigns affinity based on karma.
    #winner["affinity"] = "Good" if winner["karma"] > 8 else "Neutral" if winner["karma"] < 8 and winner["karma"] > 4 else "Evil"
    
    if winner["karma"] > 8:
        winner["affinity"] = "Good"
    elif winner["karma"] < 8 and winner["karma"] > 4:
        winner["affinity"] = "Neutral"
    else:
        winner["affinity"] = "Evil"
    
        
    #updates states based on a fixed % chance per class, and increases lvl. If lvl = 10, do nothing    
    if winner["lvl"] < 10: 
        if winner["class"] == "Warrior":
            if random.randint(0,100) > 30: #acts as a weight
                temp = winner["str"]
                winner["str"] += 1
                if temp != winner["str"]:
                    lu_list.append("Strenght level up by 1 to " + str(winner["str"]))
            if random.randint(0,100) > 50:
                temp = winner["wis"]
                winner["wis"] += 1
                if temp != winner["wis"]:
                    lu_list.append("Wisdom level up by 1 to " + str(winner["wis"]))
            if random.randint(0,100) > 50:
                temp = winner["dex"]
                winner["dex"] += 1
                if temp != winner["dex"]:
                    lu_list.append("Dexterity level up by 1 to " + str(winner["dex"]))
            if random.randint(0,100) > 70:
                temp = winner["stl"]
                winner["stl"] += 1
                if temp != winner["stl"]:
                    lu_list.append("Stealth level up by 1 to " + str(winner["stl"]))
                
        if winner["class"] == "Wizard":
            if random.randint(0,100) > 70:
                temp = winner["str"]
                winner["str"] += 1
                if temp != winner["str"]:
                    lu_list.append("Strenght level up by 1 to " + str(winner["str"]))
            if random.randint(0,100) > 30:
                temp = winner["wis"]
                winner["wis"] += 1
                if temp != winner["wis"]:
                    lu_list.append("Wisdom level up by 1 to " + str(winner["wis"]))
            if random.randint(0,100) > 50:
                temp = winner["dex"]
                winner["dex"] += 1
                if temp != winner["dex"]:
                    lu_list.append("Dexterity level up by 1 to " + str(winner["dex"]))
            if random.randint(0,100) > 50:
                temp = winner["stl"]
                winner["stl"] += 1
                if temp != winner["stl"]:
                    lu_list.append("Stealth level up by 1 to " + str(winner["stl"]))
        
        if winner["class"] == "Ranger":
            if random.randint(0,100) > 50:
                temp = winner["str"]
                winner["str"] += 1
                if temp != winner["str"]:
                    lu_list.append("Strenght level up by 1 to " + str(winner["str"]))
            if random.randint(0,100) > 70:
                temp = winner["wis"]
                winner["wis"] += 1
                if temp != winner["wis"]:
                    lu_list.append("Wisdom level up by 1 to " + str(winner["wis"]))
            if random.randint(0,100) > 30:
                temp = winner["dex"]
                winner["dex"] += 1
                if temp != winner["dex"]:
                    lu_list.append("Dexterity level up by 1 to " + str(winner["dex"]))
            if random.randint(0,100) > 50:
                temp = winner["stl"]
                winner["stl"] += 1
                if temp != winner["stl"]:
                    lu_list.append("Stealth level up by 1 to " + str(winner["stl"]))
        
        if winner["class"] == "Assassin":
            if random.randint(0,100) > 50:
                temp = winner["str"]
                winner["str"] += 1
                if temp != winner["str"]:
                    lu_list.append("Strenght level up by 1 to " + str(winner["str"]))
            if random.randint(0,100) > 50:
                temp = winner["wis"]
                winner["wis"] += 1
                if temp != winner["wis"]:
                    lu_list.append("Wisdom level up by 1 to " + str(winner["wis"]))
            if random.randint(0,100) > 70:
                temp = winner["dex"]
                winner["dex"] += 1
                if temp != winner["dex"]:
                    lu_list.append("Dexterity level up by 1 to " + str(winner["dex"]))
            if random.randint(0,100) > 30:
                temp = winner["stl"]
                winner["stl"] += 1
                if temp != winner["stl"]:
                    lu_list.append("Stealth level up by 1 to " + str(winner["stl"]))
        #level always goes up unless at max level of 10            
        winner["lvl"] += 1
        lu_list.append("level up by 1 to " + str(winner["lvl"]))
    else:
        lu_list.append("character is at max level")
        
    #converting to a list for compliance with Make's iterator, which requires a list not a dict    
    battle_data["stats"].append(battle_numbers)
        
    return {
        "winner": winner,
        "loser" : loser,
        "Battle_stats": battle_data,
        "lu_list": lu_list
    }

    
        #"Battle_stats": battle_numbers
        #last line of return statement 
        