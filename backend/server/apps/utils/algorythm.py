ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def bijective_encode(counter: int) -> str:
    # from http://refactormycode.com/codes/125-base-62-encoding
    # with only minor modification
    if counter == 0:
        return ALPHABET[0]
    result = ""
    base = len(ALPHABET)
    while counter > 0:
        result += ALPHABET[counter % base]
        counter //= base
    return result


if __name__ == "__main__":
    print(bijective_encode(120314))
