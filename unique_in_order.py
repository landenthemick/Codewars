def unique_in_order(input_word):
  output_list = []
  current_letter = None

  for letter in input_word:
      if letter != current_letter:
          output_list.append(letter)
          current_letter = letter
  return output_list

print(unique_in_order("AAAABBBCCDAABBB"))