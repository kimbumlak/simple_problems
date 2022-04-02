"""
x is a string representing a book of text. The pages are separatd by \b. The lines by \n. 

Write a function that reverses the
- order of pages
- order of lines in each page
- order of words in each line
- don't reverse the characters in each word
"""
"""
Original = "the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"
Page reverse = "\bThe big lion chased the deer\nThe monkey ate the bananas\n\bthe brown fox jumped over the fence\nthe brown bear fell down the hill\n"
Line reverse = "\b\nThe monkey ate the bananas\nThe big lion chased the deer\b\nthe brown bear fell down the hill\nthe brown fox jumped over the fence"
Word reverse = "\b\nbananas the ate monkey The\ndeer the chased lion big The\b\nhill the down fell bear brown the\nfence the over jumped fox brown the"
"""

# This function is a helper function to add back removed delimiter
# in the list after using a split function. Reason for adding back
# removed delimiter is to properly reverse delimiters as well.
def split_string_while_keeping_delimiter(s_list, delimiter):
    i = 0
    while i < len(s_list) - 1:
        if s_list[i] and s_list[i+1] != '':
            s_list.insert(i+1, delimiter)
            i += 1
        i += 1
    # If delimiter is located in either start or end of string, using split
    # function replaces empty string to that position in the list. Therefore,
    # code below adds back removed delimiter in either first or last position
    # of list where it has empty string.
    start_idx, end_idx = 0, len(s_list) - 1
    if s_list[start_idx] == '':
        s_list[start_idx] = delimiter
    if s_list[end_idx] == '':
        s_list[end_idx] = delimiter
    return s_list

# Using commented out print statement will show step by step reverse procedure
def reverse_test(x):
    page_split = x.split('\b')
    page_split = split_string_while_keeping_delimiter(page_split, '\\b')
    page_split.reverse()
    #print(page_split)
    line_split = []
    for page in page_split:
        if page == '\\b':
            line_split.append(page)
        else:
            lines = page.split('\n')
            lines = split_string_while_keeping_delimiter(lines, '\\n')
            lines.reverse()
            line_split.extend(lines)
    #print(line_split)
    for i in range(len(line_split)):
        line = line_split[i]
        if line == '\\b' or line == '\\n':
            continue
        words = line.split(' ')
        words.reverse()
        words = ' '.join(words)
        line_split[i] = words
    #print(line_split)        
    return "".join(line_split)


test_input = "the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"
print(reverse_test(test_input))



"""
Given a nested list with arbitrary level of nesting, write a function, flatten to flatten it.

sample input = [[4,5],[[1,2,3]],6]

flatten(x) --> [4,5,1,2,3,6]
"""

def flatten(x, result=[]):
    for i in x:
        if type(i) == list:
            flatten(i, result)
        else:
            result.append(i)
    return result            


flatten_test = [[4,5],[[1,2,3]],6]
print(flatten(flatten_test))
