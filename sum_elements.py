#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases
def get_number_of_elements(max_value):
   while True:
      try:
         n = int(input(f"Enter the number of elements (1-{max_value}): "))
         if 1 <= n <= max_value:
            return n
         else:
            print(f"Invalid input. Please provide a number between 1 and {max_value}.")
      except ValueError:
         print("Invalid input. Please enter a valid integer.")

def get_elements(n):
   elements = []
   print(f"Enter {n} integers:")
   for _ in range(n):
      while True:
         try:
            elements.append(int(input()))
            break
         except ValueError:
            print("Invalid input. Please enter a valid integer.")
   return elements
MAX = 100

def calculate_sum(arr):
   result = 0
   for num in arr:
      result += num
   return result

def main():
   try:
      n = int(input("Enter the number of elements (1-100): "))
      if not 1 <= n <= MAX:
            print("Invalid input. Please provide a digit ranging from 1 to 100.")
            exit(1)

      arr = []

      print(f"Enter {n} integers:")
      for _ in range(n):
            try:
               arr.append(int(input()))
            except ValueError:
               print("Invalid input. Please enter valid integers.")
               exit(1)

      total = calculate_sum(arr)

      print("Sum of the numbers:", total)

   except KeyboardInterrupt:
      print("\nProgram terminated by user.")
      exit(1)

if __name__ == "__main__":
   main()
