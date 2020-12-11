file = open("words.txt", "r")
word_list_total = file.read().upper().split()
# print(word_list_total)


# def easy_level(words):
#     easy_level_words = []
#     for word in words:
#         if len(word) >= 4 and len(word) <= 6:
#             easy_level_words.append(word)
#         # return easy_level_words
#         print(easy_level_words)
# easy_level(word_list_total)

# def normal_level(words):
#     normal_level_words = []
#     for word in words:
#         if len(word) >= 6 and len(word) <= 8:
#             normal_level_words.append(word)
#         return normal_level_words
#         # print(easy_level_words)
# normal_level(word_list_total)

# def hard_level(words):
#     hard_level_words = []
#     for word in words:
#         if len(word) >= 8:
#             hard_level_words.append(word)
#         return hard_level_words
#         # print(easy_level_words)
# hard_level(word_list_total)


# test_word = ['CAT']

# display_word = []


# def gameplay(test_word)
#     while display_word != test_word:
#         guess = input('enter your guess: ')
#         display_word=[]

test_word = 'KEEP'
test_word_list = [letter for letter in test_word]
guess = 'K'
max_guesses = 8
tries = 0
display_word = ['_','_','_','_']
#kind the location of the guess in the test_word

def gameplay(test_word, guess, max_guesses):
    guess = input('Enter your guess: ')
    if guess in test_word:
        for index in range(len(test_word)):
            if guess == test_word[index]:
                display_word[index]=guess
    else:
        max_guesses -= 1
        print(f'you have {max_guesses} guesses left')
        
        
    print(display_word)


def game_loop(display_word, test_word_list, max_guesses):
    while display_word != test_word_list and max_guesses >0:
        gameplay(test_word_list, guess, max_guesses)
        
    else:
        
        print('The Game is Over')
game_loop(display_word, test_word_list, max_guesses)

