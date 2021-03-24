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

import sys

# sys.argv

def run(inFile):
    with open(inFile, 'r') as f:
        lines = f.readlines()

    pairs = []
    try:
        pairs = [l.strip().split(' ') for l in lines]
    except:
        print('Invalid input file format')
    
    processed = []
    for p in pairs:
        processed.append(getSeats(p))


    with open('output.txt', 'w') as f:
        for p in processed:
            f.write(p[0] + ' ' + p[1] + '\n')


#      [[ Screen ]]
# A ssssssssssssssssssss
# B ssssssssssssssssssss
# C ssssssssssssssssssss
# D ssssssssssssssssssss
# E ssssssssssssssssssss
# F ssssssssssssssssssss
# G ssssssssssssssssssss
# H ssssssssssssssssssss
# I ssssssssssssssssssss
# J ssssssssssssssssssss


def getSeats(pair):
    orderNumber = pair[0]
    seats = pair[1]
    return pair



try:
    run(sys.argv[1])
except Exception as e:
    print(e)