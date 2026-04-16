import re

vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"

pattern = r'(?<=[%s])([%s]{2,})(?=[%s])' % (consonants, vowels, consonants)

match = re.findall(pattern, input(), re.I)

if match:
    print('\n'.join(match))
else:
    print("-1")
