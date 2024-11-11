#Even or Odd
def even_or_odd(number):
  return 'Even' if number % 2 == 0 else 'Odd'

# Convert a Number to a String

def number_to_string(num):
    return str(num)

#Vowel count

def get_count(sentence):
       return len([x for x in sentence if x in 'aeoiu'])