# This project is originally built in AWS Lambda.

this project uses SmartSuite as a database. Through Make automation and integration, SmartSuite passes records to Lambda were I manipulate the data through Python. 

These files represent the Lambda code, and are left in that syntax, but created outside of Lambda for simplicity. 

The project's function is to create a character from a specific sheet using logic in Python to fill out the data. Chat GPT is also used to to fill in more narrative elements. A webhook from Make triggers the sequence (from a "character sheet") and then the "Character Creation" function is executed. 
- basic stats such as HP, race, class, etc. are selected
- origin is selected 
- world constraints are then implemented for narrative purposes (this invovled funning functions to grant specific narrative constraints to each character for backstory purposes).
- Chat GPT then creates a character backstory and name using the data and constraints for each character

Eventually, these character records will engage in battle. Every "living" character is tied to the battle record, which through a webhook, triggers a Make automation. This executes the "Random Number" function to select which records are going to be battling.

Finally, the battle script is exectued which calculates all the numbers. Narrative elements are then created by Chat GPT. 