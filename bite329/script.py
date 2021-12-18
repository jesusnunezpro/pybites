def tosnake(key_string):
    if not isinstance(key_string, str):
        return key_string
    key_length = len(key_string)
    new_string = ""
    for i, char in enumerate(key_string):
        if char.isupper():
            if i > 0 and i < key_length:
                new_string += "_"
            new_string += char.lower()
        elif char == "-":
            new_string += "_"
        elif char.isnumeric() and not key_string[i-1].isnumeric():
            new_string += "_" + char
        else:
            new_string += char
    return new_string


def snake_case_keys_list(list_with_dicts):
    new_list = list()
    for element in list_with_dicts:
        if isinstance(element, dict):
            new_list.append(snake_case_keys(element))
        elif isinstance(element, list):
            new_list.append(snake_case_keys_list(element))
        else:
            new_list.append(element)
    return new_list


def snake_case_keys(data):
    new_dictionary = dict()
    for key in data:
        dvalue = data[key]
        if isinstance(dvalue, dict):
            dvalue = snake_case_keys(dvalue)
        elif isinstance(dvalue, list):
            dvalue = snake_case_keys_list(dvalue)
        new_dictionary[tosnake(key)] = dvalue
    return new_dictionary


if __name__ == "__main__":
    samples = ["numTIEFighters", "ACRONYM"]
    for sample in samples : print(f"{sample} converts to {tosnake(sample)}")