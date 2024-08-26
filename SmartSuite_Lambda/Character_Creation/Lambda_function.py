import json
import random
from get_worlds import worlds_method

def lambda_handler(event, context):
    '''
    This function determines the characteristics and stats of a character. It takes the record ID of the SmartSuite record (supplied from Make)
    as an input and the rest is generated here
    '''
    
    #dictionary for character traits - returned at the end
    character_traits = {}
    character_traits["ID"] = event["record _id"]
    world_list = []
    
    #pick Race
    race_list = ["Orc","Dwarf","Celestial","Fiary","Human","Demon","Goblin","Elf","Elemental"]
    race_number = random.randint(1,9)
    character_traits["Race"] = race_list[race_number-1]
    
    #pick Origin
    origin_dict = ["Plains", "City", "Mountains", "Forest", "Desert", "Village"]
    origin_number = random.randint(1,6)
    character_traits["Origin"] = origin_dict[origin_number-1]
   
    '''
    calls on the worlds_method from the file called get_worlds - runs it, and then returns the output back to this scope
    '''
    #assign in this scope #calls method  #name in OTHER method = #data type or variable in THIS enviornment (scope)
    character_traits =  worlds_method(character_traits_from_parent=character_traits)
   
    print("after functions run and back in main function " + str(type(character_traits)))
    print(character_traits)
    
    #pick Class
    class_number = random.randint(1,16) #select race by random number
    if class_number in [1,5,9,13]:
        character_traits["Class"] = "Warrior"
    if class_number in [2,6,10,14]:
        character_traits["Class"] = "Wizard"
    if class_number in [3,7,11,15]:
        character_traits["Class"] = "Ranger"
    if class_number in [4,8,12,16]:
        character_traits["Class"] = "Assassin"

    
    #pick Affinity
    affinity_number = random.randint(1,99)
    if character_traits["Race"] in ["Elf", "Fairy", "Celestial"]:
        affinity_number += 22
    if character_traits["Race"] in ["Orc", "Goblin", "Demon"]:
        affinity_number -= 22
    character_traits["Affinity"] = "Good" if affinity_number >= 67 else "Evil" if affinity_number <= 33 else "Neutral"
    
    #pick Strength
    str_number = random.randint(1,6)
    if character_traits["Class"] == "Warrior":
        str_number += 2
    if character_traits["Class"] == "Wizard":
        str_number -= 1
    character_traits["Strength"] = str_number
    
    #pick Wisdom
    wis_number = random.randint(1,6)
    if character_traits["Class"] == "Wizard":
        str_number += 2
    if character_traits["Class"] == "Ranger":
        str_number -= 1
    character_traits["Wisdom"] = wis_number
    
    #pick Dexterity
    dex_number = random.randint(1,6)
    if character_traits["Class"] == "Ranger":
        str_number += 2
    if character_traits["Class"] == "Assassin":
        str_number -= 1
    character_traits["Dexterity"] = dex_number
    
    #pick Stealth
    stl_number = random.randint(1,6)
    if character_traits["Class"] == "Assassin":
        str_number += 2
    if character_traits["Class"] == "Warrior":
        str_number -= 1
    character_traits["Stealth"] = stl_number
    
    #pick HP
    character_traits["Health"] = random.randint(1,8)
    
    #pick Karma
    if character_traits["Affinity"] == "Evil":
        character_traits["Karma"] = random.randint(1,3)
    if character_traits["Affinity"] == "Neutral":
        character_traits["Karma"] = random.randint(5,7)
    if character_traits["Affinity"] == "Good":
        character_traits["Karma"] = random.randint(9,11)
    
    #pick Background Event
    evil_list=["Domination of others", "Looking to summon a mythological evil", "Internal insanity" ]
    neutral_list=["Village, tribe, or city involved in war", "Personal revenge story", "Seeker of legendary power"]
    good_list=["Set out on an adventure to develop skills", "Defending a holy land or home land", "Desire to protect a certain people or item" ]
    
    if character_traits["Affinity"] == "Evil":
        character_traits["Background_Event"] = evil_list[random.randint(0,2)]
    if character_traits["Affinity"] == "Neutral":
        character_traits["Background_Event"] = neutral_list[random.randint(0,2)]
    if character_traits["Affinity"] == "Good":
        character_traits["Background_Event"] = good_list[random.randint(0,2)]
    
    #pick gender
    if random.randint(1,10) in [1,3,5,7,9]:
        character_traits["Gender"] = "Male"
    else:
        character_traits["Gender"] = "Female"
        
    return character_traits

    
 
    