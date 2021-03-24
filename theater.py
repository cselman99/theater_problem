# MOVIE THEATER SEATING CHALLENGE #
# * Overview
# * 10 rows x 20 seats
# * maximizes custumer satisfaction / safety 
# *     - (3 seats or one row of spacing required)

# Input Description
# * Order of input represents order of requests
# * Each line contains a reservation identifier (R####) 
# * followed by a space and num. seats requested

# Output Description
# * Each line contains a reservation identifier (R###)
# * followed by a space and comma divided assigned seats

# ! Example Input:
# R001 2
# R002 1
# R003 4

# ! Example Output:
# R001 I2, I3
# R002 F5
# R003 J1, J2, J3, J4

# -------------------------------------------------------------------- #
import os
import sys
import string

# ! Global 2D map of the theater (10 x 20)
ROWS = 10 # Size of ROWS limited by size of alphabet
SEATS = 20

mapTheater = [[0]*SEATS for s in range(ROWS)]
rows = string.ascii_uppercase[:ROWS]
reservations = set()

TICKET_PRICE = 20

def run(inFile, printSeating):
    # read in from input file
    with open(inFile, 'r') as f:
        lines = f.readlines()

    # split identifier and quantity and place in pairs
    pairs = [l.strip().split(' ') for l in lines]
    
    processed = []
    total = 0

    # Find seats for each p in pairs
    for p in pairs:

        if p[0] not in reservations:
            reservations.add(p[0])
        else:
            raise ValueError('Error: Duplicate reservation')
        
        seats = getSeats(p)
        
        if seats is not None:
            processed.append(seats)
            total += int(p[1])
        else:
            processed.append(p[0] + ' None\n')
            if printSeating: # Disabled for testing
                print('Could not find seats for reservation ' + p[0])

    # Write to output file
    with open('output.txt', 'w') as f:
        for p in processed:
            f.write(p)

    # If enabled, print seating chart and path to output document (disabled for testing)
    if printSeating:
        printMap(total)



def getSeats(pair):
    # ! Stategy:
    # * Check in reverse order (back to front for available rows - skip odd rows to allow for 1 row buffer)
    # * Starting from the beginning of that row, check for next available seat (space by 3's)
    if len(pair) != 2:
        raise ValueError('Invalid input file format')

    num = int(pair[1])
    
    # Iterate over the rows starting back to front
    for x in range(len(mapTheater)-1, -1, -2):
        y = 0
        # Starting with the leftmost seat, start traversing the aisle
        while y < len(mapTheater[x])-num+1:
            counter = 0
            # If empty seat found, check following seats for needed space
            if mapTheater[x][y] == 0:
                err = False
                while(counter < num):
                    if mapTheater[x][y + counter] == 1: # Came across a filled seat
                        err = True
                        break
                    counter += 1
                    
                if not err: # There is enough space to place reservation here
                    counter = 0
                    seatList = ''

                    while(counter < num):
                        mapTheater[x][y+counter] = 1 # Mark seats on map as filled
                        seatList += str(rows[x]) + str(y+counter+1) + ', '
                        counter += 1
                    return pair[0] + ' ' + seatList[:-2] + '\n'
            else:
                while y + counter < SEATS and mapTheater[x][y + counter] == 1:
                    counter += 1
                y = y + counter + 3
                    
                    
    return None

# Consider:
# Seats are broken
# Aisle separates seats (no need for 3 seat buffer in given row)
# Different shaped theaters (varying number of seats in each row)

def resetSeating():
    for x in range(len(mapTheater)):
        for y in range(len(mapTheater[x])):
            mapTheater[x][y] = 0

    reservations.clear()


def printMap(total):
    print('')
    print('Total seats sold: ' + str(total) + '/200')
    print('Total revenue: $' + str(total * TICKET_PRICE))

    CRED = '\033[92m'
    BOLD = '\033[1m'
    CEND = '\033[0m'

    print('')
    print(' ' * (SEATS - 3) + '[[ SCREEN ]]')
    print('    ' + '-' * (SEATS * 2 - 1))
    for c, i in enumerate(mapTheater):
        print(BOLD + str(rows[c]) + CEND, end='   ')
        for s in i:
            if s == 1:
                print(CRED + BOLD + str(s) + ' ' + CEND, end='')
            else:
                print(str(s) + ' ', end='')
        print('')

    ab = os.path.abspath(__file__)
    print('\n\nOutput can be found here: ' + os.path.dirname(ab) + '/output.txt')


