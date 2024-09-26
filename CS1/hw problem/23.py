P =int(input("what is the principle "))
r =int(input("what is the annual intrest rate paid by account "))
n =int(input("what is the number of times per year that the intrest is compounded "))
t =int(input("number of years the account "))

A = P*pow((1+(r/n)),n*t)



print(f"the amount of money in the account is {A:.2f}")

#what is the principle 9
#what is the annual intrest rate paid by account 9
#what is the number of times per year that the intrest is compounded 9
#number of years the account 9
#the amount of money in the account is 21760664753063325144711168.00