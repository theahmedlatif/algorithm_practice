def two_sum(input_list, target_value):

  hash_table = dict()

  for index in range(0,len(input_list)):

    if input_list[index] in hash_table:

      print(f"{input_list[index]} + {hash_table[input_list[index]]}")

      return True

    else:

      hash_table[target_value - input_list[index]] = input_list[index]
    print(hash_table)
  return False

def main():
  numbers_list = [1,2,3,4,5]
  target = 8
  print(two_sum(numbers_list,target))

main()
