
#Type Hints And Arrows

#help you in debugging , 
#declare a data type for the parameters and declare a data type for the return type
def greeting(name:str) -> str:
    return 'Hello' + name

name: str
age: int



def police_card(age: int):
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive



if police_card(19):
    print("You may pass")
else:
    print("Pay a fine")
