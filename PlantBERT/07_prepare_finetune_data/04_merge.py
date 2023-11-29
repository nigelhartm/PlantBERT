file_tf = open("/usr/users/nigel.hartman/data/finetune/filtered_tf.txt", "r")
file_no_tf = open("/usr/users/nigel.hartman/data/finetune/filtered_no_tf.txt", "r")

line_tf = file_tf.readline()
line_no_tf = file_no_tf.readline()

merged_file = open("/usr/users/nigel.hartman/data/finetune/merged.txt", "w")


while line_tf and line_no_tf:
	merged_file.write(str(line_tf).replace("\n", "") + "\t1\n")
	merged_file.write(str(line_no_tf).replace("\n", "") + "\t0\n")
	line_tf = file_tf.readline()
	line_no_tf = file_no_tf.readline()
file_tf.close()
file_no_tf.close()
merged_file.close()

