#!/usr/bin/env python
# -*- coding: utf-8 -*-
__AUTHOR__ = "Thomas Thaulow Stöcklin"
__EMAIL__ = "thomasts@stud.ntnu.no"

def ParseFile(FileName):                                            # define parsing file contents and add to variable function
    ValidCharacters = []                                            # Initiate empty list
    for char in range(32, 126):                                     # Find valid ascii characters
        ValidCharacters.append(chr(char))                           # Add valid ascii codes to list ValidCharacters
    with open(FileName, "r") as file:                               # open file as read, and proceed with file
        List = []                                                   # Initiate empty list
        for line in file.read().splitlines():                       # For every line in the file, split input into line 
            if [char in line for char in ValidCharacters]:          # Check if characters from split iteration is present in ValidCharacters
                List.append(line)                                   # If character is present in ValidCharacter, append to List variable. 
        return(List)                                                # Return List variable back to main function

def WriteFile(FileName,Content):                                    # define Writing Contents to File function
    file = open(FileName, "w")                                      # open file in write format, overwriting any previous content
    file.write(str(Content))                                        # write attribute contents to file as string 
    file.close()                                                    # close file

def CharToAscii(Char):                                              # define Character to Ascii function                
    Ascii = []                                                      # initiate empty list
    for i in range (len(Char)):                                     # loop n times the amount of characters of input
        Ascii.append(ord(Char[i]))                                  # convert input to ascii, append to variable name Ascii with ascii format
    return(Ascii)                                                   # return list "Ascii" to main function
                                                                 
