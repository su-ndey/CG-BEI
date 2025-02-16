import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLUE
from checkers.game import Game
from minimax.algorithm import minimax
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col
def choose_difficulty():
    print("Choose Difficulty Level:")
    print("1: Easy")
    print("2: Medium")
    print("3: Hard")
    while True:
        try:
            choice = int(input("Enter choice (1-3): "))
            if choice == 1:
                return 1  # Easy
            elif choice == 2:
                return 2  # Medium
            elif choice == 3:
                return 3   #Hard
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    depth = choose_difficulty()  
    while run:
        clock.tick(FPS)
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), depth, WHITE, game)
            game.ai_move(new_board)
        if game.winner() is not None:
            print(f"The winner is {game.winner()}!")
            pygame.time.delay(3000)  
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        game.update()
    pygame.quit()
main()