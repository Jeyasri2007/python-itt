import re
def validate_credit_card(card):
    structure_pattern = r"^[456]\d{3}(-?\d{4}){3}$"
    if not re.match(structure_pattern, card):
        return "Invalid"
    clean_card = card.replace("-", "")
    repeat_pattern = r"(\d)\1{3,}"
    if re.search(repeat_pattern, clean_card):
        return "Invalid"
    return "Valid"
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(validate_credit_card(input().strip()))
