def compare_strings(wordOne, wordTwo):
    if len(wordOne) != len(wordTwo): return False
    return wordTwo in (wordOne + wordOne)





