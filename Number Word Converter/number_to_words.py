# number_to_words.py

NUMBERS = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
    10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
    14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
    18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty",
    40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
    80: "Eighty", 90: "Ninety"
}

MULTIPLIERS = [
    (10**7, "Crore"),    # Indian numbering system
    (10**5, "Lakh"),
    (10**3, "Thousand"),
    (10**2, "Hundred")
]


def number_to_words(n: int) -> str:
    """Convert an integer number into words (Indian + Western system)."""
    if n == 0:
        return NUMBERS[0]

    words = []

    def helper(num):
        if num < 20:
            return [NUMBERS[num]] if num > 0 else []
        elif num < 100:
            tens, below_ten = divmod(num, 10)
            return [NUMBERS[tens * 10]] + helper(below_ten)
        else:
            for value, name in MULTIPLIERS:
                if num >= value:
                    quotient, remainder = divmod(num, value)
                    part = helper(quotient) + [name]
                    if remainder > 0:
                        part += helper(remainder)
                    return part
        return []

    words.extend(helper(n))
    return " ".join(words)


