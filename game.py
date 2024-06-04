from random import randrange
from string import ascii_lowercase

class WordList:
    def __init__(self, filename):
        self.words = []
        self.read_file(filename)
        self.num_words = len(self.words)
    
    def read_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.words.append(line[0:6])
     
    def get_word(self):
        return self.words[randrange(0, self.num_words)]

class ActiveGame:
    def __init__(self, word_list):
        self.num_guesses = 0
        self.guesses = []
        self.evals = []
        self.target_word = word_list.get_word()
        self.game_over = False
        self.win = False
        self.quit_to_main_menu = False
        self.quit_completely = False
        self.word_list = word_list

    def is_valid_guess(self, guess):
        if len(guess) != 6:
            print("invalid entry. please enter a 6-letter word.")
            return False
        for char in guess: # up to -1?
            if char not in ascii_lowercase:
                print("invalid entry. please enter letters only.")
                return False
        if guess not in self.word_list.words:
            print("word not found in dictionary. please try again.")
            return False
        return True

    def print_instructions(self):
        print()
        print("enter a 6-letter guess")
        print("if a letter from the guess is in the correct position in the")
        print("target word, it will be printed back in uppercase.")
        print("if the letter is in the target word but in a different")
        print("position, it will be printed back in lowercase.")
        print("otherwise, \"-\" will be printed")
        print("the correct word must be guessed within 8 tries.")
        print()
        print("alternatively, enter:")
        print("g) to reprint this game's guesses and evals")
        print("m) to return to main menu")
        print("q) to exit completely")
        print("i) to reprint these instructions at any time.")
        print()

    def reprint_guesses(self):
        if self.num_guesses == 0:
            print("no guesses yet")
            return
        print("guess  :  eval ")
        print("------ : ------") 
        for i in range(self.num_guesses):
            print(f"{self.guesses[i]} : {self.evals[i]}")

    def take_guess(self): 
        user_guess = input().lower()
        if user_guess == "i":
            self.print_instructions()
        elif user_guess == "m":
            self.quit_to_main_menu = True
        elif user_guess == "q":
            self.quit_completely = True
        elif user_guess == "g":
            self.reprint_guesses()
        elif not self.is_valid_guess(user_guess):
            pass
        elif self.is_valid_guess(user_guess):
            evaluation = self.eval_guess(user_guess)
            self.guesses.append(user_guess)
            self.evals.append(evaluation)
            if not self.win:
                print(evaluation)
            self.num_guesses += 1

    def eval_guess(self, guess):
        if self.target_word == guess:
            self.win = True
            return self.target_word
        evaluation = ""
        for i in range(6):
            letter = guess[i]
            if self.target_word[i] == letter:
                evaluation += str(letter).upper()
            elif letter in self.target_word:
                evaluation += str(letter).lower()
            else:
                evaluation += "-"
        return evaluation

    def play_again(self):
        print("play again? y/n")
        user_input = input()
        while user_input != "y" and user_input != "n":
            user_input = print("invalid choice")
            print("choose y to play again or n to return to main menu.")
            user_input = input()
        return user_input == "y" 

    def run_game_loop(self):
        self.print_instructions()
        continue_game = True
        while continue_game:
            self.take_guess()
            if self.quit_completely or self.quit_to_main_menu:
                break
            elif self.num_guesses >= 8 and not self.win:
                print(f"you lost. the target word was {self.target_word}")
                self.game_over = True
            elif self.win:
                self.game_over = True
            if self.game_over:
                self.num_guesses = 0
                continue_game = self.play_again()
        self.quit_to_main_menu = True

class MainGame():
    def __init__(self, word_list):
        self.word_list = word_list
        self.game_running = True

    def print_main_menu(self):
        print()
        print()
        print("main menu")
        print()
        print("---------")
        print()
        print("enter your choice")
        print("n.) \t new game")
        print("e.) \t exit")
        print()
        print()

    def get_main_menu_input(self):
        user_input = input().lower()
        while user_input != "n" and user_input != 'e':
            print("choice not accepted. please choose from the following:")
            print("n.) \t new game")
            print("e.) \t exit")
            user_input = input().lower()
        if user_input == "e":
            self.game_running = False
        
    def print_parting_message(self):
        print("thanks for playing. exiting...")

    def run_game(self):
        while True:
            self.print_main_menu()
            self.get_main_menu_input()
            if not self.game_running:
                break
            current_game = ActiveGame(self.word_list) 
            current_game.run_game_loop()
            if current_game.quit_completely:
                break
        self.print_parting_message()

def main():
    print("welcome to the six letter word game.")
    print("loading words...")
    filename = "six_letter_words.txt" 
    word_list = WordList(filename)
    main_game = MainGame(word_list)
    main_game.run_game()

if __name__ == '__main__':
    main()
