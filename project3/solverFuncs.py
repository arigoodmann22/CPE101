# Project 3 - Wordsearch
#
# Name: Arielle Goodman-Rabner
# Instructor: Mork

def read_puzzle():
    puzzle = input()
    puzzleList = []
    for i in range(0, len(puzzle), 10):
        puzzleList.append(puzzle[i:i+10])
    return puzzleList 

def read_words():
    # save this as a list of strings 
    words = input() # read in a string of words separated by spaces
    wordList = words.split() # split the text 
    for word in words: # for each word in the line
        return wordList 


# HELPER FUNCTION - search through single string/row
def search_row(row, word):
    if word in row:
        return row.find(word)

# HELPER FUNCTION - reverse a string
def reverseWord(word):
    word = word [::-1] # add find 
    return word

# HELPER FUNCTION - takes row and returns it as columns 
# def transposeWord(string, rowLength):
#     x = 0
#     transposeWord = ""
#     for i in range(0, rowLength):
#         for a in range(x, len(string), rowLength):
#             transposeWord += string[a]
#         x += 1
#     return transposeWord
def transposeWord(puzzle, rowLength):
    x = 0
    transpose = []
    temp = ""
    for col in range(0, len(puzzle)):
        for row in range(0, len(puzzle[col])):
            temp = temp + puzzle[row][col]
        transpose.append(temp)
        temp = ""
        x = x + 1
    return transpose # returns whole puzzle, not just list of 10

def search_rows(puzzle, word): 
    for row in range(len(puzzle)):
        col = puzzle[row].find(word)
        if puzzle[row].find(word) > -1:
            return(row, col, 0)
        rw = reverseWord(word)
        col = puzzle[row].find(rw)
        if puzzle[row].find(rw) > -1:
            realCol = (col + len(word) - 1)
            return(row, realCol, 1) # realCol
    nothingFound = (-1, -1, -1)
    return nothingFound

def search_cols(puzzle, word):
    rowLength = int(100 ** (1 / 2))
    ts = transposeWord(puzzle, rowLength)
    for col in range(len(puzzle)):
        row = ts[col].find(word)
        if ts[col].find(word) > -1:
            return (row, col, 2) # IS IT OK TO HAVE (COL, ROW)
        rw = reverseWord(ts[col])
        row = rowLength - 1 - rw.find(word)
        if rw.find(word) > -1:
            return (row, col, 3)
    nothingFound = (-1, -1, -1)
    return nothingFound

# def search_cols(puzzle, word):
#     rowLength = int(100 ** (1 / 2))
#     ts = transposeWord(puzzle, rowLength)
#     for row in range(len(puzzle)):
#         col = ts[row].find(word)
#         if ts[row].find(word) > -1:
#             return (col, row, 2) # IS IT OK TO HAVE (COL, ROW)
#         rw = reverseWord(ts[row])
#         col = rowLength - 1 - rw.find(word)
#         if rw.find(word) > -1:
#             return (col, row, 3)
#     nothingFound = (-1, -1, -1)
#     return nothingFound

#     # return (row, col, dir) -> 2 for down and 3 for up
#     # return (-1, -1, -1) -> not found
#     for i in range(len(puzzle)):
#         row = puzzle[i].find(word)
#         col = i
#         if row > -1
#             return (row, col, direction)
#     nothingFound = (-1, -1, -1)
#     return nothingFound

    #direction = search_backwards(word)
    # direction will be represented by a number (0 for forward and 1 for backward)

    # row = 0
    # res = (row, column, directon)
    # backward = search_backwards(word)
    # for row in puzzle:
    #     column = search_row(row, word)
    #     row += 1
    #     if res != None:
    #         res.append(row)
    #         res.append(column)
    #     if backward:
    #         res.append[2](backward)
    # return res
    #puzzle[0].find(word)

    # def search_backwards(puzzle, word):
    # for i in range(len(puzzle)):
    #     rowLength = int(100 ** (1 / 2))
    #     rw = reverseWord(puzzle[i])
    #     col = rowLength - 1 - rw.find(word)
    # return (r, col)

    # takes in a puzzle and a string
    # search through each row of the puzzle( each word in your list of words)
    # row represents the index into the list
    # column represents the index of the number in the individual string
    # direction will be represented by a number (0 for forward and 1 for backward)
    # if word not found, return a tuple: (-1, -1, -1)
    # the output will like the following where each value is an int (row, col, direction)
    # HINT: use a helper function to search through a row, single string
    # HINT: use the find function to help 


