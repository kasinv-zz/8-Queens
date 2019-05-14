from datetime import datetime as dt

r8 = range(8)
def check_diag(X):
    ret_val = True

    for i in X:
        for j in X:
            if i != j and abs(i[0]-j[0]) == abs(i[1]-j[1]):
                return False
    return ret_val


def print_board(board):
    S = ''
    for i in r8:
        s = (str(x).replace('0', '.').replace('1', 'Q') for x in board[i])
        S = S + ' '.join(s) + "\n"
    return S

if __name__ == "__main__":

    start = dt.now()
    answer = []
    cols = {0,1,2,3,4,5,6,7}
    for c0 in r8:
        for c1 in r8:
            for c2 in r8:
                for c3 in r8:
                    for c4 in r8:
                        for c5 in r8:
                            for c6 in r8:
                                for c7 in r8:

                                    q = cols - {c0,c1,c2,c3,c4,c5,c6,c7}

                                    # no overlapping columns
                                    if len(q) == 0:
                                        # set (row, col) coordinates
                                        x = [(0,c0), (1,c1), (2,c2), (3,c3),
                                             (4,c4), (5,c5), (6,c6), (7,c7)]

                                        # diagonality check
                                        if check_diag(x):
                                            board = [[0 for a in r8] for b in r8]
                                            board[0][c0] = 1
                                            board[1][c1] = 1
                                            board[2][c2] = 1
                                            board[3][c3] = 1
                                            board[4][c4] = 1
                                            board[5][c5] = 1
                                            board[6][c6] = 1
                                            board[7][c7] = 1
                                            answer.append(board)
#                                            print(". ", sep='',end='')

    print()
    end = dt.now()
    
    print("# of 8 Queens solutions = {}".format(len(answer)))
    print("Elapsed Time = {}".format(end-start))
    
    while True:
        p = input("print solution? G(rid), A(rray), F(ile), Q(uit) => ")
        print()
        s = 0
        if p.lower() == "g":
            for a in answer:
                print("Solution# {}".format(s+1))
                sp = print_board(a)
                print(sp)
                s += 1
                if s%3 == 0:
                    input("Press <enter> to continue...")
        elif p.lower() == "a":
            for a in answer:
                x = []
                for i in r8:
                    for j in r8:
                        if a[i][j] == 1:
                            x.append((i+1, j+1))
                print("Solution# {:2d} = {}".format(s+1,x))
                s += 1
                if s%10 == 0:
                    input("Press <enter> to continue...")

        elif p.lower() == "f":
            f = open("8queens.txt", "w")

            for a in answer:
                x = []
                for i in r8:
                    for j in r8:
                        if a[i][j] == 1:
                            x.append((i+1, j+1))
                line = ("{:2d}\t{}\n".format(s+1,x))
                f.writelines(line)            
                s += 1
            f.close()

        elif p.lower() == "q":
            break
        else:
            pass
