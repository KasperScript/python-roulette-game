import random
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
BLACK_NUMBERS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title_screen():
    title = r"""
    $$$$$$$\  $$$$$$\  $$\      $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\   $$$$$$\
    $$  __$$\$$  __$$\ $$ | $\  $$ |$$  __$$\ $$  _____|$$  _____|$$  _____|$$  __$$\ $$  __$$\
    $$ |  $$ |$$ /  $$ |$$ |$$$\ $$ |$$ |  $$ |$$ |      $$ |      $$ |      $$ |  $$ |$$ /  \__|
    $$$$$$$  |$$$$$$$$ |$$ $$ $$\$$ |$$$$$$$  |$$$$$\    $$$$$\    $$$$$\    $$$$$$$  |\$$$$$$\
    $$  __$$< $$  __$$ |$$$$  _$$$$ |$$  __$$< $$  __|   $$  __|   $$  __|   $$  __$$<  \____$$\
    $$ |  $$ |$$ |  $$ |$$$  / \$$$ |$$ |  $$ |$$ |      $$ |      $$ |      $$ |  $$ |$$\   $$ |
    $$ |  $$ |$$ |  $$ |$$  /   \$$ |$$$$$$$  |$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$$  |\$$$$$$  |
    \__|  \__|\__|  \__|\__/     \__|\_______/ \________|\________|\________|\_______/  \______/
    """
    print(Fore.YELLOW + Style.BRIGHT + title)
    print(Fore.CYAN + "Welcome to the Console Casino! Tonight's game: EUROPEAN ROULETTE!")
    print("-" * 70)

def get_bet_amount(player_cash):
    while True:
        try:
            amount = int(input(f"How much of your {Fore.GREEN}${player_cash} are you willing to risk?\n> "))
            if 0 < amount <= player_cash:
                return amount
            else:
                print(Fore.RED + "Don't get clever! Bet an amount you actually have (and that's > 0).")
        except ValueError:
            print(Fore.RED + "That's not a number. Let's try that again.")

def get_bet_type():
    print("\nWhat are you betting your hard-earned cash on?")
    print("1. A specific number (0-36) " + Fore.YELLOW + "(Pays 35:1)")
    print("2. Color (Red/Black) " + Fore.YELLOW + "(Pays 1:1)")
    print("3. Odd/Even " + Fore.YELLOW + "(Pays 1:1)")
    print("4. Low (1-18) / High (19-36) " + Fore.YELLOW + "(Pays 1:1)")

    while True:
        choice = input("> ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print(Fore.RED + "Just pick an option from 1 to 4, mate.")

def get_bet_details(bet_type):
    if bet_type == '1':
        while True:
            try:
                number = int(input("Alright, name your number (0-36): "))
                if 0 <= number <= 36:
                    return number
                else:
                    print(Fore.RED + "The wheel has numbers from 0 to 36. Try one of those.")
            except ValueError:
                print(Fore.RED + "That doesn't look like a number to me.")

    if bet_type == '2':
        while True:
            color = input("Pick your color (red/black): ").lower()
            if color in ['red', 'black', 'r', 'b']:
                return 'red' if color.startswith('r') else 'black'
            else:
                print(Fore.RED + "Only 'red' or 'black' are options here.")

    if bet_type == '3':
        while True:
            choice = input("Odd or Even? (o/e): ").lower()
            if choice in ['odd', 'even', 'o', 'e']:
                return 'even' if choice.startswith('e') else 'odd'
            else:
                print(Fore.RED + "Just type 'o' for odd or 'e' for even.")

    if bet_type == '4':
        while True:
            choice = input("Low (1-18) or High (19-36)? (l/h): ").lower()
            if choice in ['low', 'high', 'l', 'h']:
                return 'low' if choice.startswith('l') else 'high'
            else:
                print(Fore.RED + "Just type 'l' for low or 'h' for high.")

def spin_animation():
    print("\n" + Fore.MAGENTA + "The croupier spins the wheel...")
    time.sleep(1)
    print(Fore.MAGENTA + "The ball is rolling... clack-clack-clack...")
    time.sleep(1.5)
    print(Fore.MAGENTA + "It's slowing down...")
    time.sleep(2)
    print(Fore.MAGENTA + "And the winner is...")
    time.sleep(0.5)



def play_roulette():
    player_cash = 1000
    clear_screen()
    print_title_screen()

    while player_cash > 0:
        print(f"\nYour current balance: {Fore.GREEN}${player_cash}")
        print("-" * 30)

        bet_amount = get_bet_amount(player_cash)
        bet_type = get_bet_type()
        bet_detail = get_bet_details(bet_type)

        spin_animation()

        winning_number = random.randint(0, 36)

        winning_color = ""
        if winning_number in RED_NUMBERS:
            winning_color = "red"
            print(f"\nThe winning number is: {Fore.RED}{Style.BRIGHT}{winning_number} ({winning_color.upper()})")
        elif winning_number in BLACK_NUMBERS:
            winning_color = "black"
            print(f"\nThe winning number is: {Style.BRIGHT}{winning_number} ({winning_color.upper()})")
        else:
            winning_color = "green"
            print(f"\nThe winning number is: {Fore.GREEN}{Style.BRIGHT}{winning_number} ({winning_color.upper()})")

        winnings = 0
        is_winner = False

        if bet_type == '1' and bet_detail == winning_number:
            winnings = bet_amount * 35
            is_winner = True
        elif bet_type == '2' and bet_detail == winning_color:
            winnings = bet_amount * 1
            is_winner = True
        elif bet_type == '3' and winning_number != 0:
            odd_or_even = 'even' if winning_number % 2 == 0 else 'odd'
            if bet_detail == odd_or_even:
                winnings = bet_amount * 1
                is_winner = True
        elif bet_type == '4' and winning_number != 0:
            low_or_high = 'low' if 1 <= winning_number <= 18 else 'high'
            if bet_detail == low_or_high:
                winnings = bet_amount * 1
                is_winner = True

        if is_winner:
            print(Fore.GREEN + Style.BRIGHT + f"\nYES! You won ${winnings}!")
            player_cash += winnings
        else:
            print(Fore.RED + f"\nOuch. Bad luck. You lose your ${bet_amount}.")
            player_cash -= bet_amount

        if player_cash <= 0:
            print("\n" + Fore.RED + Style.BRIGHT + "GAME OVER! You're broke. The house always wins. See ya!")
            break

        play_again = input("\nFancy another round? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Hope you walked away with a profit! ;)")
            break
        clear_screen()
        print_title_screen()


if __name__ == "__main__":
    play_roulette()
