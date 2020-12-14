file = open("words.txt", "r")
word_list_total = file.read().upper().split()
easy_level_words = []
normal_level_words = []
hard_level_words = []


for word in word_list_total:
    if len(word) >= 4 and len(word) <= 6:
        easy_level_words.append(word)
    if len(word) >= 6 and len(word) <= 8:
        normal_level_words.append(word)
    if len(word) >= 8:
        hard_level_words.append(word)

while True:
    difficulty = input('Welcome to the game! Choose difficulty: easy, normal, or hard: ')
    if difficulty != "easy" and difficulty != "normal" and difficulty != "hard":
        continue
    else:
        break
difficulty_selected = None
if difficulty == "easy":
    difficulty_selected = easy_level_words
elif difficulty == "normal":
    difficulty_selected = normal_level_words
elif difficulty == "hard":
    difficulty_selected = hard_level_words

import random
test_word = random.choice(difficulty_selected)
test_word_list = [letter for letter in test_word]
max_guesses = 8
display_word = ['_' for letter in range(len(test_word))]
already_guessed = []



def gameplay(test_word, max_guesses):
    # print(test_word)
    print(" ".join(display_word))
    
    guess = input('Enter your guess: ')
    if guess in test_word:
        for index in range(len(test_word)):
            if guess == test_word[index]:
                display_word[index]=guess
                already_guessed.append(guess)
        return True

    else:
        already_guessed.append(guess)
        print(f'Remember, you have already guessed these letters! {already_guessed}')
        return False



def game_loop(display_word, test_word_list, max_guesses):
    max_guesses = 8
    while display_word != test_word_list and max_guesses >0:
        correct_guess = gameplay(test_word_list, max_guesses)
        if not correct_guess:
            max_guesses -=1
            print(f'\U0001F922 You have {max_guesses} guesses left \U0001F922')
        # elif guess in already_guessed:
        #     print('you already guessed that')
        
    else:
        
        print('The Game is Over')
        print(f'The correct word was {test_word}')
game_loop(display_word, test_word_list, max_guesses)

