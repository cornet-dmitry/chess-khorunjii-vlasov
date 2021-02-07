"""
This class is responsible for storing all the information about the current state of a chess game.
It will also be responsible for determining the valid moves at the current state.
It will also keep a move log.
"""
import sqlite3

from Chess import main


class GameState:

    def __init__(self, firstUserID, secondUserID):
        # Board is an 8x8 2d list, each element of the list has 2 characters
        # The first character represents the color of the piece: 'w' or 'b'
        # The second character represents the type of the piece: 'K', 'Q', 'R', 'B', 'N' or 'P'

        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.moveFunctions = {'p': self.getPawnMoves, 'R': self.getRookMoves, 'N': self.getKnightMoves,
                              'B': self.getBishopMoves, 'Q': self.getQueenMoves, 'K': self.getKingMoves}

        self.whiteToMove = True
        self.moveLog = []
        self.whiteKingLocation = (7, 2)
        self.blackKingLocation = (0, 2)
        self.checkmate = False
        self.stalemate = False
        self.list = []
        self.firstUserID = firstUserID
        self.secondUserID = secondUserID
        self.beforeCountPiece = 32
        self.tempCount = 0

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.countPiece()

        self.whiteToMove = not self.whiteToMove
        # update the king's location if moved
        if move.pieceMoved == 'wK':
            self.whiteKingLocation = (move.endRow, move.endCol)
        elif move.pieceMoved == 'bK':
            self.blackKingLocation = (move.endRow, move.endCol)

    def countPiece(self):
        self.tempCount += 1
        if self.tempCount % (32 - (32 - self.beforeCountPiece)) == 0:
            count = 0
            for i in self.board:
                for j in i:
                    if j != '--':
                        count += 1
            if self.beforeCountPiece - 1 == count:
                self.givenPiece()
            self.beforeCountPiece = count

    def givenPiece(self):
        con = sqlite3.connect("chess.sqlite")
        cur = con.cursor()

        if not self.whiteToMove:
            resultGiven = cur.execute("SELECT Given FROM Users WHERE ID=?", (self.firstUserID,)).fetchall()[0][0]
            resultGiven += 1
            cur.execute(f"""UPDATE Users SET Given={resultGiven} WHERE ID={self.firstUserID}""")
            con.commit()
        else:
            resultGiven = cur.execute("SELECT Given FROM Users WHERE ID=?", (self.secondUserID,)).fetchall()[0][0]
            resultGiven += 1
            cur.execute(f"""UPDATE Users SET Given={resultGiven} WHERE ID={self.secondUserID}""")
            con.commit()

        if self.whiteToMove:
            resultTaken = cur.execute("SELECT Taken FROM Users WHERE ID=?", (self.firstUserID,)).fetchall()[0][0]
            resultTaken += 1
            cur.execute(f"""UPDATE Users SET Taken={resultTaken} WHERE ID={self.firstUserID}""")
            con.commit()
        else:
            resultTaken = cur.execute("SELECT Taken FROM Users WHERE ID=?", (self.secondUserID,)).fetchall()[0][0]
            resultTaken += 1
            cur.execute(f"""UPDATE Users SET Taken={resultTaken} WHERE ID={self.secondUserID}""")
            con.commit()

        con.close()

    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove  # switch turns back
            # update the king's location if needed
            if move.pieceMoved == 'wK':
                self.whiteKingLocation = (move.startRow, move.startCol)
            elif move.pieceMoved == 'bK':
                self.blackKingLocation = (move.startRow, move.startCol)

    def getValidMoves(self):
        moves = self.getAllPossibleMove()

        for i in range(len(moves) - 1, -1, -1):  # when removing from a list go backwards through that list
            self.makeMove(moves[i])
            oppMoves = self.getAllPossibleMove()
            self.whiteToMove = not self.whiteToMove
            if self.inCheck():
                moves.remove(moves[i])
            self.whiteToMove = not self.whiteToMove
            self.undoMove()

        if len(moves) == 0:  # either checkmate or stalemate
            if self.inCheck():
                self.checkmate = True
            else:
                self.stalemate = True
        else:
            self.checkmate = False
            self.stalemate = False

        return moves

    def inCheck(self):
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKingLocation[0], self.whiteKingLocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0], self.blackKingLocation[1])

    def squareUnderAttack(self, row, col):
        self.whiteToMove = not self.whiteToMove  # switch to opponent's turn
        oppMoves = self.getAllPossibleMove()
        self.whiteToMove = not self.whiteToMove  # switch turns back
        for move in oppMoves:
            if move.endRow == row and move.endCol == col:  # square is under attack
                return True
        return False

    def getAllPossibleMove(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0]
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    self.moveFunctions[piece](row, col, moves)
        return moves

    def getPawnMoves(self, row, col, moves):
        if self.whiteToMove:  # white pawn moves
            if self.board[row - 1][col] == '--':  # 1 square pawn advance
                moves.append(Move((row, col), (row - 1, col), self.board))
                if row == 6 and self.board[row - 2][col] == '--':  # 2 square pawn advance
                    moves.append(Move((row, col), (row - 2, col), self.board))
            if col - 1 >= 0:  # captures to the left
                if self.board[row - 1][col - 1][0] == 'b':  # enemy piece to capture
                    moves.append(Move((row, col), (row - 1, col - 1), self.board))
            if col + 1 <= 7:  # captures to the right
                if self.board[row - 1][col + 1][0] == 'b':  # enemy piece to capture
                    moves.append(Move((row, col), (row - 1, col + 1), self.board))

        else:  # black pawn moves
            if self.board[row + 1][col] == '--':  # 1 square pawn advance
                moves.append(Move((row, col), (row + 1, col), self.board))
                if row == 1 and self.board[row + 2][col] == '--':  # 2 square pawn advance
                    moves.append(Move((row, col), (row + 2, col), self.board))
            if col - 1 >= 0:  # captures to the left
                if self.board[row + 1][col - 1][0] == 'w':  # enemy piece to capture
                    moves.append(Move((row, col), (row + 1, col - 1), self.board))
            if col + 1 <= 7:  # captures to the right
                if self.board[row + 1][col + 1][0] == 'w':  # enemy piece to capture
                    moves.append(Move((row, col), (row + 1, col + 1), self.board))

    def getRookMoves(self, row, col, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))  # up, left, down. right
        enemyColor = 'b' if self.whiteToMove else 'w'

        for d in directions:
            for i in range(1, 8):
                endRow = row + d[0] * i
                endCol = col + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:  # on board
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '--':  # empty space valid
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColor:  # enemy piece valid
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                        break
                    else:  # friendly piece invalid
                        break
                else:  # off board
                    break

    def getKnightMoves(self, row, col, moves):
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        allyColor = 'w' if self.whiteToMove else 'b'

        for m in knightMoves:
            endRow = row + m[0]
            endCol = col + m[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:  # on board
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor:  # not an ally piece (empty or enemy piece)
                    moves.append(Move((row, col), (endRow, endCol), self.board))

    def getBishopMoves(self, row, col, moves):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))  # 4 diagonals
        enemyColor = 'b' if self.whiteToMove else 'w'

        for d in directions:
            for i in range(1, 8):
                endRow = row + d[0] * i
                endCol = col + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:  # on board
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '--':  # empty space valid
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColor:  # enemy piece valid
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                        break
                    else:  # friendly piece invalid
                        break
                else:  # off board
                    break

    def getQueenMoves(self, row, col, moves):
        self.getRookMoves(row, col, moves)
        self.getBishopMoves(row, col, moves)

    def getKingMoves(self, row, col, moves):
        kingMoves = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        allyColor = 'w' if self.whiteToMove else 'b'

        for i in range(8):
            endRow = row + kingMoves[i][0]
            endCol = col + kingMoves[i][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:  # on board
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor:  # not an ally piece (empty or enemy piece)
                    moves.append(Move((row, col), (endRow, endCol), self.board))


class Move:
    # maps keys to values
    # key: value

    ranksToRows = {'1': 7, '2': 6, '3': 5, '4': 4,
                   '5': 3, '6': 2, '7': 1, '8': 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                   'e': 4, 'f': 5, 'g': 6, 'h': 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        # print(self.moveID)

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
