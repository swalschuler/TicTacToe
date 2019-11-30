from random import randint

# Q-Learning variables

# Higher value means learns "faster" (values new information more)
LEARNING_RATE = .9
# Higher values long term, lower values immediate
DISCOUNT_FACTOR = 1
REWARD = 1

QTable = {}

# State given as board as a string
# Action = which move did I make (num b/w 0 and 8)
def updateQState(state, action, nextQs, reward):
    if state not in QTable:
        QTable[state] = [0] * 9

    qCurrent = QTable[state][action]

    a = LEARNING_RATE
    g = DISCOUNT_FACTOR
    r = reward
    maxQ = max(nextQs)

    q = (1 - a) * qCurrent
    q = q + a * (r + g * maxQ)

    QTable[state][action] = q

def chooseMove(state, training):
    if state in QTable:
        move = QTable[state].index(max(QTable[state]))
    else:
        move = randint(0, 8)
    row = int(move / 3)
    col = move - (row * 3)
    return row, col

def updateQTable(reward, history):
    nextQ = history.pop()
    updateQState(nextQ[0], nextQ[1], [0], reward)
    while history:
        q = history.pop()
        updateQState(q[0], q[1], QTable[nextQ[0]], 0)
        nextQ = q

def saveQTable():
    with open('qtable.txt', 'w') as f:
        for entry in QTable:
            f.write(entry + ": " + str(QTable[entry]) + '\n')
