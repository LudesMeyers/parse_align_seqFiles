#Needs to keep sequence that has no Ns, add a fasta header, and rename file.
#arg[1]: the file name you want all of the parsed sequences copied to.
#arg[2]... file names of sequences to be parsed.
#!!Should include a table of lengths of noNs.
import sys
print("There %d args" % len(sys.argv))

#open io stream with output file using name generated from argv[1]
comboFile = sys.argv[1]
outFile = comboFile + "_noNs.txt"
of = open(outFile, 'a')

print("Parsed files will be in %s" % (outFile))

if len(sys.argv) < 3:
	print("Did you specify an output filename and seqFile(s)?")
for i in range(len(sys.argv)):
	if i == 0 or i == 1:
		print("Did you specify an output file name and seqfile(s)?")
		continue
	print(".")
	print("Parsing file %s" % (sys.argv[i]))
	print("..")
	fileName = sys.argv[i]
	print("...")
	filePath = fileName
	print("\nReading: %s" % (filePath))

	fSeq = ""
	print("output filepath: %s" % (filePath))
	input("Press enter")
	with open(filePath) as f:
		for line in f:
			fSeq += line.rstrip('\n')
	
	print("Input sequence: %s" % fSeq)
	input("Press enter")
	if 'N' in fSeq:
		print("Finding sequence with no Ns")
	else:
		print("No Ns in sequence")
	"""
	tempSeq = '>' + fileName + "\n"
	upSeq = '>' + fileName + "\n"
	print("Assigned supSeq: %s" % upSeq)
	print("upSeq file before parsing %s" % upSeq)
	seqList = {}
	#Find longest N-less sequence.
	#Save N-less sequences >100 bases
	for nt in fSeq:
		if nt != 'N':
			tempSeq += nt
		else:
			#print("Current N-less sequence is %d bases long and has seq %s" % (count, tempSeq))
			#print("Input sequence: %s" % fSeq)
			#input("Press enter")
			if len(tempSeq) > 100:
				seqList[len(tempSeq)] = tempSeq
				print("seqList is: %s" % seqList)
			if len(tempSeq) > len(upSeq):
				upSeq = tempSeq
				print("Ongoing upSeq %s" % upSeq)

			tempSeq = '>' + fileName + "\n"
	"""

	#allgn all sequences > 100bases
	
	tempSeq = ""
	for nt in fSeq:
		if nt != 'N':
			tempSeq += nt
		else:
			#print("Current N-less sequence is %d bases long and has seq %s" % (count, tempSeq))
			#print("Input sequence: %s" % fSeq)
			#input("Press enter")
			if len(tempSeq) > 100:
				lenTempSeq = str(len(tempSeq))
				seqName = fileName.rstrip('.txt')
				seqName += '_' + lenTempSeq + '\n'
				seqName += tempSeq + '\n'
				of.write(seqName)

			tempSeq = ""
	"""
	upSeq += '\n'
	print("")
	print('There are %d sequences over 100 bases \n' % len(seqList))
	for k, v in seqList.items():
		print(k, "  ", v)
	input('press enter')
	print(upSeq)

	if 'N' in upSeq:
		print("\nThere is still an N")
	
	print("Writing: ", outFile)

	of.write(upSeq)
	"""
of.close()
