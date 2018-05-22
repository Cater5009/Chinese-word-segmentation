# *-* conding=utf-8

import pickle
import sys

maxlen_word = 0

#MM
def MM_maxmatch_seg(line, dic):
    words = []
    index = 0
    while index < len(line):
        offset = 0
        ismatched = False
        for i in range(maxlen_word, 0, -1):
            currchars = line[index : index + i]
            if currchars in dic:
                words.append(currchars)
                ismatched = True
                offset = i
                break
        if not ismatched:
            offset = 1
            words.append(line[index])
        index += offset
    return words


if __name__=="__main__":
    try:
        inputfile = open("pku_training_unsegged.utf8", "r")
    except:
        print(sys.stderr)
        sys.exit(1)

    try:
        dic = pickle.load(open("pku_training.utf8.pkl", "rb"))
        # find max-length in dic
        for key in dic:
            if len(key) > maxlen_word:
                maxlen_word = len(key)
    except:
        print(sys.stderr)
        sys.exit(1)

    #MM
    try:
        outputfile = open("result/pku_train_seg_MM.utf8", "w")
    except:
        print(sys.stderr)
        sys.exit(1)

    for eachline in inputfile:
        outputfile.write("  ".join(MM_maxmatch_seg(eachline, dic)))
