import random

Words = ('python', 'david', 'honor', 'room')
word = random.choice(Words)
trigger = 0
wordGuess = '*' * len(word)
wordGuessList = list(wordGuess)
print('Welcome to play Hangman')
def guess_Times():
    try:
        num = int(input('Enter number of choices in which you will guess : '))
        return num
    except ValueError:
        print("Wrong input, Enter a numeric value and try again.")
        num = guess_Times()
        return num
num = guess_Times()
# for x in word:
#     print('*', end=' ')
print('\n You have to guess a word that has ' + str(len(word)) + ' letters : ')
print(wordGuessList)
while num > 0:
    guess = input(str(num) + ' guess remaining : ')
    for x in word:
        if guess == x:
            i = word.index(x)
            trigger = 1
            if wordGuessList[i] == '*':
                wordGuessList[i] = x
            else:
                continue
        else:
            continue
    print(wordGuessList)
    if trigger == 1:
        if "".join(wordGuessList) == word:
            print('You Win the game!')
            break
        trigger = 0
    else:
        num = num-1

if "".join(wordGuessList) != word:
    print('You lose the game! Try Again')










