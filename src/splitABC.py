# split abc
import sys
import re

def main(filepath):
	# var
	startFlag = False
	buffers = ''
	nameIndex = 0
	TEMPLATE_NAME = '../data/processed/abc_{}.abc'

	# open main abc file
	with open(filepath, 'r') as f:
		for line in f:
			# check if line only '\n' or len(line) == 1
			if len(line) == 1:
				startFlag = not startFlag
				# if buffers != ''
				if buffers != '':
					# write to file
					with open(TEMPLATE_NAME.format(nameIndex), 'w') as wf:
						# write buffers to name with newline before and after, not necessary as using the notes to train
						#wf.write('\n')
						wf.write(buffers)
						#wf.write('\n')
					# update name
					nameIndex += 1
					# reset buffers
					buffers = ''
				continue
			# check for title
			if line[0] == '%' or (line[0].isupper() and line[1] == ':'):
				continue
			# do replacement 
			#regString = 'X: \d+'
			#replacedLine = re.sub(regString, 'X: 1', line)
			buffers += line

if __name__ == '__main__':
	# check for filename in sys.argv filename
	if len(sys.argv) != 2:
		# quit
		exit()

	main(sys.argv[1])