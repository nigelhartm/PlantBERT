import sys
import os
import pandas

table = pandas.read_csv("/usr/users/nigel.hartman/data/finetune/01_oryza/all.gff3", dtype=str, sep="\t", skiprows=1)

#make list of tf ids
tf_id_file = open("/usr/users/nigel.hartman/data/finetune/01_oryza/Osj_cds.fas", "r")
line = tf_id_file.readline()
tf_ids = []
while line:
    if line.startswith(">"):
        end = line.find(".") # Test ohne rücksicht auf .
        tf_ids.append(line[1:end])
    line = tf_id_file.readline()
print("Length of TF_IDS:" + str(len(tf_ids)))

out = open("/usr/users/nigel.hartman/data/finetune/01_oryza/no_tf.gff", "w")
for index, row in table.iterrows():
    properties = str(table.iloc[index, 8]).split(";")
    protein_coding = False
    if str(table.iloc[index, 2]) == "gene":
        protein_coding = True
    for prop in properties:
        try:
            x, y = str(prop).split("=")
#            if x == "gene_biotype":
#                if y == "protein_coding":
#                    protein_coding = True
            if x == "ID":
                if protein_coding:
                    if y not in tf_ids:
                        out.write("\t".join(map(str, table.loc[index, :])) + "\n")       
        except:
            print("Error")
out.close()

