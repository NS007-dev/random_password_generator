import random
import math

# random generates random numbers/ items in a list.
# math gives you all the math functions

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special = "@#$%&*"

# all the possible characters that can be chosen from

pass_len = int(input("Enter your password length: "))

alpha_len = pass_len // 2
# does int or floor division, divides then throws awar the decimal. 
# like 11/2 is 5 not 5.5
# here it gives us half len for the letters

num_len = math.ceil(pass_len * 30/100)
# calcs 30% of the total length. make sure to round up so we dont end up with 0 if the bassword is too short.

special_len = pass_len - (alpha_len + num_len)
# takes whatrever is left over after the numbers and letters, and guarantees that all 3 parts add up

# empty list to hold password

password = []

def generate_password(length, array, is_alpha=False) :
    # 3 inputs: length is how many char to generate, array: which pool to pick from: alpha, mum or special. is_alpha: true/false should it capitalise or not.
    for i in range(length):
        #loop repating length times. sequence of nums from 0 up to not including length.
        index = random.randint(0, len(array) -1)
        character = array[index]
        if is_alpha:
            case = random.randint(0,1)
            if case ==1:
                character = character.upper()
        password.append(character)

generate_password(alpha_len, alphabet, True)
generate_password(num_len, numbers)
generate_password(special_len, special)

random.shuffle(password)
gen_password = ""
for i in password:
    gen_password = gen_password + str(i)
print(gen_password)