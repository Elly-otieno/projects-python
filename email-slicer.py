email = input('Enter your Email address: ')

index = email.index('@')

username = email[:index]
domain = email[index + 1 :]

print(f'Your username is {username} and the domain is {domain}')