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
    validMoves = gs.getValidMoves()
    moveMade = False

    loadImages()  # only do this once, before the will loop

    running = True
    sqSelected = ()
    playerClicks = []

    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            # mouse handlers
            elif e.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:  # after 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = ()  # reset users click
                    playerClicks = []
            # key handlers
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_z:  # undo when 'z' is pressed
                    gs.undoMove()
                    moveMade = True

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        pg.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)  # draw squares on the board
    drawPieces(screen, gs.board)  # draw pieces on top of those squares


def drawBoard(screen):
    # colors = [pg.Color('white'), pg.Color('gray')]
    colors = [(242, 216, 183), (181, 136, 100)]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            pg.draw.rect(screen, color, pg.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != '--':
                screen.blit(IMAGES[piece], pg.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == '__main__':
    main()
