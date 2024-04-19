The Caesar cipher is one of the simplest and oldest methods of encryption, dating back to Julius Caesar in ancient Rome. 
It is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. 
For example, with a shift of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on.

The original Caesar Cipher method only handled upper case alphabets and thus only had 26 possible keys, that is, 26 possible shift values(0-25).
Here, We Utilise the ascii values of characters to implement Caesar Cipher and thus effectively increase the possible keys to 256(0-255).
Any Shift value given from the user that is above 255 will be effectively converted to the value mod 256.
