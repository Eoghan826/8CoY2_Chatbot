
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
print(HANGMANPICS[0])
print("This is hangman! Hangman will be hanged if you get too many letters wrong.")
secretword = input("what is your secret word? ")
print ("\n"*100)
showword = " " * len (secretword)
guess = input ("what is your guess? ")
# do this automatically
tempShowword = ""
count = 0
for letter in secretword:
    if letter == guess: # it's the same!
        print ("Yippee! You got a letter correct!")
        print ("So far your word is ")
        tempShowword += guess
    else:
        if list (showword) [count] == "_":
            tempShowword += "-"
        else:
            tempShowword += list (showword) [count]
        count += 1
showword = tempShowword
print (showword)
