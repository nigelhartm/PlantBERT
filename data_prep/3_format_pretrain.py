import glob

for file in glob.glob('fnagz/*.fna'):
	file = file[file.find('/')+1:len(file)]
	print(file)
	in_file = open('fnagz/' + str(file), 'r')
	out_file = open('formatted/' + str(file), 'w')
	buf = ''
	line = in_file.readline()
	while line:
		if not line.startswith('>'):
			buf += line
			buf = buf.upper()
			buf = buf.replace('N', '')
			buf = buf.replace('.', '')
			buf = buf.replace('\n', '')
			buf = buf.replace(' ', '')
		if len(buf) >= 1024:
			out_file.write(buf[0:1024] + "\n")
			buf = buf[1024:len(buf)]
		line = in_file.readline()
	if len(buf) > 0:
		out_file.write(buf[0:1024] + "\n")
		buf = buf[1024:len(buf)]
	in_file.close()
	out_file.close()
