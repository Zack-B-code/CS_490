import os


def extract_lines(input_file):
    base_filename = os.path.splitext(input_file)[0]

    # Create the output filename with '_neg' suffix
    output_file = base_filename + "_onlyseq.txt"

    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        lines = f_in.readlines()
        for i in range(1, len(lines), 2):
            line = lines[i].strip()  # Remove leading/trailing whitespace
            if not line.startswith('>chr'):
                # Trim the line to a length of 200 characters
                trimmed_line = line[:200]
                if len(trimmed_line) == 200:
                    f_out.write(trimmed_line + '\n')  # Write trimmed line to output file

    print("Lines extracted and trimmed to length 200, saved in", output_file)


def main():
    input_file = input("Enter the name of the txt file: ")

    extract_lines(input_file)

if __name__ == "__main__":
    main()

