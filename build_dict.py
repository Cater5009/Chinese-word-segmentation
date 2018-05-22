# *-* conding=utf-8

import pickle
import sys

wordcount = {}

if __name__=="__main__":
    try:
        file = open("pku_training.utf8", "r")
    except:
        print(sys.stderr)
        print("failed to open file")
        sys.exit(1)

    for line in file:
        for word in line.split("  "):
            if word.replace("\n", "") not in wordcount:
                if word != "\n":
                    wordcount[word] = 0
                    wordcount[word] += 1

    vocab = set([k for k in wordcount])
    pickle.dump(vocab, open("pku_training.utf8.pkl", "wb"))