import nltk
from nltk.corpus import words

nltk.download('words')


def is_valid_word(word):
    return word in word_list


def dfs(the_grid, i, j, visited, current_word, valid_words):
    if len(current_word) >= 4 and is_valid_word(current_word):
        valid_words.add(current_word)

    # Define the 8 possible directions (up, down, left, right, and diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(the_grid) and 0 <= nj < len(the_grid[0]) and (ni, nj) not in visited:
            visited.add((ni, nj))
            dfs(the_grid, ni, nj, visited, current_word + the_grid[ni][nj], valid_words)
            visited.remove((ni, nj))


def find_all_words(the_grid):
    valid_words = set()
    for i in range(len(the_grid)):
        for j in range(len(the_grid[0])):
            dfs(the_grid, i, j, {(i, j)}, the_grid[i][j], valid_words)
    return valid_words


if __name__ == '__main__':
    # Example grid
    grid = [
        ['h', 'w', 's', 'e'],
        ['l', 'a', 'u', 'l'],
        ['a', 'g', 'g', 'a'],
        ['e', 'u', 'n', 'e']
    ]

    # Load dictionary
    word_list = set(words.words())

    # Filter words to include only those with at least 4 letters
    word_list = {word.lower() for word in word_list if len(word) >= 4}

    result = find_all_words(grid)

    print(result)
