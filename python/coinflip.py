#this program will flip a coin for you!
import random
def main():
    print("Welcome to the coin flipper!")
    print("This program will flip a coin for you!")
    print("Please enter the number of times you would like to flip the coin:")
    #get the number of times to flip the coin
    num = int(input())
    #flip coin
    for i in range(num):
        flip = (random.randint(0,1))
        #print the result
        if flip == 0:
            print("Heads")
        elif flip == 1:
            print("Tails")  
main()