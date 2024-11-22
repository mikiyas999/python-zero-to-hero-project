import requests

def get_random_quote():
   url = "https://api.quotable.io/random"
   try:
      response = requests.get(url)
      response.raise_for_status()  # Raise an exception for HTTP errors
      quote_data = response.json()
      return f"{quote_data['content']} - {quote_data['author']}"
   except requests.exceptions.RequestException as e:
      return f"Error fetching quote: {e}"

def main():
   expression = input("Enter expression (happy/sad): ").strip().lower()
   if expression not in ['happy', 'sad']:
      print("Invalid expression. Please choose 'happy' or 'sad'.")
      return

   print(f"Quotes for {expression} mood:")
   while True:
      user_input = input("Type 'get' for a quote or 'exit' to stop: ").strip().lower()
      if user_input == 'get':
         print(get_random_quote())
      elif user_input == 'exit':
         print("Exiting the program.")
         break
      else:
         print("Invalid input. Please type 'get' or 'exit'.")

if __name__ == "__main__":
   main()
