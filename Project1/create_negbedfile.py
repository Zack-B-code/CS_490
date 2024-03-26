import os

def modify_bed_file(input_file):
    # Extract the base filename without extension
    base_filename = os.path.splitext(input_file)[0]

    # Create the output filename with '_neg' suffix
    output_file = base_filename + "_neg.bed"

    file = open(input_file, 'r')
    initialcontents = file.readlines()
    # remove newline character from contents
    filecontents = [s.replace("\n", "") for s in initialcontents]
    file.close()

    outputline = "chr1\t"
    finalfileoutput = ""

    for line in range(len(filecontents)):
        currline = filecontents[line].split('\t')
        if line == 0:
            outputline += str(int(currline[2])+1) + "\t"
            restofline = "\t".join(map(str, currline[3:]))
        if line >= 1:
            outputline += str(int(currline[1])-1) + "\t" + restofline + "\n"
            outputline += currline[0]+"\t" + str(int(currline[2])+1) + "\t"
            restofline = "\t".join(map(str, currline[3:]))

    finalfileoutput = outputline
    output = open(output_file, 'w')
    output.write(finalfileoutput)

if __name__ == "__main__":
    input_file = input("Enter the name of the .bed file: ")
    modify_bed_file(input_file)
    print("Modification complete.")
