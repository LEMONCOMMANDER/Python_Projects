import random

def world1_fun(character_traits_from_parent):
    
    character_traits = character_traits_from_parent
    
    if character_traits["World"] == 1:
        if character_traits["Origin"] == "Forest":
            character_traits["Region"] = "Norhaven"
        if character_traits["Origin"] == "Mountains":
            character_traits["Region"] = random.choice(["Norhaven","Esgard"])
        if character_traits["Origin"] == "City":
            character_traits["Region"] = random.choice(["Valoria","Thalindor"])
        if character_traits["Origin"] == "Plains":
            character_traits["Region"] = "Valoria"
        if character_traits["Origin"] == "Desert":
            character_traits["Region"] = random.choice(["Esgard","Thalindor"])
        if character_traits["Origin"] == "Village":
            character_traits["Region"] = random.choice(["Norhaven","Esgard"])
            
        #selects sub-region and home
        if character_traits["Region"] == "Norhaven": #1
            norhaven_regions = {
                                "Frozenpeak Range": ["Hîthloss", "Taur-Amarth", "Tûr-Gelair", "Cûlvarn"],
                                "Whispering Woods": ["Sûlithîr", "Thôr-Dôl", "Tâlbereth", "Bânthalad", "Angrenthorn", "Drû-penin"], 
                                "Frostvale Basin":["Frostvale", "Rathló", "Cûl-awarth", "Kornadûl"]
                                }
            region_key = list(norhaven_regions.keys())
            home_key = list(norhaven_regions.values())
            rnum = random.randint(1,len(region_key)) #length determined by how many sub-regions are present in the region
            
            character_traits["Sub-region"] = region_key[rnum-1] #subtracts 1 to set index starting at 0
            #matches the key index with the selected sub-region | ##selects random location from proper sub-region
            character_traits["Home"] = home_key[rnum-1][random.randint(0,len(home_key[rnum-1])-1)]
            
        
        if character_traits["Region"] == "Valoria": #2
            valoria_regions = {
                                "Eldenmir Plains" : ["Eldenmir", "Orunir", "Celedhren", "Abernil Ael"], 
                                "Caelond Hills" : ["Caelond", "Nim-Er", "Nim-Tád", "Thalion"], 
                                "Ardhon Fortress": ["Ardhon"], 
                                "Green Sea": ["Gwindar", "Londae", "Dagor úrui", "Glír Dór", "Ulin"]
                                }
            region_key = list(valoria_regions.keys())
            home_key = list(valoria_regions.values())
            rnum = random.randint(1,len(region_key)) 
            
            character_traits["Sub-region"] = region_key[rnum-1] 
            character_traits["Home"] = home_key[rnum-1][random.randint(0,len(home_key[rnum-1])-1)]

        
        if character_traits["Region"] == "Thalindor": #3
            thalindor_region = {
                                "Calenmor": ["Calenmor", "Tolond", "The Lorien Stretch"],
                                "Anír Gilith Desert": ["Ardhâl", "Aiwenor Ant Oasis", "Astlant Oasis"],
                                "Herdirnen Bay": ["Herdirnen", "Goronath Port", "Rastrond Port", "Cerch dôl Annui", "Virda Port", "Fán othrond"]
                                }
            region_key = list(thalindor_region.keys())
            home_key = list(thalindor_region.values())
            rnum = random.randint(1,len(region_key)) 
            
            character_traits["Sub-region"] = region_key[rnum-1] 
            character_traits["Home"] = home_key[rnum-1][random.randint(0,len(home_key[rnum-1])-1)]
            
            
        if character_traits["Region"] == "Esgard": #4
            esgard_regions = {
                            "Ironpeak Mountains": ["Onglîn-i-Gorlak"], 
                            "Bleakrock Pass": ["Morfuku Ost", "Pîn Bardh", "Coe Ant", "Fânrist Magor", "Orodcaun"], 
                            "Enders Plateau": ["Tol Eressea"]
                            }
            region_key = list(esgard_regions.keys())
            home_key = list(esgard_regions.values())
            rnum = random.randint(1,len(region_key)) 
            
            character_traits["Sub-region"] = region_key[rnum-1] 
            character_traits["Home"] = home_key[rnum-1][random.randint(0,len(home_key[rnum-1])-1)]
            
            
        print("world 1 function output " + str(type(character_traits)))
        return character_traits