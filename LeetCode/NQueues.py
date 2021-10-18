# N = 4
# #chessboard
# #NxN matrix with all elements 0
# board = [['.']*N for _ in range(N)]

# def is_attack(i, j):
#     #checking if there is a queen in row or column
#     for k in range(0,N):
#         if board[i][k]=='Q' or board[k][j]=='Q':
#             return True
#     #checking diagonals
#     for k in range(0,N):
#         for l in range(0,N):
#             if (k+l==i+j) or (k-l==i-j):
#                 if board[k][l]=='Q':
#                     return True
#     return False

# def N_queen(n):
#     #if n is 0, solution found
#     if n==0:
#         return True
#     for i in range(0,N):
#         for j in range(0,N):
#             '''checking if we can place a queen here or not
#             queen will not be placed if the place is being attacked
#             or already occupied'''
#             if (not(is_attack(i,j))) and (board[i][j]!='Q'):
#                 board[i][j] = 'Q'
#                 #recursion
#                 #wether we can put the next queen with this arrangment or not
#                 if N_queen(n-1)==True:
#                     return True
#                 board[i][j] = '.'

#     return False

# N_queen(N)
# for i in board:
#     print (i)
def solveNQueens(n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
    result = []
    DFS([],[],[])
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

res = solveNQueens(4)
print(res)


