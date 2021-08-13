def solution(board, moves):

    catch = []
    count = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                catch.append(board[j][i-1])
                board[j][i-1] = 0
                break

        if len(catch) >= 2:
            if catch[-1] == catch[-2]:
                del catch[-2:]
                count += 2

    return count


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
print(solution([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 2, 1, 0, 0], [
      0, 2, 1, 0, 0], [0, 2, 1, 0, 0]],  [1, 2, 3, 3, 2, 3, 1]))

# n번째 줄 board[?][n-1]
