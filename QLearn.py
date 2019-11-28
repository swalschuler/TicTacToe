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





def updateQTable(reward, history):
    nextQ = history.pop()
    updateQState(nextQ[0], nextQ[1], [0], reward)
    while history:
        q = history.pop()
        updateQState(q[0], q[1], QTable[nextQ[0]], 0)
        nextQ = q
    print(QTable)