def Hash(AsciiPass):                                                # define Hashing functions

    def HashH1(AsciiPass):                                          # define hashing function 1
        temp = AsciiPass                                            # transfer AsciiPass to new variable for manipulation
        Hash = 1                                                    # Define function Hash as 1, to initiate multiplication
        for i in temp:                                              # For every integer in new variable
            Hash *= i                                               # Multiply by amount of iteration
        Hash = Hash % (2**24-3)                                     # Perform Modulos 2^24 -3 
        return(Hash)                                                # Return hashed input to Hash function

    def HashH2(AsciiPass):                                          # define hashing function 2
        temp = AsciiPass                                            # transfer AsciiPass to new variable for manipulation
        Hash = 0                                                    # Define function Hash as 0, initiating addition 
        for i in temp:                                              # For every integer in new variable 
            Hash += i                                               # Addition by amount of iteration
        Hash = Hash % (2**24-3)                                     # Perform Modulos 2^24 -3
        return(Hash)                                                # Return hashed input to Hash function

    def HashH3(AsciiPass):                                          # define hashing function 3
        temp = []                                                   # initiate empty list
        temp += AsciiPass                                           # Add function input to temporarily variable for manipulation
        Hash = 1                                                    # Define function Hash as 1, to initiate multiplication
        while len(temp) % 3 != 0:                                   # If input is not in a group of 3, loop this code
            temp.append(32)                                         # add 32 to the end of temp variable, start loop again
        else:                                                       # if input length is a group of 3    
            addition = 0                                            # Define function Hash as 0, initiating addition
            for i in range((len(temp))):                            # For every integer in new variable
                addition += temp[i]                                 # Add temp to addition variable for manipulation
                if (i+1) % 3 == 0:                                  # if iteration+1 equals 3
                    Hash *= addition                                # multiply Hash with addition in hash variable
                    addition = 0                                    # Set addition to 0, start new count of 3
        Hash = Hash % (2**24-3)                                     # Perform Modulos 2^24 -3
        return(Hash)                                                # Return Hash value to main function
    
    def HashH4(AsciiPass):                                          # define hashing function 4
        temp = []                                                   # initiate empty list
        temp += AsciiPass                                           # Add function input to temporarily variable for manipulation
        Hash = 1                                                    # Define function Hash as 1, to initiate multiplication
        while len(temp) % 5 != 0:                                   # If input is not in a group of 5, loop this code
            temp.append(32)                                         # add 32 to the end of temp variable, start loop again
        addition = 0                                                # Define function Hash as 0, initiating addition
        for i in range((len(temp))):                                # For every integer in new variable
            addition += temp[i]                                     # Add temp to addition variable for manipulation
            if (i+1) % 5 == 0:                                      # if iteration+1 equals 5
                Hash *= addition                                    # multiply Hash with addition in hash variable
                addition = 0                                        # Set addition to 0, start new count of 5
        Hash = Hash % (2**24-3)                                     # Perform Modulos 2^24 -3
        return(Hash)                                                # Return Hash value to main function

    def HashH5(AsciiPass):                                          # define hashing function 5
        temp = []                                                   # initiate empty list
        temp += AsciiPass                                           # Add function input to temporarily variable for manipulation
        Hash = 0                                                    # Define function Hash as 0, to initiate addition
        while len(temp) % 3 != 0:                                   # If input is not in a group of 3, loop this code
            temp.append(32)                                         # add 32 to the end of temp variable, start loop again
        else:                                                       # if input is in group of 3
            multiplication = 1                                      # initiating multiplication by setting value to 1
            for i in range((len(temp))):                            # For every integer in new variable
                multiplication *= temp[i]                           # multiply Hash with addition in temp variable
                if (i+1) % 3 == 0:                                  # if iteration+1 equals group of 3
                    Hash += multiplication                          # Addition of multiplications sum from loop to Hash
                    multiplication = 1                              # Set multiplication to 0, start new count of 3
        Hash = Hash % (2**24-3)                                     # Perform Modulos 2^24 -3
        return(Hash)                                                # Return Hash value to main function

    def HashH6(AsciiPass):                                          # define hashing function 6
        temp = []                                                   # initiate empty list
        temp += AsciiPass                                           # Add function input to temporarily variable for manipulation
        Hash = 0                                                    # Define function Hash as 0, to initiate addition
        while len(temp) % 5 != 0:                                   # If input is not in a group of 5, loop this code
            temp.append(32)                                         # add 32 to the end of temp variable, start loop again
        else:                                                       # if input is in group of 5
            multiplication = 1                                      # initiating multiplication by setting value to 1
            for i in range((len(temp))):                            # For every integer in new variable
                multiplication *= temp[i]                           # multiply Hash with addition in temp variable
                if (i+1) % 5 == 0:                                  # if iteration+1 equals group of 5
                    Hash += multiplication                          # Addition of multiplications sum from loop to Hash
                    multiplication = 1                              # Set multiplication to 0, start new count of 5
        Hash = Hash % (2**24-3)                                     # Perform Modulos 2^24 -3
        return(Hash)                                                # Return Hash value to main function

    def HashH7(AsciiPass):                                          # define hashing function 7
        temp = []                                                   # initiate empty list
        temp += AsciiPass                                           # Add function input to temporarily variable for manipulation
        odd = 0                                                     # initiate variable with 0 value for counting odd
        even = 0                                                    # initiate variable with 0 value for counting even 
        for i in range((len(temp))):                                # For every integer in new variable
            if i % 2 == 0:                                          # if number is even
                even += temp[i]                                     # add number to even list
            else:                                                   # if number not even
                odd += temp[i]                                      # add number to odd list
        Hash = odd * even                                           # multiply odd and even variable
        Hash = Hash % (2**24-3)                                     # Perform Modulos 2^24 -3 on value
        return(Hash)                                                # Return Hash value to main function

    def HashH8(AsciiPass):                                          # define hashing function 8
        temp = []                                                   # initiate empty list
        temp += AsciiPass                                           # Add function input to temporarily variable for manipulation
        Hash = 0                                                    # Define function Hash as 0, to initiate addition
        q = 31                                                      # Define q as the value 31 as required in task
        for i in range(len(temp)):                                  # For every integer in new variable                 
            Hash += (temp[i]) * (pow(q,i))                          # Add input multiplied by modulos q (31) in iteration (n)
        Hash = Hash % (2**24-3)                                     # Perform Modulos 2^24 -3 on value                                 
        return(Hash)                                                # Return Hash value to main function

    Hash1 = HashH1(AsciiPass)                                       # Run HashH1 function, set return value as Hash1 variable
    Hash2 = HashH2(AsciiPass)                                       # Run HashH2 function, set return value as Hash2 variable
    Hash3 = HashH3(AsciiPass)                                       # Run HashH3 function, set return value as Hash3 variable
    Hash4 = HashH4(AsciiPass)                                       # Run HashH4 function, set return value as Hash4 variable
    Hash5 = HashH5(AsciiPass)                                       # Run HashH5 function, set return value as Hash5 variable
    Hash6 = HashH6(AsciiPass)                                       # Run HashH6 function, set return value as Hash6 variable
    Hash7 = HashH7(AsciiPass)                                       # Run HashH7 function, set return value as Hash7 variable
    Hash8 = HashH8(AsciiPass)                                       # Run HashH8 function, set return value as Hash8 variable
    return (Hash1, Hash2, Hash3, Hash4, Hash5, Hash6, Hash7, Hash8)     # Return all 8 attributes to main function

