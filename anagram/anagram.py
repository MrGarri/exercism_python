def find_anagrams(word: str, candidates: list) -> list:
    word_sorted = sorted(word.lower())
    result = []

    for candidate in candidates:
        if word_sorted == sorted(candidate.lower()) and word.lower() != candidate.lower():
            result.append(candidate)

    return result
