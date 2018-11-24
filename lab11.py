#Lab 11
#Team 10 - M. Mariscal, C. Piwarski, W. Robleh

# One object of Class Room represents a room in the game map
class Room:

    # Constructor method for class Room
    def __init__(self, name='', desc='', exits=''):
        self.name = name
        self.desc = desc
        self.exits = exits
        self.beenVisited = False

    # This method returns the name of the room
    def getName(self):
        return self.name

    # This method returns the description of the room
    def getDesc(self):
        return self.desc

    # This method returns the exits of the room
    def getExits(self):
        return exits

    # String method for class Room
    def __string__(self):
        return name + ' ' + desc + ' ' + exits

    # This method sets the name of the room
    def setName(self, name):
        self.name = name

    # This method sets the description of the room
    def setDesc(self, desc):
        self.desc = desc

    # This method sets the exits for the room
    def setExits(self):
        self.exits = exits

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

    def getLocation(self):
        return self.location

# Main function for the game
def Main():

    # Create map and player | Test Classes
    player1 = Player()
    descCell = 'A cold, lonely jail cell'
    room1 = Room('cell', descCell, 'n')
    player1.setLocation(room1)
    commands = ['examine', 'n', 's', 'w', 'e']

    gameWon = False

    while gameWon != True:

        print player1.getLocation().getName()
        print player1.getLocation().getDesc()
        input = requestString('Which way to go?')

        if input == 'n':
            gameWon = True
            print 'Congratulations, you escaped!'
    # Put in a loop that checks if the player got to the exit
    # If they did, then the loop ends and they win.
