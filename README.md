# Encrypter Gen 2
JX Encrypter Gen2

Basic description and usage instruction

In a nutshell, this python script will encode (maybe encrypt) the text data you enter into it. It will save the encoded data into a filename of your choice (will add a JE2F extension to it coz looks cool B) ).
The encrypted file (with the .JE2F ext) can be decrypted using the decrypter given alongside. In this, you need to enter the path of the encrypted file (with the extension obv, like anywhere else); and it will print the single sentence which was encrypted.
For those curious, Gen1 was basically replacing each character with a 4 (or 5, cant rememeber) digit numerical code, so wasnt anything strong. This one however, essentially each file has its unique 'encryption key' which is hidden in the file itself, and can only be found by the algorithm.
'Encryption Key' - By this I mean that each character has a unique code representing it, which varies with each execution, as you will see.

# Those who want to know the algorithm
I wont get into the nitty-gritty of it, for that there is the (quite (un)readable) code. But basically what it does is, after you enter your text input. It will generate some 6 - 7 random numbers. and then it will make a list of all possible numbers which can be obtained by adding or multiplying any 2 of these random numbers. it will then sort the list, and filter the first 63 distinct elements. The use of this 63 list will be seen later.

It will a make file consisting of multiple units, where each unit is a string of 9 characters with a '.' in the middle(like abcd.edfh). To be precise, there will be max(63 list) number of units(why? read ahead). So the file will look something like 123f.4iogbsfo.efkejofb.nobo and so on(there is no space within the units). What actually happens is that the 2nd set of 4 characters(the 4 chars after the '.' ) represent the key(the encoded form) for each alphabet. So the 63 numbers which we had before; the first number will tell us the position of the Encoded form of the character 'a', the second number will tell us the Encoded form of the character 'b' and so on.(FYI, 63 included a-z,A-z,0-9 and SPACE(" ") ). At all the other positions (positions which dont come in the 63 list), it is just random strings which arent a part of the 63 list. Due to this reason, for the 63rd character as well, to ensure that it is also represented in the file, we need atleast those many units, so that the last unit will represent the 63rd character.

Now this was how to find the KEYS (the encoded forms) of each alphabet. To read the actual data which we wrote, we just read the first 4 characters (the characters before the '.' ) of each segment (segment was abcd.efgh as described earlier). If the first 4 chars match any of the keys, it represents some letter written by the user, else its just garbage to be ignored.

Now, you may have realised that the 6-7 unique numbers are like the key to the whole encryption, since they reveal the positions of all the characters. These are embedded at the start of the encrypted file in a unique format. Like if the numbers are 2 3 4 5 6 7 8. each will be converted to binary, and in the binary representation, each 0 will be replaced by a digit divisible by 2, and each 1 will be replaced by a digit not divisible by 2. So while decrypting, first the nummbers are converted to binary by taking modulus with 2, then binary representation is converted to decimal representation, and then all the products and sums will be made and checked to find the unique 63 positions.

# Limitations
Ofcourse this algorithm has its limitations. 

There should be a theoretical maximum value to the size of input data, and for bigger files, the computation time may be higher than usual, and ofcourse it doesnt support non conventional characters like .,_,! and so on. Also worth mentioning, currently it only supports one line of input, but that can probably be extended by making a file for each line in a multiple line text file, and somehow embedding those files together; OR; making a single encryption key for each file and creating a special key for the newline character, so that the Decrypter identifies the newline char and accordingly prints in a new line, although if the user explicitly enters '\n' in the file, this may cause issues.
To be addressed in later releases

