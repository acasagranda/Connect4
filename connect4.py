#plays 2D list that keeps track of player 1 and player 2 moves
#turn flips between player 1 and player 2
#totalturns keeps track of total number of moves


plays = [[0 for c in range(7)] for r in range(6)]
turn = 1
winner = False
totalturns = 0
#board size
rows,cols=6,7


#print out the game board
def printboard():
  def printrow(pstr):
    print("\t",end="")
    for col in range(cols):
        print(pstr, end = "")

  print(f"\n\033[1m           CONNECT 4\033[0m\n")
  print("\t",end="")

  for col in range(cols):
    print(" "+str(col+1),end="")

  print("")
  printrow(" v")
  print("")
  
  for row in range(rows):
    printrow("+-")
    print("+")
    print("\t",end="")
    for col in range(cols):
      print("|", end = "")
      if plays[row][col]==0:
        print(" ", end = "")
      elif plays[row][col]==1:
        print("X", end = "")
      else:
        print("O", end = "")
    print("|")

  printrow("+-")
  print("+")
  print("")


#input col choice - check if appropriate
def taketurn():
  goodchoice = False
  
  #turn doesn't end if player chooses a full column or puts in a strange input
  while not goodchoice:
    input_choice = input(f"Player {turn}, choose a column to play your next piece: ")

    #check to see if input is a number
    if str.isnumeric(input_choice) and 1<= int(input_choice)<=cols:
      choice = int(input_choice)
      goodchoice=True
     
    if goodchoice:
        if plays[0][choice-1]!=0:
            goodchoice = False
            print("This column is full.  Try again.")
    else:
        print("This is not a valid choice.  Try again.")
  #enter move in correct row
  for row in range(rows-1,-1,-1):
    if plays[row][choice-1]==0:
        plays[row][choice-1]=turn
        break
        
    
      
    
#See if last move makes 4 in a row  
def checkforwinner():
  winner=False
  #check rows and cols
  maxlen=max(rows,cols)
  for row in range(maxlen):
    if winner:
      break
    runr=0
    runc=0
    for col in range(maxlen):
      if row<rows and col<cols:
        if plays[row][col]==turn:
            runr+=1
        else:
            runr = 0
        if runr >3:
            winner = True
            break 
      if row<cols and col<rows:
        if plays[col][row]==turn:
            runc+=1
        else:
            runc = 0
        if runc >3:
            winner = True
            break 
  #check diagonals
  if not winner:
    for rowstart in range(3,rows):
      if winner:
        break
      runr=0
      runl=0
      col=0
      row=rowstart
      while row>=0 and col<cols:
        if plays[row][col]==turn:
          runr +=1
          if runr >3:
            winner = True
            break 
        else:
          runr = 0
        if plays[row][cols-1-col]==turn:
          runl+=1
          if runl>3:
            winner=True
            break
        else:
          runl = 0
        row-=1
        col+=1
  if not winner:
    for colstart in range(1,cols-3):
      if winner:
        break
      runr=0
      runl=0
      row=rows-1
      col=colstart
      while row>=0 and col<cols:
        if plays[row][col]==turn:
          runr +=1
          if runr >3:
            winner = True
            break 
        else:
          runr = 0
        if plays[row][cols-1-col]==turn:
          runl+=1
          if runl>3:
            winner=True
            break
        else:
          runl = 0
        row-=1
        col+=1
  return winner
     
    
 


      


printboard()
while not winner:
  taketurn()
  if totalturns>=6:
    winner=checkforwinner()
  printboard()
  turn=3-turn
  totalturns+=1
  if totalturns == rows*cols:
    break
  
  

print("**********************************")

if winner:
  print(f"\tPlayer {3-turn}, you won!")
else:
  print("\tWell matched -- you TIE!")
print("**********************************")
print("")