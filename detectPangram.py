'''
A pangram is a sentence that contains every single letter of 
the alphabet at least once. For example, the sentence "The 
quick brown fox jumps over the lazy dog" is a pangram, because 
it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True 
if it is, False if not. Ignore numbers and punctuation.


'''

def detectPangram(myString):
    my_dict = {
        'a': 'a', 'b': 'b', 'c': 'c',
        'd': 'd', 'e': 'e', 'f': 'f',
        'g': 'g', 'h': 'h', 'i': 'i',
        'j': 'j', 'k': 'k', 'l': 'l',
        'm': 'm', 'n': 'n', 'o': 'o', 
        'p': 'p', 'q': 'q', 'r': 'r',
        's': 's', 't': 't', 'u': 'u',
        'v': 'v', 'w': 'w', 'x': 'x',
        'y': 'y', 'z': 'z',
    }

    new_list = []
    low_str = myString.lower()

    for key in low_str:
        if key in my_dict:
            new_list.append(key)

    if len(set(new_list)) == 26:
        return True
    return False



    
print(detectPangram("The quick brown fox jumps over the lazy dog"))
print(detectPangram('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'))