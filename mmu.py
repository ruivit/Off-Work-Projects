

import math
import re


def main():
    # input the user for the memory size
    mem_size = int(input("Enter the memory size (in KB): "))
    # input the user for the page size
    page_size = int(input("Enter the page size (in KB): "))

    mem_size_to_power = int(math.log(mem_size, 2) + 10)
    page_size_to_power = int(math.log(page_size, 2) + 10)

    # input for the number to be translated
    num_to_translate = int(input("Enter the number to be translated: "))

    # print the binary number
    print("\nThe binary number is: ", dec_to_bin(num_to_translate, mem_size_to_power))

    # calculate the number of bits for the offset
    offset_bits = mem_size_to_power - page_size_to_power

    # convert the binary offset to decimal
    print("The offset is: ", offset_bits, " because ", mem_size_to_power, "-", page_size_to_power, "=", offset_bits)
    print("Offset in binary: " + dec_to_bin_nspaces(offset_bits, offset_bits))

    # get the first offset bits from the binary number
    binary_offset = dec_to_bin(num_to_translate, mem_size_to_power)
    binary_offset.replace(" ", "")
    binary_offset = binary_offset[:offset_bits + 1]
    tablePosition = bin_to_dec(binary_offset) 
    print("\n>>> Check position " + str(tablePosition) + " in the page table")

    # input for the substitution
    substitution = int(input("Enter the substitution: "))

    # substitute the binary offset with the substitution
    # it will be the first X bits of the binary number (from left)
    binary_substitution = dec_to_bin_nspaces(num_to_translate, mem_size_to_power)

    # replace the first offset left bits with the substitution
    binary_substitution = re.sub(r'^.{0,' + str(offset_bits) + '}', str(substitution), binary_substitution)
    

    # print the binary number with the substitution and decimal
    decimal = bin_to_dec(binary_substitution)
    bin = dec_to_bin(decimal, mem_size_to_power)
    print("\nThe binary number with the substitution is: " + bin)
    print("The decimal number with the substitution is: " + str(decimal))
    
    # dont quit the program
    input("")


def dec_to_bin(num, maxSize):
    """ convert decimal to binary splitting the number in 4 bits 0010 0011 0111"""
    # convert the number to binary
    num_in_bin = bin(num)[2:]

    # add the 0s to the left 
    num_in_bin = num_in_bin.zfill(maxSize)

    # split the number in 4 bits starting from the end
    for i in range(len(num_in_bin), 0, -4):
        num_in_bin = num_in_bin[:i] + " " + num_in_bin[i:]

    return num_in_bin

def dec_to_bin_nspaces(num, maxSize):
    """ convert decimal to binary splitting the number in 4 bits 0010 0011 0111"""
    # convert the number to binary
    num_in_bin = bin(num)[2:]

    # add the 0s to the left 
    num_in_bin = num_in_bin.zfill(maxSize)

    return num_in_bin

def bin_to_dec(num):
    """ remove the spaces and convert the binary number to decimal """
    num = num.replace(" ", "")
    return int(num, 2)

""" main """
if __name__ == "__main__":
    main()