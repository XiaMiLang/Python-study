# secret_word = "giraffe"
# guess = ""
# guess_count =0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count+=1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of Guesses, YOU LOSE!")
# else:
#     print("You win!")


# secret_word = "giraffe"
# guess = ""
# guess_limit = 3
# guess_count = 0
# while guess!=secret_word and guess_limit<=3 :
#     guess = input("Please guess: ")
#     if secret_word == guess:
#         print("you win")
#     else:
#         guess_count +=1
#         if guess_count == guess_limit:
#             print("out of guesses, you lose! ")
#             break


secret_word = "giraffe"
guess_limit = 3
guess_count = 1
guess = ""
while guess_count<=guess_limit and guess!=secret_word:
    guess = input("Please guess: ")
    guess_count +=1
if secret_word == guess:
    print("Good guess, You Win!")
if guess_count > guess_limit:
    print("Sorry, you are out of guesses")