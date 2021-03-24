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
import sys
import string

# ! Global 2D map of the theater (10 x 20)
ROWS = 10 # Size of ROWS limited by size of alphabet
SEATS = 20

mapTheater = [[0]*SEATS for s in range(ROWS)]
rows = string.ascii_uppercase[:ROWS]

TICKET_PRICE = 20

def run(inFile):
    with open(inFile, 'r') as f:
        lines = f.readlines()

    pairs = []
    try:
        pairs = [l.strip().split(' ') for l in lines]
    except:
        print('Invalid input file format')
    
    processed = []
    total = 0

    for p in pairs:
        seats = getSeats(p)
        if seats is not None:
            processed.append(seats)
            total += int(p[1])
        else:
            processed.append([p[0], 'None'])
            print('Could not find seats for reservation ' + p[0])

    with open('output.txt', 'w') as f:
        for p in processed:
            f.write(p[0] + ' ' + p[1] + '\n')


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



def getSeats(pair):
    # ! Stategy:
    # * Check in reverse order (back to front for available rows - skip odd rows to allow for 1 row buffer)
    # * Starting from the beginning of that row, check for next available seat (space by 3's)
    
    num = int(pair[1])
    for x in range(len(mapTheater)-1, -1, -2):
        y = 0
        
        while y < len(mapTheater[x])-num+1:
            counter = 0
            if mapTheater[x][y] == 0:

                err = False
                while(counter < num):
                    if mapTheater[x][y + counter] == 1:
                        err = True
                        break
                    counter += 1
                    
                if not err:
                    counter = 0
                    seatList = ''

                    while(counter < num):
                        mapTheater[x][y+counter] = 1
                        seatList += str(rows[x]) + str(y+counter+1) + ', '
                        counter += 1
                    return (pair[0], seatList[:-2])
                else:
                    print('here')
                    y = y + counter + 3
            else:
                while y + counter < SEATS and mapTheater[x][y + counter] == 1:
                    counter += 1
                y = y + counter + 3
                    
                    
    return None




try:
    #print(mapTheater)
    run(sys.argv[1])
except Exception as e:
    print(e)