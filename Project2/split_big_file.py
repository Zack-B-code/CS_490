import os

def split_data(big_file):
    directory = os.path.dirname(big_file)
    train_file = os.path.join(directory, 'train_data.txt')
    test_file = os.path.join(directory, 'test_data.txt')
    validation_file = os.path.join(directory, 'validation_data.txt')

    with open(big_file, 'r') as f:
        lines = f.readlines()
        total_lines = len(lines)
        train_size = int(0.75 * total_lines)
        test_size = int(0.20 * total_lines)
        validation_size = int(0.05 * total_lines)

        with open(train_file, 'w') as train, open(test_file, 'w') as test, open(validation_file, 'w') as validation:
            train.writelines(lines[:train_size])
            test.writelines(lines[train_size:train_size + test_size])
            validation.writelines(lines[train_size + test_size:train_size + test_size + validation_size])

    print("Big file split into train_data.txt, test_data.txt, and validation_data.txt")


# Conversion dictionary
encode_convert = {'A': [1, 0, 0, 0],
                  'G': [0, 1, 0, 0],
                  'C': [0, 0, 1, 0],
                  'T': [0, 0, 0, 1]}

def convert_to_one_hot(sequence):
    one_hot = []
    for base in sequence:
        one_hot.extend(encode_convert.get(base, [0, 0, 0, 0]))  # Default to [0, 0, 0, 0] if base not found
    return one_hot

def process_file(input_file):
    one_hot_sequences = []
    with open(input_file, 'r') as infile:
        for line in infile:
            label, sequence = line.strip().split(' ', 1)
            label = int(label)
            one_hot_sequence = convert_to_one_hot(sequence)
            one_hot_sequences.append([label] + one_hot_sequence)
    return one_hot_sequences

def main():
    big_file_name = input("Enter the name of the big file: ")
    big_file = os.path.join('./', big_file_name)

    if not os.path.isfile(big_file):
        print("Big file not found.")
        return

    split_data(big_file)


    train_data_file = 'train_data.txt'
    test_data_file = 'test_data.txt'
    validation_data_file = 'validation_data.txt'

    if os.path.isfile(train_data_file) and os.path.isfile(test_data_file) and os.path.isfile(validation_data_file):
        train_data_one_hot_sequence = process_file(train_data_file)
        test_data_one_hot_sequence = process_file(test_data_file)
        validation_data_one_hot_sequence = process_file(validation_data_file)
        print(f"{train_data_file} converted to one-hot encoded array named train_data_one_hot_sequence:")
        print(f"{test_data_file} converted to one-hot encoded array named test_data_one_hot_sequence:")
        print(f"{validation_data_file} converted to one-hot encoded array named validation_data_one_hot_sequence:")
        
    else:
        print("files were not found.")


if __name__ == "__main__":
    main()
