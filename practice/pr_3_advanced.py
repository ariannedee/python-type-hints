"""Rock paper scissors game"""
import random
from time import sleep


class BotPlayer:
    counter = 1

    def __init__(self):
        self.name = f"Computer {BotPlayer.counter}"
        BotPlayer.counter += 1

    def choose_move(self):
        choice = random.choice(["rock", "paper", "scissors"])
        print(f"{self.name} chose {choice}")
        sleep(1)
        return choice


class HumanPlayer:
    def __init__(self, name: str) -> None:
        self.name = name

    def choose_move(self):
        while True:
            choice = input(f"{self.name} - rock (r), paper (p) or scissors (s): ").strip().lower()
            if choice == "r":
                return "rock"
            elif choice == "p":
                return "paper"
            elif choice == "s":
                return "scissors"
            else:
                print("  Invalid choice")


def beats(m1, m2) -> bool:
    return ((m1 == "rock" and m2 == "scissors") or
            (m1 == "paper" and m2 == "rock") or
            (m1 == "scissors" and m2 == "paper"))


def result_string(m1, m2, winner):
    if winner is None:
        return "Tie"
    elif winner == 1:
        return f"{m1.capitalize()} beats {m2}"
    elif winner == 2:
        return f"{m2.capitalize()} beats {m1}"
    else:
        return "Invalid result"


class RPSGame:
    def __init__(self, player1, player2, best_of=3):
        self.player_1 = player1
        self.player_2 = player2
        self.best_of = best_of
        self.score = [0, 0]

    def play_round(self):
        player_1_choice = self.player_1.choose_move()
        player_2_choice = self.player_2.choose_move()

        if player_1_choice == player_2_choice:
            winner = None
        elif beats(player_1_choice, player_2_choice):
            winner = 1
            self.score[0] += 1
        else:
            winner = 2
            self.score[1] += 1

        return player_1_choice, player_2_choice, winner

    @property
    def score_display(self) -> str:
        return f"{self.score[0]} - {self.score[1]}"

    def play_game(self):
        while sum(self.score) < self.best_of:
            m1, m2, winner = self.play_round()
            print(f"{self.score_display}: {result_string(m1, m2, winner)}")
        if self.score[0] > self.score[1]:
            print(f"{self.player_1.name} wins!")
        else:
            print(f"{self.player_2.name} wins!")


if __name__ == "__main__":
    game = RPSGame(BotPlayer(), BotPlayer())
    game.play_game()
