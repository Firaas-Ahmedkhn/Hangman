import random
from hangman_words import word_list
import pyttsx3


print("Hi, Welcome to hangman")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hi, Welcome to hang man!")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


from hangman_art import logo
print(logo)


#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)
while not end_of_game:
    print(f"First letter is {chosen_word[0]}")
    guess = input("Guess a letter: ").lower()

    
    if guess in display:
        speak(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        speak(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            speak("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        speak("You win.")

    from hangman_art import stages
    print(stages[lives])

print(chosen_word)