from cbMath import myStatistics
from cbMath import myCalcArea
from cbMath import myArithmetic

print("Homework 1, Chan Hin Man, 10912175")
print("Programme is for finding the mean of 5 numbers")
print("don't know why import so many mods and most of them are unused...\n")

info1 = float(input("Number 1:"))
info2 = float(input("Number 2:"))
info3 = float(input("Number 3:"))
info4 = float(input("Number 4:"))
info5 = float(input("Number 5:"))
N = [info1, info2, info3, info4, info5]

print(myStatistics.myMean(N))
