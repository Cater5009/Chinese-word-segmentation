# *-* conding=utf-8

import pickle
import sys

maxlen_word = 0

#RMM
def RMM_maxmatch_seg(line, dic):
    words = []
    word_len = len(line)
    while word_len > 0:
        max_cut_len = min(word_len, maxlen_word)
        for i in range(max_cut_len, 0, -1):
            currchars = line[word_len - i : word_len]
            if currchars in dic:
                words.append(currchars)
                word_len -= i
                break
            elif i == 1:
                words.append(currchars)
                word_len -= 1
    words.reverse()
    return words


if __name__=="__main__":
    try:
        inputfile = open("pku_training_unsegged.utf8", "r")
    except:
        print(sys.stderr)
        sys.exit(1)

    try:
        dic = pickle.load(open("pku_training.utf8.pkl", "rb"))
        # find the max-length in dic
        for key in dic:
            if len(key) > maxlen_word:
                maxlen_word = len(key)
    except:
        print(sys.stderr)
        sys.exit(1)

    #RMM
    try:
        outputfile = open("result/pku_train_seg_RMM.utf8", "w")
    except:
        print(sys.stderr)
        sys.exit(1)

    for eachline in inputfile:
        outputfile.write("  ".join(RMM_maxmatch_seg(eachline.strip('\n'), dic)))
        outputfile.write("\n")
