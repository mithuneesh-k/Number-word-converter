# words_to_number.py

NUMBERS = {
    "ZERO": 0, "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4,
    "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9,
    "TEN": 10, "ELEVEN": 11, "TWELVE": 12, "THIRTEEN": 13,
    "FOURTEEN": 14, "FIFTEEN": 15, "SIXTEEN": 16, "SEVENTEEN": 17,
    "EIGHTEEN": 18, "NINETEEN": 19, "TWENTY": 20, "THIRTY": 30,
    "FORTY": 40, "FIFTY": 50, "SIXTY": 60, "SEVENTY": 70,
    "EIGHTY": 80, "NINETY": 90
}

MULTIPLIERS = {
    "HUNDRED": 100,
    "THOUSAND": 1000,
    "LAKH": 100000,
    "MILLION": 1000000,
    "CRORE": 10000000  # Indian numbering system
}

def words_to_number(text: str) -> int:
    text = text.upper().replace("-", " ").replace(" AND", " ").replace("LAKHS", "LAKH").replace("CRORES", "CRORE")
    words = text.split()

    total = 0
    current = 0

    for word in words:
        if word in NUMBERS:  # direct match
            current += NUMBERS[word]

        elif word in MULTIPLIERS:
            if current == 0:
                current = 1
            current *= MULTIPLIERS[word]

            # Add to total for big multipliers
            if MULTIPLIERS[word] >= 1000:
                total += current
                current = 0

        else:
            raise ValueError(f"Unknown word: {word}")

    return total + current