def SetBits(hashes):                                                    # Initiate Set Bits function
    for hash in hashes:                                                 # For every item in input
            bloomfilter[hash+2] = 1                                     # add 1 to bloomfilter index equal to every item +2
    return bloomfilter                                                  # return bloomfilter value to main function

def VerifyBits(hashes):                                                 # Initiate Verify Bits function
    count = 0                                                           # Set variable count to 0
    for hash in hashes:                                                 # For every item in input
        if bloomfilter[hash+2] == 1:                                    # if bloomfilter index of hash value + 2 equals 1
            count += 1                                                  # add 1 to variable "count", to track identical values
            continue                                                    # Continue loop to next iteration
        else:                                                           # if bloomfilter index of hash value +2 does not equal 1
            return True                                                 # Return True statement to main function, all bits are valid
    return False                                                        # Return False statement to main function, one bit is bad

def BitToAscii(bits):                                                       # define bit to ascii function
    BitString = "".join(str(item) for item in bits)                         # convert list BitString to strings
    Bloomfilter = ("")                                                      # Initiate empty bloomfilter
    BinaryList = [BitString[i:i + 6] for i in range(0, len(BitString), 6)]  # For every 6th bit, add to BinaryList attribute
    for i in BinaryList:                                                    # For every item in BinaryList
        Bloomfilter += alphabet[int(i, 2)]                                  # Add the ascii value by using the index of the alphabet
    return(Bloomfilter)                                                     # Return Ascii output to main function

############################ CONFIGURATION ##############################

FILE = "TrainingBF.txt"             # Password file to be trained
PASSWORDFILE = "TestPW_583463.txt"  # List of passwords to check
OUTPUTNAME = "BF_583463.txt"        # Name of output bloomfilter 

######################### START OF APPLICATION ###########################

###### TRAIN BLOOMFILTER ######
if __name__ == '__main__':                              #initiate file
    bloomfilter =  [0] * (2+(2**24))                    #initiate empty array with 0, length 2, power of 24) + 2 bits. (16,777,218 / 6 = 2,796,203)
    alphabet = (list(map(chr, range(65, 91))))+(list(map(chr, range(97, 123))))+(list(map(chr, range(48, 58))))+["+"]+["/"]

    PasswordList = ParseFile(FILE)                      # Parse file and add all passwords in variable 
    for char in PasswordList:                           # Iterate each password in the list
        AsciiPass = CharToAscii(char)                   # Convert characters to ASCII number
        HashList = Hash(AsciiPass)                      # Hash ASCII list with 8 different hashes. Returns 8 hashes per ASCII variable
        BitList = SetBits(HashList)                     # Use HashList as index to set bits as 1 in filter. 
    Bloomfilter = BitToAscii(BitList)                   # Convert set bits as binary to ascii
    WriteFile(OUTPUTNAME,str(Bloomfilter))              # Write string version of bloomfilter attribute to txt file

    ###### VERIFY PASSWORDS ######
    Passwords = ParseFile(PASSWORDFILE)                 # # Parse file and add all passwords in variable 
    for char in Passwords:                              # Iterate each password in the list
        AsciiPass = CharToAscii(char)                   # Convert characters to ASCII number
        HashList = Hash(AsciiPass)                      # Hash ASCII list with 8 different hashes. Returns 8 hashes per ASCII variable
        if VerifyBits(HashList) is True:                # Verify if password index is unique from bloomfilter, if true 
            print("Password",char, "was accepted")      # print acceptance message
        else:                                           # if password index is not unique from bloomfilter, 
            print("Password", char, "was DENIED")       # print denial message
