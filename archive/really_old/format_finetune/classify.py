# CCCCCC = 1
# else 0

k = 6 #@param {type:"integer"}
in_file = open(str(k)+"mer_formatted_TAIR9_chr_all.fas", "r")
out_file = open("classified_"+str(k)+"mer_formatted_TAIR9_chr_all.fas", "w")
line = in_file.readline()
while line:
  line = line.replace("\n", "")
  classify = 0
  if(line.find("CCCCCC") >= 0):
    classify = 1
  out_file.write(line+ "\t" + str(classify)+"\n")
  line = in_file.readline()
in_file.close()
out_file.close()