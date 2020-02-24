def read_file():
    dictionary = {}
    with open("request_counts.txt") as f:
        for line in f:
            (key, val) = line.split()
            dictionary[key] = int(val)
    return dictionary


def write_to_file(dictionary):
    with open("request_counts.txt" , "w") as f:
        for k, v in dictionary.items():
            f.writelines(f"{k}  {v}\n")

