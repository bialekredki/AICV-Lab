import numpy

MAZE = numpy.array([['W','W','W','O','O','O','W','W'],
                   ['W','O','O','O','W','O','W','W'],
                   ['W','O','W','W','W','O','W','W'],
                   ['O','O','O','O','W','G','W','W'],
                   ['O','W','W','W','W','O','W','W'],
                   ['O','W','W','O','O','O','W','W'],
                   ['O','W','W','O','W','W','W','W'],
                   ['S','O','O','O','W','W','W','W']])


def checkForPath(maze,position):
    xd = (-1,1)
    res = []
    for x in xd:
        val1 = maze[position[0]+x,position[1]]
        val2 = maze[position[0],position[1]+x]
        if val1 != 'W':
            res.insert((position[0]+x,position[1]))
        elif val2 != 'W':
            res.insert((position[0],position[1]+x))
    if len(res) > 0: return res
    return -1

def checkForGoal(maze,position):
    if maze[position[0],position[1]] == 'G':
        return True
    return False





