import os

def merge_files(file1, file2, combined_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(combined_file, 'w') as combined:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        min_length = min(len(lines1), len(lines2))

        for i in range(min_length):
            combined.write(f'1 {lines1[i].strip()}\n')  # Prefix line from file1 with 1
            combined.write(f'0 {lines2[i].strip()}\n')  # Prefix line from file2 with 0

def main():
    folder_name = input("Enter the name of the folder containing the text files: ")
    directory = os.path.join('./', folder_name)
    
    if not os.path.isdir(directory):
        print("Folder not found.")
        return
    
    files = os.listdir(directory)

    # Group files by their prefix before the first underscore
    file_groups = {}
    for file in files:
        prefix = file.split('_')[0]
        if prefix in file_groups:
            file_groups[prefix].append(file)
        else:
            file_groups[prefix] = [file]

    # Merge files in each group
    for prefix, group in file_groups.items():
        if len(group) == 2:  # Make sure there are exactly two files for each prefix
            file1, file2 = sorted(group)  # Sort to ensure consistent order
            combined_file = os.path.join(directory, f'{prefix}_combined.txt')
            merge_files(os.path.join(directory, file1), os.path.join(directory, file2), combined_file)
            print(f"Merged {file1} and {file2} into {prefix}_combined.txt")

    # Merge contents from all _combined.txt files into one big file
    all_data_file = os.path.join(directory, 'all_data_big_file.txt')
    with open(all_data_file, 'w') as output:
        for file in os.listdir(directory):
            if file.endswith('_combined.txt'):
                with open(os.path.join(directory, file), 'r') as f:
                    output.write(f.read())

    print(f"All combined files merged into {all_data_file}")

if __name__ == "__main__":
    main()
