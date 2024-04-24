
import os


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
    labels_one_hot_sequence = []
    seqdata_one_hot_sequence = []
    with open(input_file, 'r') as infile:
        for line in infile:
            label, sequence = line.strip().split(' ', 1)
            label = int(label[0])  # Take the first digit of the label
            one_hot_sequence = convert_to_one_hot(sequence)
            labels_one_hot_sequence.append([label])
            seqdata_one_hot_sequence.append(one_hot_sequence)
    return labels_one_hot_sequence, seqdata_one_hot_sequence


def main():
    train_data_file = 'train_data.txt'
    test_data_file = 'test_data.txt'
    validation_data_file = 'validation_data.txt'

    if os.path.isfile(train_data_file) and os.path.isfile(test_data_file) and os.path.isfile(validation_data_file):
        train_labels_one_hot_sequence, train_seqdata_one_hot_sequence = process_file(train_data_file)
        print(f"{train_data_file} converted to one-hot encoded arrays")
        test_labels_one_hot_sequence, test_seqdata_one_hot_sequence = process_file(test_data_file)
        print(f"{test_data_file} converted to one-hot encoded arrays")
        validation_labels_one_hot_sequence, validation_seqdata_one_hot_sequence = process_file(validation_data_file)
        print(f"{validation_data_file} converted to one-hot encoded arrays")   
    else:
        print("Data files were not found.")


if __name__ == "__main__":
    main()