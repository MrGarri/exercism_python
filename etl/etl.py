def transform(legacy_data: dict) -> dict:
    return {
        letter.lower(): key
        for key, value in legacy_data.items()
        for letter in value
    }
