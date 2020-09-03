def DisplayBoard():
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#

    s = '''
        +=======================+
        |       |       |       |
        |  %s    |  %s    |  %s    |
        |       |       |       |
        |-------|-------|-------|
        |       |       |       |
        |  %s    |  %s    |  %s    |
        |       |       |       |
        |-------|-------|-------|
        |       |       |       |
        |  %s    |  %s    |  %s    |
        |       |       |       | 
        +=======================+
    ''' %(board['a1'], board['a2'], board['a3'], board['b1'], board['b2'], board['b3'], board['c1'], board['c2'], board['c3'] )

    print(s)

def FieldCheck(move):
    val = []
    for key, value in board.items():
        val.append(value)
    
    if move in val:
        return True
    else:
        return False
    
def EnterMove():
   
    global count

    userMove = int(input("Enter your desired move(1-9): "))

    while True:
        if FieldCheck(userMove):
            break
        else:
            userMove = int(input("Invalid Input! Enter your desired move(1-9): "))        

    for key, value in board.items():
        if userMove == value:
            choice = key
        else:
            continue        
    user = 'O'
    board[choice] = user
    count += 1
    DisplayBoard()
    VictoryFor(user)
    
    
def ComputerMove():

    global count
    
    print("The computer's move:")

    import random

    compMove = random.randint(1,9)
    
    while True:
        if FieldCheck(compMove):
            break
        else:
            compMove = random.randint(1,9)

    for key, value in board.items():
        if compMove == value:
            choice = key
        else:
            continue
    user = 'X'
    board[choice] = user
    count += 1
    DisplayBoard()
    VictoryFor(user)


def DrawMove():
    
    global count, end

    if count == 9:
        print("Game Draw")
        end = 1
        return end
    else:
        return        

def VictoryFor(choice):

#    win categories = (('a1','a2','a3'),('b1','b2','b3'),('c1','c2','c3'), ('a1','b2','c3'),
#                      ('a3','b2','c1'),('a1','b1','c1'), ('a2','b2','c2'), ('a3','b3','c3'))
    global end

    if board['a1'] == choice and board['a2'] == choice and board['a3'] == choice:
        print("Win for", choice, "'s")
        end = 1
        return end

    elif board['b1'] == choice and board['b2'] == choice and board['b3'] == choice:
        print("Win for", choice, "'s")
        end = 1
        return end

    elif board['c1'] == choice and board['c2'] == choice and board['c3'] == choice:
        print("Win for", choice, "'s")
        end = 1
        return end

    elif board['a1'] == choice and board['b2'] == choice and board['c3'] == choice:
        print("Win for", choice, "'s")
        end = 1
        return end

    elif board['a3'] == choice and board['b2'] == choice and board['c1'] == choice:
        print("Win for", choice, "'s")
        end = 1
        return end

    elif board['a1'] == choice and board['b1'] == choice and board['c1'] == choice:
        print("Win for", choice, "'s")
        end = 1
        return end

    elif board['a2'] == choice and board['b2'] == choice and board['c2'] == choice:
        print("Win for", choice, "'s")
        end = 1
        return end

    elif board['a3'] == choice and board['b3'] == choice and board['c3'] == choice:
        print("Win for", choice, "'s")
        end = 1
        return end

    else:
        DrawMove()
        
### The program starts here ###

# definition of the variables
board = {
    "a1" : 1, 
    "a2" : 2,
    "a3" : 3,
    "b1" : 4,
    "b2" : 5,
    "b3" : 6,
    "c1" : 7,
    "c2" : 8,
    "c3" : 9
}
# end of definition 

print("""
Welcome to this exciting game of tic-tac-toe.You will be matched against a random computer.
As you can see from the graphic below, each box is numbered from 1-9.
You will play as O's while the computer will be X's.
""")

DisplayBoard()

print("The computer starts:")

# first computer move

board['b2'] = 'X'
DisplayBoard()

end = 0
count = 1

while end < 1:
    print('--------------------------------------------')  
    EnterMove()
    if end >= 1:
        break
    ComputerMove()
  

print("Game Over")


