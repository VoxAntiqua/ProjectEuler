# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:43:59 2019

@author: andre
"""

#Project Euler Problem 42
WORD_LIST_FILE = "p042_words.txt"

VALUES_DICT = {"A": 1,
               "B": 2,
               "C": 3,
               "D": 4,
               "E": 5,
               "F": 6,
               "G": 7,
               "H": 8,
               "I": 9,
               "J": 10,
               "K": 11,
               "L": 12,
               "M": 13,
               "N": 14,
               "O": 15,
               "P": 16,
               "Q": 17,
               "R": 18,
               "S": 19,
               "T": 20,
               "U": 21,
               "V": 22,
               "W": 23,
               "X": 24,
               "Y": 25,
               "Z": 26
               }

TRIANGLE_LIST = [1,3,6,10,15,21,28,36,45,55]

def calculateWordSum(word):
    """
    Calculates the sum of letters in a word, where "A" is 1, "B" is 2, etc.
    """
    wordSum = 0
    for letter in word:
        wordSum += VALUES_DICT[letter]
    return wordSum

def loadWords(filename):
    """
    Loads words from text file
    """
    f = open(filename,"r")
    if f.mode == "r":
        contents = f.read()
    contents = contents.replace("\"","")
    words = contents.split(",")
    return words

def nextTriangleNumber():
    """
    Generates the next Triangle number and appends to TRIANGLE_LIST
    """
    n = len(TRIANGLE_LIST)+1
    nextValue = int((1/2)*n*(n+1))
    TRIANGLE_LIST.append(nextValue)    
    

def main():
    wordList = loadWords(WORD_LIST_FILE)
    triangleWords = []
    for word in wordList:
        wordValue = calculateWordSum(word)
        greatestTriangleNumber = TRIANGLE_LIST[len(TRIANGLE_LIST)-1]
        while wordValue > greatestTriangleNumber:
            nextTriangleNumber()
            greatestTriangleNumber = TRIANGLE_LIST[len(TRIANGLE_LIST)-1]
        if wordValue in TRIANGLE_LIST:
            triangleWords.append(word)
            
    print("There are",len(triangleWords),"triangle words.")

    
    
    
if __name__ == "__main__":
    main()