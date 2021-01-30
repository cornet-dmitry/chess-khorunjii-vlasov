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
    animate = True

    loadImages()  # only do this once, before the will loop

    running = True
    sqSelected = ()
    playerClicks = []

    gameOver = False

    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            # mouse handlers
            elif e.type == pg.MOUSEBUTTONDOWN:
                if not gameOver:
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
                        if move in validMoves:
                            gs.makeMove(move)
                            moveMade = True
                            animate = True
                            sqSelected = ()  # reset users click
                            playerClicks = []
                        else:
                            playerClicks = [sqSelected]

            # key handlers
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_z:  # undo when 'z' is pressed
                    gs.undoMove()
                    moveMade = True
                if e.type == pg.K_r:  # reset the board when 'r' is pressed
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    playerClicks = []
                    moveMade = False
                    animate = False

        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1], screen, gs.board, clock)
            validMoves = gs.getValidMoves()
            moveMade = False
            animate = False

        drawGameState(screen, gs, validMoves, sqSelected)

        if gs.checkmate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen, 'Black wins to checkmate')
            else:
                drawText(screen, 'White wins to checkmate')
        elif gs.stalemate:
            gameOver = True
            drawText(screen, 'Stalemate')

        clock.tick(MAX_FPS)
        pg.display.flip()


"""Highlight square selected and moves for piece selected"""


def highlightSquares(screen, gs, validMoves, sqSelected):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):
            s = pg.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)
            s.fill(pg.Color('blue'))
            screen.blit(s, (c * SQ_SIZE, r * SQ_SIZE))
            s.fill(pg.Color('yellow'))

            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (move.endCol * SQ_SIZE, move.endRow * SQ_SIZE))


def drawGameState(screen, gs, validMoves, sqSelected):
    drawBoard(screen)  # draw squares on the board
    drawPieces(screen, gs.board)  # draw pieces on top of those squares
    highlightSquares(screen, gs, validMoves, sqSelected)


def drawBoard(screen):
    global colors
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


"""Animating a move"""


def animateMove(move, screen, board, clock):
    global colors
    coords = []
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 10  # frames to move one square
    framesCount = (abs(dR) + abs(dC)) * framesPerSquare

    for frame in range(framesCount + 1):
        r, c = (move.startRow + dR * frame / framesCount, move.startCol + dC * frame / framesCount)
        drawBoard(screen)
        drawPieces(screen, board)
        color = colors[(move.endRow + move.endCol) % 2]
        endSquare = pg.Rect(move.endCol * SQ_SIZE, move.endRow * SQ_SIZE, SQ_SIZE, SQ_SIZE)
        pg.draw.rect(screen, color, endSquare)

        if move.pieceCaptured != '--':
            screen.blit(IMAGES[move.pieceCaptured], endSquare)
        screen.blit(IMAGES[move.pieceMoved], pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        pg.display.flip()
        clock.tick(120)


def drawText(screen, text):
    font = pg.font.SysFont('Arial', 32, True, False)
    textObject = font.render(text, 0, pg.Color('Black'))
    textLocation = pg.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH / 2 - textObject.get_width() / 2,
                                                     HEIGHT / 2 - textObject.get_height() / 2)
    screen.blit(textObject, textLocation)


if __name__ == '__main__':
    main()
