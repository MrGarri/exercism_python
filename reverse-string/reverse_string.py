def reverse(text):
    # return text[::-1]     -- Avoiding this solution explicitly

    return "".join(text[i] for i in range(len(text)-1, -1, -1))
