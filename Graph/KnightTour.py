def validMoves(curr, n):
    
    moves_d = [(1,2), (2,1), (1,-2), (-2,1), (-1,2), (2,-1), (-1,-2), (-2,-1)]
    moves = [tuple(map(sum, zip(curr,d))) for d in moves_d]
    moves = list(filter(lambda d: d[0] >= 0 and d[0] < n and d[1] >= 0 and d[1] < n, moves))
    
    return moves

def printMatrix(matrix):
    for r in matrix:
        print(r)

def dfsUtil(matrix, curr, moveCount, n):
    i, j = curr
    matrix[i][j] = moveCount
    #print(len(visited))
    solutionFound = False

    if moveCount == n * n:
        printMatrix(matrix)
        return True
    
    moves = validMoves(curr, n)
    for x,y in moves:
        if matrix[x][y] == 0:
            solutionFound = dfsUtil(matrix, (x,y), moveCount + 1, n)
            if solutionFound:
                break 
                       
    if not solutionFound:
        matrix[i][j] = 0

    return solutionFound

def knightTour(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    curr = (0,0)
    moveCount = 1
    solutionFound = dfsUtil(matrix, curr, moveCount, n)
    #print(len(visited))
    #printMatrix(matrix)

    if not solutionFound:
        print("There is no solution to this Knight Tour problem")

if __name__ == "__main__":
    knightTour(8)
    