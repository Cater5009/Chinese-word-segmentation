# -*- coding: utf-8 -*-
import codecs
import sys
import linecache

class NGram(object):

    def __init__(self, n):
        # n is the order of n-gram language model
        self.n = n
        self.unigram = {}
        self.bigram = {}

    # scan a sentence, extract the ngram and update their
    # frequence.
    #
    # @param    sentence    list{str}
    # @return   none
    def scan(self, sentence):
        # file your code here
        for line in sentence:
            self.ngram(line.split())
        #unigram
        if self.n == 1:
            try:
                fip = open("data.uni","w")
            except:
                print(sys.stderr)
                print("failed to open data.uni")
            for i in self.unigram:
                fip.write("%s %d\n" % (i,self.unigram[i]))
        if self.n == 2:
            try:
                fip = open("data.bi","w")
            except:
                print(sys.stderr)
                print("failed to open data.bi")
            for i in self.bigram:
                fip.write("%s %d\n" % (i,self.bigram[i]))
    # caluclate the ngram of the words
    #
    # @param    words       list{str}
    # @return   none
    def ngram(self, words):
        # unigram
        if self.n == 1:
            for word in words:
                if len(word) == 1:
                    if word not in self.unigram:
                        self.unigram[word] = 1
                    else:
                        self.unigram[word] = self.unigram[word] + 1
                else:
                    for w in word[1:len(word) - 1]:
                        if w not in self.unigram:
                            self.unigram[w] = 1
                        else:
                            self.unigram[w] += 1

        # bigram
        if self.n == 2:
            for word in words:
                if len(word) == 3:
                    stri = word[1 : 2]
                    if stri not in self.bigram:
                        self.bigram[stri] = 1
                    else:
                        self.bigram[stri] = self.bigram[stri] + 1
                if len(word) > 3:
                    for i in range(0, len(word) - 1, 1):
                        stri = word[i : i + 2]
                        if stri not in self.bigram:
                            self.bigram[stri] = 1
                        else:
                            self.bigram[stri] = self.bigram[stri] + 1

# 4 tags for character tagging: B M E S
def character_tagging(input_file, output_file, bi):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open("pku_training_tagging.utf8.2", 'w', 'utf-8')
    for line in input_data.readlines():
        word_list = line.strip().split()
        for word in word_list:
            if len(word) == 1:
                output_data.write(word + " S\n")
            else:
                output_data.write(word[0] + " B\n")
                for w in word[1:len(word) - 1]:
                    output_data.write(w + " M\n")
                output_data.write(word[len(word) - 1] + " E\n")
        output_data.write("\n")
    input_data.close()
    output_data.close()
    output_data = codecs.open(output_file, 'w', 'utf-8')
    line_count = len(open("temp.txt").readlines())
    for i in range(1, line_count - 1, 1):
        fst_line = linecache.getline("temp.txt", i)
        sed_line = linecache.getline("temp.txt", i + 1)
        ha = fst_line[0] + sed_line[0]
        if ha in bi.bigram:
            write = fst_line[0] + " " + str(bi.bigram[ha]) + fst_line[1:len(fst_line)]
            output_data.write(fst_line.strip('\n') + " " + str(bi.bigram[ha]) + "\n")
    fst_line = linecache.getline("temp.txt", line_count)
    ha = fst_line[0] + "\n"
    if ha in bi.bigram:
        output_data.write(fst_line.strip('\n') + " " + str(bi.bigram[ha]) + "\n")
    output_data.close()

if __name__ == '__main__':
    sentence = []
    try:
        fip = open("pku_training.utf8", "r")
        for line in fip:
            if len(line.replace("  ", "")) != 0:
                sentence.append(line.replace("  ", ""))
    except:
        print(sys.stderr)
        print("failed to open input file")

    uni = NGram(1)
    bi = NGram(2)
    uni.scan(sentence)
    bi.scan(sentence)

    input_file = "pku_training.utf8"
    output_file = "pku_training_tagging.utf8.3"
    character_tagging(input_file, output_file, bi)
