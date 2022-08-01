'''An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
'''

#  my solution
def is_isogram(string):
    st = string.lower()
    if len(st) == 0:
        return True
    else:
        for el in st:
            x = st.count(el)
            if x > 1:
                return False
        return True


print(is_isogram(""))

# best solution
#  def is_isogram(string):
#      return len(string) == len(set(string.lower()))