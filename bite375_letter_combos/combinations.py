from itertools import product

def generate_letter_combinations(digits: str) -> list[str]:
    """
    Calculate all possible letter combinations of a very short phone number.
    Input: A string of up to four digits.
    Output: A list of strings where each string represents a valid combination of letters
        that can be formed from the input. The strings in the output list should be sorted
        in lexicographical order.
    Raises: `ValueError`: If the input `digits` string contains non-digit characters or
        has more than four digits.
    """
    alphabet_dict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    list_of_alphas = list()
    if len(digits)> 4:
        raise ValueError
    for digit in digits:
        if digit not in alphabet_dict:
            raise ValueError
        list_of_alphas.append(alphabet_dict[digit])
    combinations = product(*list_of_alphas)
    return ["".join(combo) for combo in combinations]
        

if __name__ == "__main__":
    print(generate_letter_combinations('24'))
