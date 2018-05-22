#-*-coding:utf-8-*-

#CRF Segmenter based character tagging:
# 4-tags for character tagging: B(Begin), E(End), M(Middle), S(Single)

import codecs
import sys

import CRFPP

def crf_segmenter(input_file, output_file, tagger):
	input_data = codecs.open(input_file, 'r', 'utf-8')
	output_data = codecs.open(output_file, 'w', 'utf-8')
	for line in input_data.readlines():
		tagger.clear()
		for word in line.strip():
			word = word.strip()
			if word:
				tagger.add((word + "\to\tB"))#.encode('utf-8'))
		tagger.parse()
		size = tagger.size()
		xsize = tagger.xsize()
		for i in range(0, size):
			for j in range(0, xsize):
				char = tagger.x(i, j)#.decode('utf-8')
				tag = tagger.y2(i)
				if tag == 'B':
					output_data.write(' ' + char)
				elif tag == 'M':
					output_data.write(char)
				elif tag == 'E':
					output_data.write(char + ' ')
				else:
					output_data.write(' ' + char + ' ')
		output_data.write('\n')
	input_data.close()
	output_data.close()

if __name__ == '__main__':
	crf_model = "crf_model/crf_model_test_3f1c4t"
	input_file = "pku_training_unsegged.utf8"
	output_file = "result/pku_train_seg_CRF_3f1c4t.utf8"
	tagger = CRFPP.Tagger("-m " + crf_model)
	crf_segmenter(input_file, output_file, tagger)