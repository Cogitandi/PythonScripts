import random
import sys

def drawMap(board):
    licznik = 0
    
    for i in board.values():
        if licznik % 3 == 0:
            print( ' | ', end='')
            
        print( i+' | ', end='')
        
        if licznik in [2,5]:
            print('')
            
        licznik +=1
    print("")
        
def computerMove(board, computerChar):
    
    position = random.choice(list(board.keys()))
    
    while board.get( position ) != '':
        position = random.choice(list(board.keys()))
    board[position] = computerChar
    
def isPlayable(board):
    isWinner(board, 'x')
    isWinner(board, 'o')
    for i in board.values():
        if i == '':
            return True
    return False

def isWinner(board, char):
    cols = [ ['top-L','mid-L','low-L'],
             ['top-M','mid-M','low-M'],
             ['top-R','mid-R','low-R']
           ]
    rows = [ ['top-L','top-M','top-R'],
             ['mid-L','mid-M','mid-R'],
             ['low-L','low-M','low-R'],
            ]
    diags =[ ['top-L','mid-M','low-R'],
             ['low-L','mid-M','top-R']
           ]

    possible = [ cols, rows, diags]

    for i in possible:
        for j in i:      
            counter=0
            for v in j:
                if board.get(v) != char:
                    break
                else:
                    counter +=1
                if counter == 3:
                    print("\nGracz: "+char+" wygrał grę")
                    sys.exit()  
                    
                    
            
    
                

board = {'top-L':'','top-M':'','top-R':'',
         'mid-L':'','mid-M':'','mid-R':'',
         'low-L':'','low-M':'','low-R':''}

print("Wybierz kim chcesz grać")
print("Wpisz 'x' albo 'o': ", end='')
gracz = input()

while gracz != 'x' and gracz != 'o':
    print(" Mozesz wybrac tylko 'x' albo 'o' ")
    print("Wpisz 'x' albo 'o': ", end='')
    gracz = input()

if gracz == 'x':
    computer = 'o'
else:
    computer = 'x'

print("Komputer gra jako: "+computer) 
print("Komputer zaczyna...")
computerMove(board,computer)

while isPlayable(board):
    print("Wybierz gdzie chcesz sie postawic: ",end='')
    playerMove = input()
    board[playerMove] = gracz
    computerMove(board,computer)
    drawMap(board)
print("Koniec gry")
sys.exit()



    


