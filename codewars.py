def words_loop():
  words = ['I', 'need', 'another', 'five', 'years']
  first_letters = ''

  for word in words:
      first_letters = first_letters + word[0]
  print(first_letters)

words_loop()

def words_list():
   words = ['I', 'need', 'another', 'five', 'years']
   first_letters = []

   for word in words:
      first_letters.append(word[0])

   result = ''.join(first_letters)
   print(result)

words_list()