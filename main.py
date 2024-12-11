from random import choice


def parse_text(text: str, token_size: int) -> list[str]:
    """
    Parses text into tokens consisting of several words
    """
    words = text.split()
    tokens = []
    for i in range(len(words) // token_size):
        tokens.append(" ".join(words[i * token_size:(i + 1) * token_size]))
    return tokens


def make_pairs(tokens: list[str]) -> dict[str: list[str]]:
    """
    Makes a dictionary of all adjacent token pairs
    This dict has tokens as keys and lists of tokens that came after key token as items
    """
    pair_dict = {}
    token_2 = tokens[0]
    for i in range(len(tokens) - 1):
        token_1 = token_2
        token_2 = tokens[i + 1]
        if token_1 in pair_dict.keys():
            pair_dict[token_1].append(token_2)
        else:
            pair_dict[token_1] = [token_2]
    return pair_dict


def find_first_word(start: list[str]) -> str:
    """
    Finds starting sequence in tokens list or chooses random token if it doesn't exist
    """
    if len(start) > 0:
        if len(start) > n:
            new_start = []
            for i in range(len(start) // n):
                new_start.append(" ".join(start[i * n:(i + 1) * n]))
            start = new_start
        if start[-1] in pair_dict:
            first_word = start[-1]
        else:
            first_word = ""
            for word in tokens:
                if word.lower().startswith(start[-1].lower()):
                    first_word = word
                    break
            if first_word == "":
                first_word = choice(tokens)
    else:
        first_word = choice(tokens)
    return first_word


def generate_text_chain(first_word: str, num_tokens: int, pair_dict) -> list[str]:
    """
    Generates text markov chain using pairs dict and first word
    """
    chain = [first_word]

    for i in range(num_tokens):
        chain.append(choice(pair_dict[chain[-1]]))
    return chain



if __name__ == '__main__':
    while True:
        try:
            name = input("Enter source text path: ")
            with open(name, encoding='utf8') as file:
                data = file.read()
            if len(data) > 0:
                break
            else:
                print("File contains no data, try again...")
        except FileNotFoundError:
            print("Invalid file path, try again...")

    while True:
        try:
            n = int(input("Enter token size in words: "))
            break
        except ValueError:
            print("Invalid value, try again...")

    start = input("Enter starting text or nothing:\n").split()

    while True:
        try:
            num_tokens = int(input("Enter generated text size in tokens: "))
            break
        except ValueError:
            print("Invalid value, try again...")

    tokens = parse_text(data, n)
    print(f"Loaded {len(tokens)} tokens.")

    pair_dict = make_pairs(tokens)
    first_word = find_first_word(start)

    chain = generate_text_chain(first_word, num_tokens, pair_dict)
    res = ' '.join(chain)
    print(f"Your generated text is:\n{res}")
    input("Press enter to exit...")
