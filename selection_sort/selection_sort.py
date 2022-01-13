def selection_sort(input_list):
  for index in range(0,len(input_list)-1):
    for sub_index in range(index+1,len(input_list)):
      if input_list[index] > input_list[sub_index]:
        temp = input_list[index]
        input_list[index] = input_list[sub_index]
        input_list[sub_index] = temp
    print(input_list)

def main():
  list_length = int(input("Enter Your List Length: "))
  numbers_list = []
  for item in range(0,list_length):
    new_number = int(input("Enter Number: "))
    print(f"Remaining {list_length - item - 1}")
    numbers_list.append(new_number)
  selection_sort(numbers_list)

main()
