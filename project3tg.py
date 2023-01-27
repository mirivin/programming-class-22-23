def start():
    print("Welcome!")
    home()

def home():
    print("You are in your home")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tyour_room\n\tsunroom\n\tbackyard")
    if move.lower() == "your_room":
        your_room()
    elif move.lower() == "sunroom":
        sunroom()
    elif move.lower() == "backyard":
        backyard()
    else:
        print("Invalid entry")
        #TODO: what should happen if they type something else?
        pass

def your_room():
    print("You are in your room")
    print("You have looked around everywhere in your room, and still you've found nothing.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tsunroom\n\tbackyard\n\n")
    if move.lower() == "sunroom":
        sunroom()
    elif move.lower() == "backyard":
        backyard()
    else:
        print("Invalid entry")
        your_room()
        pass

def sunroom():
    print("You are in your sunroom. You look around and find nothing of interest.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tbackyard\n\tyour room")
    if move.lower() == "backyard":
        backyard()
    elif move.lower() == "your room":
        your_room
    else:
        print("Invalid entry")
        sunroom()
        pass

def backyard():
    print("You are in your backyard. You see your dog playing with its toy.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tsunroom\n\tfriends house\n")
    if move.lower() == "sunroom":
        backyard()
    elif move.lower() == "friends house":
        frineds_house()
    else:
        print("Invalid entry")
        backyard()
        pass

def frineds_house():
    print("You arrive at your friends door and his mom lets you in.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tfriends room\n\tbackyard\n")
    if move.lower() == "friends room":
        friends_room()
    elif move.lower() == "backyard":
        backyard()
    else:
        print("Invalid entry")
        frineds_house()
        pass

def friends_room():
    print("You enter your friends room.\nYou: Can I use your basketball shoes I got to go to a game.\n Friend: Sure they are right here.\n CONGRATULATIONS YOU HAVE ACQUIRED SHOES FOR YOUR BASKETBALL GAME!")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tbasketball game")
    if move.lower() == "basketball game":
        bgame()
    else:
        print("Invalid entry")
        friends_room()
    pass

def bgame():
    print("You drop 30 points and win the game!")
    exit()

########
#main
#######
#TODO: Add some global variables

start()
