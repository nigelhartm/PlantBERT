k = 6 #@param {type:"integer"}
in_file = open("working_dir/DNABERT/examples/arabidopsis/formatted_TAIR9_chr_all.fas", "r")
out_file = open("working_dir/DNABERT/examples/arabidopsis/" + str(k) + "mer_formatted_TAIR9_chr_all.fas", "w")
line = in_file.readline()
while line:
  line = line.replace("\n", "")
  for j in range(0, len(line), k):
    out_file.write(line[j:j+k] + " ")
  out_file.write("\n")
  line = in_file.readline()
in_file.close()
out_file.close()
