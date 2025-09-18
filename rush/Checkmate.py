def Checkmate(board):    
    try:
        board = [list(line) for line in board.strip().split()]
        L = len(board)
        for row in board:
            if len(row) != L:
                print("Fail")
                return                                
        Piece = set("KQRBP.")   
        for r in range(L):                         
            for c in range(L):
                if board[r][c] not in Piece :
                    print("Fail")
                    return       
        found = False
        King = 0
        #find King
        for i in range(L):
            for k in range(L):
                if board[i][k]=="K":
                    K_p = (i,k)
                    King+=1
            if King > 1:
                print("Fail")
                return

        #Rook and Queen
        for i in range(L):
            for k in range(L):
                if board[i][k]=="R" or board[i][k]=="Q":
                    R_p = (i,k)
                    if K_p[0] == R_p[0]:
                        row = K_p[0]
                        start = min(K_p[1], R_p[1]) + 1
                        end   = max(K_p[1], R_p[1])
                        for i in range(start, end):
                            if board[row][i] != ".":
                                break
                            else :
                                print("Success")
                                found = True
                    if K_p[1] == R_p[1]:
                        col = K_p[1]
                        start = min(K_p[0], R_p[0]) + 1
                        end   = max(K_p[0], R_p[0])
                        for i in range(start, end):
                            if board[i][col] != ".": 
                                break
                            else:
                                print("Success")
                                found = True
        #Bishop and Queen
        for i in range(L):
            for k in range(L):
                if board[i][k]=="B" or board[i][k]=="Q":
                    B_p = (i,k)
                    if abs(K_p[0] - B_p[0]) == abs(K_p[1] - B_p[1]):
                        if K_p[0] > B_p[0]:dr = 1
                        else:dr = -1
                        if K_p[1] > B_p[1]:dc = 1
                        else:dc = -1
                        r, c = B_p[0] + dr, B_p[1] + dc
                        
                        while (r, c) != K_p:
                            if board[r][c] != ".":
                                break
                            r += dr
                            c += dc

                        if (r, c) == K_p:
                            print("Success")
                            found = True
        #Pawn
        for i in range(L):
            for k in range(L):
                if board[i][k]=="P":
                    P_p = (i,k)
                    if P_p[0] == K_p[0]+1:
                        if P_p[1]-1 == K_p[0] or P_p[1]+1 == K_p[0]:
                            print("Success")
                            found = True


        if not found:
            print("Fail")                     
    except Exception:
        return

                    
                        