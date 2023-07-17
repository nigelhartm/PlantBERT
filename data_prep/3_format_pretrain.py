import glob

for file in glob.glob('fnagz/*.fna'):
	file = file[file.find('/')+1:len(file)]
	in_file = open('fnagz/' + str(file), 'r')
	out_file = open('formatted/' + str(file), 'w')
	line = in_file.readline()
	while line:
		out_file.write(line)
		line = in_file.readline()
		#if line.startswith('>'):
# create lines of length 577 like original put away all N and \n
#in_file = open("working_dir/DNABERT/examples/arabidopsis/TAIR9_chr_all.fas", "r")
#out_file = open("working_dir/DNABERT/examples/arabidopsis/formatted_TAIR9_chr_all.fas", "w")
#line = in_file.readline()
#buf = ""
#while line:
#  if(not line.startswith(">")):
#    buf += line
#    buf = buf.replace("N", "")
#    buf = buf.replace(".", "")
#    buf = buf.replace("\n", "")
#    if(len(buf)>=576):
#      out_file.write(buf[0:576] + "\n")
#      buf = buf[576:len(buf)]
#  line = in_file.readline()
#in_file.close()
#out_file.close()
