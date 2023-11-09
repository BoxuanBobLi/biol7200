import subprocess

def needleman_wunsch(seq_a: str, seq_b: str, match: int, mismatch: int, gap: int) -> tuple[tuple[str, str], int]:
    # Initialize the score matrix
    rows = len(seq_a) + 1
    cols = len(seq_b) + 1
    score_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Initialize the traceback matrix
    traceback_matrix = [[None for _ in range(cols)] for _ in range(rows)]

    # Fill the top row and left column of the score matrix with gap penalties
    for i in range(1, rows):
        score_matrix[i][0] = score_matrix[i-1][0] + gap
        traceback_matrix[i][0] = 'U'  # U indicates an upward traceback

    for j in range(1, cols):
        score_matrix[0][j] = score_matrix[0][j-1] + gap
        traceback_matrix[0][j] = 'L'  # L indicates a leftward traceback

    # Fill in the score matrix and build the traceback matrix
    for i in range(1, rows):
        for j in range(1, cols):
            match_score = score_matrix[i-1][j-1] + (match if seq_a[i-1] == seq_b[j-1] else mismatch)
            delete_score = score_matrix[i-1][j] + gap
            insert_score = score_matrix[i][j-1] + gap

            score_matrix[i][j], traceback_matrix[i][j] = max(
                (match_score, 'D'),  # D for diagonal move
                (delete_score, 'U'),  # U for up move (deletion)
                (insert_score, 'L'),  # L for left move (insertion)
                key=lambda x: x[0]
            )

    # Trace back from the bottom right corner to construct the alignment
    aligned_a, aligned_b = [], []
    i, j = rows - 1, cols - 1
    score = score_matrix[i][j]
    while i > 0 or j > 0:
        move = traceback_matrix[i][j]
        if move == 'D':
            aligned_a.append(seq_a[i-1])
            aligned_b.append(seq_b[j-1])
            i, j = i-1, j-1
        elif move == 'U':
            aligned_a.append(seq_a[i-1])
            aligned_b.append('-')
            i -= 1
        elif move == 'L':
            aligned_a.append('-')
            aligned_b.append(seq_b[j-1])
            j -= 1

    # Reverse the alignments as we've built them from the end to the start
    aligned_a = ''.join(reversed(aligned_a))
    aligned_b = ''.join(reversed(aligned_b))

    return (aligned_a, aligned_b), score


