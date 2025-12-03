
# class Main:
#     def __init__(self):
#         pass
print('Hello World')
Name = ""
Gender = ""
Age = 0
Race = ""
Class = ""

def set_gender():
    global Gender

    char_gender = input("Are you a boy wizard or a girl wizard? ")

    if char_gender.lower() == "boy":
        Gender = "Male"
        print("Ok!")
    elif char_gender.lower() == "girl":
        Gender = "Female"
        print("Ok!")
    else:
        print("Please enter either 'boy' or 'girl'.")
        return set_gender()
def set_name():
    global Name      # use the global variable

    charName = input('What is your character’s name? ')

    confirm = input(f"{charName} — is this your character’s name? Y/N: ").upper()

    if confirm == 'Y':
        Name = charName
        print("Ok!")
    elif confirm == 'N':
        return set_name()   # ask again
    else:
        print("Please enter Y or N.")
        return set_name()
def set_age():
    global Age

    char_age = input("What is your age? ")

    # Validate that input is a number
    if not char_age.isdigit():
        print("Please enter a valid number.")
        return set_age()

    age_num = int(char_age)

    # Age must be at least 1
    if age_num >= 1:
        print(f"Ok! You are {age_num} years old.")
        Age = age_num
    else:
        print("You must be at least 1 year old.")
        return set_age()
def set_race():
    global Race
    Race = input("What is your race? Human, Goblin , Orc , Elf , Dwarf, Cow(Polish)")
    if Race.lower() == "human":
        print("Ok!")
        Race = "Human"
    elif Race.lower() == "goblin":
        print("Ok!")
        Race = "Goblin"
    elif Race.lower() == "orc":
        print("Ok!")
        Race = "Orc"
    elif Race.lower() == "elf":
        print("Ok!")
        Race = "Elf"
    elif Race.lower() == "dwarf":
        print("Ok!")
        Race = "Dwarf"
    elif Race.lower() == "cow":
        print("Ok!")
        Race = "Cow"
    else:
        print("please enter a valid race.")
        return set_race()
def set_class():
    global Class
    char_class = input("What is your class? Knight, Archer , Wizard , or Gamer ")
    if char_class.lower() == "knight":
        Class = "Knight"
        print("Ok!")
    elif char_class.lower() == "archer":
        Class = "Archer"
        print("Ok!")
    elif char_class.lower() == "wizard":
        Class = "Wizard"
        print("Ok!")
    elif char_class.lower() == "Gamer":
        Class = "Gamer"
        print("Ok!")
    else:
        print("please enter a valid class.")
        return set_class()



def start():
    set_gender()
    set_name()
    set_age()
    set_race()
    set_class()

    print(Age)
    print(Name)
    print(Gender)
    print(Race)
    print(Class)
    answer = input(f"Ok! so you are a {Age} years old {Gender} {Race} {Class} , named {Name}? Y/N")
    if answer.lower() == "y":
        return
    elif answer.lower() == "n":
        return start()
    else:
        print("Please enter Y or N.")

start()

# set_gender()
# set_name()
# set_age()
# set_race()
# set_class()
#
# print(Age)
# print(Name)
# print(Gender)
# print(Race)
# print(Class)