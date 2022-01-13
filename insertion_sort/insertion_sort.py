def insertion_sort(input_list):
  print(input_list)
  current = 0
  for index in range (1, len(input_list)):
    sub_index = index - 1
    current = input_list[index]
    while(input_list[sub_index] > current and sub_index >= 0):
      input_list[sub_index + 1] = input_list[sub_index]
      sub_index -= 1 
    input_list[sub_index + 1] = current
    print(input_list)

def main():
  list_length = int(input("Enter Your List Length: "))
  numbers_list = []
  for item in range(0,list_length):
    new_number = int(input("Enter Number: "))
    print(f"Remaining {list_length - item - 1}")
    numbers_list.append(new_number)
  insertion_sort(numbers_list)

main()
