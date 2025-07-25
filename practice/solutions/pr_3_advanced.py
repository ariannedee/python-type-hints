"""Rock paper scissors game"""
import random
from dataclasses import dataclass
from time import sleep
from typing import Literal, Protocol, TypeVar, ClassVar, Optional

Move = Literal["rock", "paper", "scissors"]
MOVES: list[Move] = ["rock", "paper", "scissors"]

Winner = Optional[Literal[1, 2]]

@dataclass
class RoundResult:
    player_1_move: Move
    player_2_move: Move
    winner: Winner

    def display(self) -> str:
        if self.winner == 1:
            return f"{self.player_1_move.capitalize()} beats {self.player_2_move}"
        elif self.winner == 2:
            return f"{self.player_2_move.capitalize()} beats {self.player_1_move}"
        else:
            return "Tie"

class Player(Protocol):
    name: str

    def choose_move(self) -> Move: ...


class BotPlayer:
    counter: ClassVar[int] = 1

    def __init__(self) -> None:
        self.name = f"Computer {BotPlayer.counter}"
        BotPlayer.counter += 1

    def choose_move(self) -> Move:
        choice = random.choice(MOVES)
        print(f"{self.name} chose {choice}")
        sleep(1)
        return choice


class HumanPlayer:
    def __init__(self, name: str) -> None:
        self.name = name

    def choose_move(self) -> Move:
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


def beats(m1: Move, m2: Move) -> bool:
    return ((m1 == "rock" and m2 == "scissors") or
            (m1 == "paper" and m2 == "rock") or
            (m1 == "scissors" and m2 == "paper"))

T = TypeVar("T", bound=Player)

class Game:
    def __init__(self, player1: Player, player2: Player, best_of=3):
        self.player_1 = player1
        self.player_2 = player2
        self.best_of = best_of
        self.score = [0, 0]
        self.history: list[RoundResult] = []

    def play_round(self) -> RoundResult:
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
        result = RoundResult(player_1_choice, player_2_choice, winner)
        self.history.append(result)

        return result

    @property
    def score_display(self) -> str:
        return f"{self.score[0]} - {self.score[1]}"

    def play_game(self):
        while sum(self.score) < self.best_of:
            result = self.play_round()
            print(f"{self.score_display}: {result.display()}")
        if self.score[0] > self.score[1]:
            print(f"{self.player_1.name} wins!")
        else:
            print(f"{self.player_2.name} wins!")

    def display_history(self):
        for result in self.history:
            print(f"{result.player_1_move}, {result.player_2_move} -> {result.winner}")


if __name__ == "__main__":
    game = Game(BotPlayer(), BotPlayer())
    game.play_game()
    game.display_history()