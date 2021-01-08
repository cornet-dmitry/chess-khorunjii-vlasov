import pygame as pg
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8  # dimension on a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""Initialize a global dictionary of images. This will be called exactly once in the main"""


def loadImages():
    pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))


"""The main driver for our code. This will handle user input and updating the graphics"""


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color('white'))
    gs = ChessEngine.GameState()
    loadImages()  # only do this once, before the will loop

    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        clock.tick(MAX_FPS)
        pg.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)  # draw squares on the board
    drawPieces(screen, gs.board)  # draw pieces on top of those squares


def drawBoard(screen):
    pass


def drawPieces(screen, board):
    pass


if __name__ == '__main__':
    main()
