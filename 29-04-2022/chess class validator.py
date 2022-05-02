def validChessBoard(board):
    piecetype = ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king')
    bkings = 0
    wkings = 0
    blacks = 0
    whites = 0
    bpawns = 0
    wpawns = 0
    bbishops = 0
    wbishops = 0
    brooks = 0
    wrooks = 0
    bqueens = 0
    wqueens = 0
    bknights = 0
    wknights = 0
    for k in board.keys():
        if int(k[0]) > 8 or k[1] not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            print("Chess square index not valid")
            return
    for v in board.values():
        if v == '':
            continue
        if v[0] not in ('b', 'w'):
            print("Colour error: Only black and white pieces are allowed")
            return
        elif v[1:] not in piecetype:
            print(v + "No such piece in chess")
            return
        elif v[0] == 'b':
            #print(v)
            blacks += 1
            if v[1:] == 'pawn':
                bpawns += 1
            elif v[1:] == 'knight':
                bknights += 1
            elif v[1:] == 'bishop':
                bbishops += 1
            elif v[1:] == 'rook':
                brooks += 1
            elif v[1:] == 'queen':
                bqueens += 1
            elif v[1:] == 'king':
                bkings += 1
        elif v[0] == 'w':
            whites += 1
            if v[1:] == 'pawn':
                wpawns += 1
            elif v[1:] == 'knight':
                wknights += 1
            elif v[1:] == 'bishop':
                wbishops += 1
            elif v[1:] == 'rook':
                wrooks += 1
            elif v[1:] == 'queen':
                wqueens += 1
            elif v[1:] == 'king':
                wkings += 1
        if whites <= 16:
            if wpawns > 8:
                print("There cannot be more than 8 white pawns")
                return
            if wknights > 2:
                print("There cannot be more than 2 white knights")
                return
            if wrooks > 2:
                print("There cannot be more than 2 white rooks")
                return
            if wbishops > 2:
                print("There cannot be more than 2 white bishops")
                return
            if wqueens > 1:
                print("There cannot be more than 1 white queen")
                return
            if wkings > 1:
                print("There cannot be more than 1 white king")
                return
        else:
            print("White pieces cannot be more than 16")
            return

        if blacks <= 16:
            if bpawns > 8:
                print("There cannot be more than 8 black pawns")
                return
            if bknights > 2:
                print("There cannot be more than 2 black knights")
                return
            if brooks > 2:
                print("There cannot be more than 2 black rooks")
                return
            if bbishops > 2:
                print("There cannot be more than 2 black bishops")
                return
            if bqueens > 1:
                print("There cannot be more than 1 black queen")
                return
            if bkings > 1:
                print("There cannot be more than 1 black king")
                return
        else:
            print("Black pieces cannot be more than 16")
            return
    print("Valid Chess Board!")


board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}

validChessBoard(board)
        
        
