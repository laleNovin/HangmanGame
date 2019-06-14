# hang man game
import random


def evaluate_entered_letter(some_char):  # check 1 letter and check data type(letter/number/sign)
    if len(some_char) != 1:
        print("Opss!...enter just 1 letter, try again!")
        return False
    elif ord(some_char) not in range(97, 123):
        print("Opss!...enter a letter a-z or A-Z, try again!")
        return False
    else:
        return True


def is_or_not(char, my_word): # is the guessed char in the word or not?
    if char in my_word:
        return True
    else:
        return False


def random_word():
    word_list = ["happy"]  # select a random word for user to guess "hangout", "chicken", "english", "goodbye"
    word = random.choice(word_list)
    char_len = len(word)
    number_of_possible_guess = char_len - 2  # limit user's guesses
    return word, char_len, number_of_possible_guess


def show_char(word, new_word, char):  # to show user position of guessed letter if he has guessed sth True up to now
    new_word = list(new_word)
    for i in range(len(word)):
        if char == word[i]:
            new_word[i] = char
    return new_word  # list


main_word = random_word()[0]
char_len = random_word()[1]
number_of_possible_guess = random_word()[2]
print("we have a word with " + str(char_len) + " characters")
print("you can try just " + str(number_of_possible_guess) + " times")
print("Notice; you will have an extra chance to try for every True guesses")
temp_word = list("*" * len(main_word))
try_number = 1
# star =
while try_number <= number_of_possible_guess:
    print("your try number is: " + str(try_number))
    guessed_letter = str((input("guess a letter: "))).lower()
    if evaluate_entered_letter(guessed_letter):
        if is_or_not(guessed_letter, main_word):
            try_number -= 1
            print("there is < " + str(main_word.count(guessed_letter)) + " > of your guessed letter in this word")
            whole_word = show_char(main_word, temp_word, guessed_letter)
            temp_word = "".join(whole_word)
            print("you can see where your guessed letter is in the word:")
            print(temp_word)
            guessed_word = input("if you can, guess the whole word now: ")
            if guessed_word == "".join(main_word):
                print("Good Job!")
                break
            else:
                if try_number == number_of_possible_guess:
                    print("you are out of number of try, the word was: ", "".join(main_word))
                    break
                else:
                    print("Not True")
        else:
            if try_number == number_of_possible_guess:
                last_guess = input("you are out of number of try, you should guess the whole word now: ")
                if last_guess == "".join(main_word):
                    print("Good Job!")
                    break
                else:
                    print("Not True")
                    print("the word was: ", "".join(main_word))
                    break
            else:
                print("your guessed letter is not in the word, try again!")
    else:
        try_number -= 1
    try_number += 1



