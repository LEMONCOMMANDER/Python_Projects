#this function creates a random number from 1 to upper limit, which is determined by the length of a provided 
#list. It will then create a second number from a second provided list, which may be the same or a seperate one
#depeding on the configuration of "equal" or "rankup" in SmartSuite. If the same, the numbers != same


import json
import random

def lambda_handler(event, context):
    """
    part 1 will evaluate the list of chracters provided and strip the level associated with each character into a new list. It will then 
    evaluate each character level against the fight level provided. Anytime the character is eligable, it will be added to the 
    eligable list.
    
    can evaluate the list against 2 provided levels should you keep the equal or rank up concept, you would need to include some identifier in 
    the make JSON
    
    part 2 will choose w random characters, that are not the same, from the eligable list, and use that to update SS.
    """
    
    #system lists 
    split_list_4lvl = []
    counter = 0
    
    #usable lists
    eligable_f = [] #stores only fighters that are living and at the specified level
    character_list = [] #stores names of all fighters - index reference to this list 
   
    '''
    part 1
    '''
    living_test=[]
    
    for character in event["c_list"]: #data from SS/Make
        character_add = character #makes a placeholder of original character to add to list later
        character = character.split(" - ") #splits naming convention to isolate level indicator
        l_value = character[3] #can't be character because it changes the attribute of character, which later referneced,
        if l_value == "Living": #filters out dead characters
            character_list.append(character_add)
            character = character[2] #selects the character level
            living_test.append(character)
            character = character.strip("lv. ") #removes lv. from name
            split_list_4lvl.append(character) #adds to the split level list
            
    
    for lvl in split_list_4lvl:
        #compares the level number for character to the provided fight level. If matches, add to eligable list. If not, skip to the next character. 
        if int(split_list_4lvl[counter]) == event["fight_level"]:
            eligable_f.append(character_list[counter]) 
            counter += 1
        else: 
            counter += 1
    
    '''
    part 2
    '''
    
    #select 2 random numbers that are not equal. Can amend this should a rank up battle option be introduced, first check the battle type,
    #if rank up, battle type = fighter level +1. If battle type != to fighter level, they CAN be the same number.
    #this evaluation will first be made in part 1 and then each random number will look at a seperate list. They will be the same list if 
    #battle type == fighter level.
    
    random_num_f1 = random.choice(eligable_f)
    random_num_f2 = random.choice(eligable_f)
    
    while random_num_f2 == random_num_f1: #ensures that F1 cant be F2
        random_num_f2 = random.choice(eligable_f)
    
    return {
        "target_record1": random_num_f1,
        "target_record2": random_num_f2
    }


