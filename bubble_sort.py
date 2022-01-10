def bubble_sort(numbers_list):
  swap = False
  while not swap:
    swap = True
    print(numbers_list)
    for i in range(1, len(numbers_list)):
      if numbers_list[i-1] > numbers_list[i]:
        swap = False
        temp = numbers_list[i]
        numbers_list[i] = numbers_list[i-1]
        numbers_list[i-1] = temp

def main():
  list_length = int(input("Enter Your List Length: "))
  numbers_list = []
  for item in range(0,list_length):
    new_number = int(input("Enter Number: "))
    print(f"Remaining {list_length - item - 1}")
    numbers_list.append(new_number)
  bubble_sort(numbers_list)

main()
