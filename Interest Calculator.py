"Interest Calculator"
import math
answer2 = 1
ValueError is False
def interesteq(p,r,n,t):
   return float(float(p)*(1+(float(r)/float(n)))**(float(r)*float(t)))
def continouseq(p,r,t):
  return float(float(p)*float(math.exp(1))**(float(r)*float(t)))
print("Hello, please state which equation you would like to use,")
while answer2 == 1:
    answer = input("Regular Compounded Interest for 1, and Continoutsly Compounded interest for 2:")  
    if answer == ("1")  or answer == ("2"):
       answer2 == 2 
       break
if answer == ("1"): print("Type in your starting amount, your rate of interest, the number of times the interest is compounded in a year, and your time")
if answer == ("2") : print("Type in your starting amount, your interest rate, and your time in years.")
p = input("What is your starting amount of money:")
r = input("What is the rate of your interest in decimal form:")
if answer == ("1") : n = input("What is the number of times your interest gets compounded in a year:")
t = input("How much time in years:")
if answer == ("1") : print(interesteq(p,r,n,t))
if answer == ("2") : print(continouseq(p,r,t))
