import re
import email.utils

n = int(input())

for _ in range(n):
    name_email = input()
    parsed = email.utils.parseaddr(name_email)
    email_address = parsed[1]
    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    
    if re.match(pattern, email_address):
        print(email.utils.formataddr(parsed))
