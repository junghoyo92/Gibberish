#CSE231 section 2
#proj03 Gibberish

# This part of the program imports the string module

import string

while True:

    # This part of the program ask for inputs for the gibberish syllables and the word to translate
    first= input('Enter your first gibberish syllable: ')
    second= input('Enter your second gibberish syllable: ')
    word= input('Please enter a word you want to translate: ')
    print('Original word: ', word)
    vowel= 'aeiouAEIOU'
    consonates= 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWYXZ'
    start=0
    gibberish= ""
    whether_first=0

    # This part of the program is suppose to calculate for the wildcard and translate the word
    # Unfortunately i could not get this portion to work properly.

    for ch in first or second:
        if first[0]=='*':
            if ch not in vowel:
                letter = ch
            elif ch in vowel and whether_first==0:
                letter = first.replace('*', ch)
                whether_first=1
        elif second[0]=='*':
            if ch not in vowel:
                letter = ch
            elif ch in vowel and whether_first==0:
                letter = second.replace('*', ch)
                whether_first=1
        else:
            break
        gibberish= gibberish + letter
        print('Say this gibberish word: ', gibberish)

    # This Part of the program translates the word to gibberish

    for i,ch in enumerate(word):
        if ch in consonates:                            # if the character is a consonate, it will add that letter to the empty string
            letter = ch
        elif ch in vowel and whether_first ==0:         # if the character is a vowel and whether first = 0, then it will replace the vowel with the first syllable and add the syllable to the empty string
            letter= ch.replace(ch, first)
            whether_first =1
        else:                                           # if the character is a vowel after the first vowel, then it will replace the vowel with the second syllable and add the syllable to the empty string
            letter= ch.replace(ch, second)
        gibberish = gibberish + letter   
    
    print('Say this gibberish word: ', gibberish)                                    # this will print the final word
    
    answer= input('Would you like to play again (y for yes & n for no)? ')
    if answer=='y':
        continue

    else:
        print('Thank you for playing')
        break
