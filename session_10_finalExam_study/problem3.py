# Implement a function that meets the specifications below.

# def cipher(map_from, map_to, code):
#     """ map_from, map_to: strings where each contain 
#                           N unique lowercase letters. 
#         code: string (assume it only contains letters also in map_from)
#         Returns a tuple of (key_code, decoded).
#         key_code is a dictionary with N keys mapping str to str where 
#         each key is a letter in map_from at index i and the corresponding 
#         value is the letter in map_to at index i. 
#         decoded is a string that contains the decoded version 
#         of code using the key_code mapping. """
#     # Your code here
# For example,

# cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may 
# not be the same) ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
# Paste your entire function, including the definition, in the box below. 
# Do not leave any debugging print statements.

 def cipher(map_from, map_to, code):

# Step 1: Create the mapping dictionary
    key_code = {}
    
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
        
# Step 2: Decode the message using the dictionary
        
    decoded = ""
    
    for char in code:
        decoded += key_code[char]
# Step 3: Return the mapping dictionary and decoded message      
    return decoded, key_code

print(cipher("abcd", "dcba", "dab"))
