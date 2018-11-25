#Lab 11
#Team 10 - M. Mariscal, C. Piwarski, W. Robleh

# One object of Class Room represents a room in the game map
class Room:

    # Constructor method for class Room
    def __init__(self, name='', desc='', north=None, south=None, \
        west=None, east=None):
        self.name = name
        self.desc = desc
        self.beenVisited = False

        # set exits
        self.north = north
        self.south = south
        self.west = west
        self.east = east

    # This method returns the name of the room
    def getName(self):
        return self.name

    # This method returns the description of the room
    def getDesc(self):
        return self.desc

    # This method returns the exit to the room based on the given direction
    def getExit(self, direction):
        if direction == 'n':
            return self.north
        elif direction == 's':
            return self.south
        elif direction == 'e':
            return self.east
        elif direction == 'w':
            return self.west
        else:
            return None

    # String method for class Room
    def __string__(self):
        return name + ' ' + desc + ' ' + exits

    # This method sets the name of the room
    def setName(self, name):
        self.name = name

    # This method sets the description of the room
    def setDesc(self, desc):
        self.desc = desc

    # This method sets the north exit for the room
    def setNorth(self, room):
        self.north = room

    # This method sets the south exit for the room
    def setSouth(self, room):
        self.south = room

    # This method sets the east exit for the room
    def setEast(self, room):
        self.east = room

    # This method sets the west exit for the room
    def setWest(self, room):
        self.west = room
        
    
    

# Class Player represents the player character
class Player:

    # Constructor method for Class Player
    def __init__(self, inventory=''):
        self.inventory = inventory
        self.location = None

    # This method returns the contents of the player's inventory
    def getInventory(self):
        return self.inventory

    # This method sets the location of the player
    def setLocation(self, location):
        self.location = location

    # This method returns the room that the player is currently in
    def getLocation(self):
        return self.location

# Main function for the game
def Main():

    # Create Map 
    descCell = 'A cold, lonely jail cell. The gate is open to the north'
    descHall = 'The hallway of a prison. To the south there is a jailcell. \
        To the east is the kitchen.'
    descKitchen = 'The kitchen for the prison. Hall is still to the West. Door to North and East!'
    descCloset = 'Closet in the Kitchen. You are in the wrong location!'
    twoHall = 'Second Hallway, you have the option of a door to your East and South!'
    
    threeHall = 'Entering a hallway with a door to your North and East?'
    twoCell = 'Entering another Cell.'
    
    guardRoom = 'You enter and see about three guards. What should you do now?'
    endDescription = 'This is the exit. Happy making it out Alive!'
    
    room1 = Room('cell', descCell)
    room2 = Room('Hall', descHall)
    room3 = Room('Kitchen', descKitchen)
    room4 = Room('Closet', descCloset)
    room5 = Room('2nd Hall', twoHall)
    room6 = Room('2nd Cell', twoCell)
    room7 = Room('3rd Hall', threeHall)
    room8 = Room('Guard Room', guardRoom )
    room9 = Room('Exit', endDescription)
    
    
    # Connect Rooms
    room1.setNorth(room2)
    room2.setSouth(room1)
    room2.setEast(room3)
    room3.setWest(room2)
    room3.setNorth(room4)
    room4.setSouth(room3)
    
    room3.setEast(room5)
    room5.setWest(room3)
    room5.setSouth(room6)#entering second cell
    room6.setNorth(room5) #would like this to be a gameOver later on - Wais
    room5.setEast(room7)#entering third hallway
    room7.setWest(room5)
    
    room7.setNorth(room8)
    room7.setEast(room9)

    # Create Player
    player1 = Player()
    player1.setLocation(room1)

    # Test Classes
    

    # Define Extra Variables
    commands = ['examine', 'n', 's', 'w', 'e', 'get']

    gameWon = False

    # Main game loop
    while gameWon != True:

        try:
            printNow(player1.getLocation().getName())
            printNow(player1.getLocation().getDesc())
            input = requestString('Which way to go?')
            player1.setLocation(player1.getLocation().getExit(input))
        except:
            printNow('There is no exit in that direction')
            break #to Stop Error

        if input == 'quit':
            gameWon = True
            print 'Congratulations, you escaped!'
       
    # Put in a loop that checks if the player got to the exit
    # If they did, then the loop ends and they win.
