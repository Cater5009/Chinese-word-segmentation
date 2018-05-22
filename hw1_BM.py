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

#BM,based on MM and RMM
def BM_maxmatch_seg(line, dic):
    words_MM = MM_maxmatch_seg(line, dic)
    words_RMM = RMM_maxmatch_seg(line, dic)
    if len(words_MM) > len(words_RMM):#return the smaller one
        return words_RMM
    elif len(words_MM) < len(words_RMM):
        return words_MM
    else:#return the one including fewer single word
        issame = True
        for each_words_MM in words_MM:
            if each_words_MM in words_RMM:
                issame = False
        if issame:
            return words_RMM
        else:
            singlenum_MM = 0
            singlenum_RMM = 0
            for each in words_MM:
                if len(each) == 1:
                    singlenum_MM += 1
            for each in words_RMM:
                if len(each) == 1:
                    singlenum_RMM += 1
            if singlenum_MM <= singlenum_RMM:
                return words_MM
            else:
                return words_RMM

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

    #BM
    try:
        outputfile = open("result/pku_train_seg_BM.utf8", "w")
    except:
        print(sys.stderr)
        sys.exit(1)

    for eachline in inputfile:
        outputfile.write("  ".join(BM_maxmatch_seg(eachline.strip('\n'), dic)))
        outputfile.write("\n")
