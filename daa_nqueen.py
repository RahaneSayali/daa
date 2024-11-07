def solve_nqueen(n, first_queen_col):
    col = set()
    pos_diag = set()  # (r + c) for positive diagonals
    neg_diag = set()  # (r - c) for negative diagonals
    res = []
    
    # Initialize the board
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    # Place the first queen at (0, first_queen_col)
    col.add(first_queen_col)
    pos_diag.add(0 + first_queen_col)
    neg_diag.add(0 - first_queen_col)
    board[0][first_queen_col] = "Q"
    
    # Start backtracking from the second row
    backtrack(1, board, col, pos_diag, neg_diag, res, n)
    
    return res

def backtrack(r, board, col, pos_diag, neg_diag, res, n):
    if r == n:
        solution = ["".join(row) for row in board]
        res.append(solution)
        return
    
    for c in range(n):
        if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
            continue
        
        # Place the queen
        col.add(c)
        pos_diag.add(r + c)
        neg_diag.add(r - c)
        board[r][c] = "Q"
        
        # Recurse to place queens in the next row
        backtrack(r + 1, board, col, pos_diag, neg_diag, res, n)
        
        # Backtrack and remove the queen
        col.remove(c)
        pos_diag.remove(r + c)
        neg_diag.remove(r - c)
        board[r][c] = "."

def main():
    n = 8
    first_queen_col = 1
    solutions = solve_nqueen(n, first_queen_col)
    
    if solutions:
        for row in solutions[0]:  # Corrected to loop over rows of the first solution
            print("".join(row))
    else:
        print("No solutions found")

if __name__ == "__main__":
    main()
