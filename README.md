# Square Letter Game Solver

## Inspiration

This project was inspired by the [Squares](https://squares.org/) word game. The solver is designed to emulate the game's mechanics and rules, providing an automated way to find the maximum scoring words from a given grid.

This project implements a solver for a square letter game where the goal is to find all possible words in a given letter grid. The solver uses a depth-first search (DFS) algorithm to explore all valid words by connecting letters in various directions.

## How to Play

- Create words by connecting letters up, down, left, right, and diagonally.
- The goal is to find all the words in the letter grid and score the maximum number of points.

## Rules of the Game

- You earn 1 point for each letter in a guessed word. For example, you will receive 5 points for a 5-letter word.
- Words must contain at least 4 letters.
- Each tile cannot be used more than one time in a word.
- Words with hyphens, proper nouns, vulgarities, and especially rare words are not included in the main word list.

## Features

- **Grid Representation**: Uses a 2D list to represent the letter grid.
- **Dictionary**: Includes a comprehensive word list to check valid words.
- **Word Search Algorithm**: Implements a depth-first search (DFS) algorithm to find all possible words in the grid.
- **Scoring System**: Calculates the score based on the length of the words found.
- **Optimization**: Ensures efficient exploration of valid word combinations.

## Usage

1. Clone the repository.
2. Install the required dependencies (e.g., `nltk`).
3. Run the solver to find all valid words and calculate the total score.

## Example

```python
import nltk
from nltk.corpus import words
nltk.download('words')

# Example grid
grid = [
    ['t', 'h', 'i', 's'],
    ['w', 'a', 't', 's'],
    ['o', 'a', 'h', 'g'],
    ['f', 'g', 'd', 't']
]

# Load dictionary
word_list = set(words.words())

# Filter words to include only those with at least 4 letters
word_list = {word.lower() for word in word_list if len(word) >= 4}

def is_valid_word(word):
    return word in word_list

def dfs(grid, i, j, visited, current_word, valid_words):
    if len(current_word) >= 4 and is_valid_word(current_word):
        valid_words.add(current_word)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited:
            visited.add((ni, nj))
            dfs(grid, ni, nj, visited, current_word + grid[ni][nj], valid_words)
            visited.remove((ni, nj))

def find_all_words(grid):
    valid_words = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dfs(grid, i, j, {(i, j)}, grid[i][j], valid_words)
    return valid_words

def calculate_score(words):
    return sum(len(word) for word in words)

# Find all valid words and calculate the score
valid_words = find_all_words(grid)
score = calculate_score(valid_words)
print(f"Found {len(valid_words)} valid words.")
print(f"Total score: {score}")
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
