# Project 3 - Wordsearch
#
# Name: Arielle Goodman-Rabner
# Instructor: Mork

from solverFuncs import*

def main():
    puzzle = read_puzzle()
    print('Puzzle:\n')
    for i in puzzle:
        print(i)
    words = read_words()
    print()
    for eachWord in words:
        result = printPuzzle(puzzle, eachWord) 
        if result != None:
            print(str(eachWord) + ':', result[0], 'row:', result[1], 'column:', result[2])
        else:
            print(str(eachWord) + ':', 'word not found')

# HELPER FUNCTION - search through puzzle 
def printPuzzle(puzzle, word):
    searchRow = search_rows(puzzle, word)
    if searchRow[2] == 0:
        forward = ['(FORWARD)', searchRow[0], searchRow[1]]
        return forward
    elif searchRow[2] == 1:
        back = ['(BACKWARD)', searchRow[0], searchRow[1]]
        return back
    searchCol = search_cols(puzzle, word)
    if searchCol[2] == 2:
        down = ['(DOWN)', searchCol[0], searchCol[1]]
        return down
    elif searchCol[2] == 3:
        up = ['(UP)', searchCol[0], searchCol[1]]
        return up


if __name__ == '__main__':
    main()
# runs the main function 


