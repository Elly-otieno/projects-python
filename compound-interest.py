# compound interest calculator
# A = P (1+(r/n))^t   ...

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input('Enter Principle: '))
    if principle <= 0:
        print('Principle can`t be less than or equal to zero')

while time <= 0:
    time = int(input('Enter time: '))
    if time <= 0:
        print('Time can`t be less than or equal to zero')

while rate <= 0:
    rate = float(input('Enter Rate: '))
    if rate <= 0:
        print('Rate can`t be less than or equal to zero')


interest = principle * pow((1 + rate / 100), time)

print(f'Your interest after {time} year/s : ksh {interest:.2f}')  #to 2 dp ---> .2f
