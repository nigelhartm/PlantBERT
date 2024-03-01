tf_file = open("/usr/users/nigel.hartman/data/finetune/Ath_cds.fas", "r")
no_tf_file = open("/usr/users/nigel.hartman/data/finetune/seq_no_tf.fna", "r")

output_tf = open("/usr/users/nigel.hartman/data/finetune/filtered_tf.txt", "w")
output_no_tf = open("/usr/users/nigel.hartman/data/finetune/filtered_no_tf.txt", "w")

line = tf_file.readline()
buf = ""
while line:
	if line.startswith(">"):
		buf = buf.upper()
		buf = buf.replace("\n", "")
		if buf.find("N") < 0 and buf.find(".") < 0:
			if len(buf) >= 512:
				output_tf.write(buf[0:512] + "\n")
		buf = ""
	else:
		buf += line
	line = tf_file.readline()
output_tf.close()

line = no_tf_file.readline()
buf = ""
while line:
        if line.startswith(">"):
                buf = buf.upper()
                buf = buf.replace("\n", "")
                if buf.find("N") < 0 and buf.find(".") < 0:
                        if len(buf) >= 512:
                                output_no_tf.write(buf[0:512] + "\n")
                buf = ""
        else:
                buf += line
        line = no_tf_file.readline()
output_no_tf.close()
