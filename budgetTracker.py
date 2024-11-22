Simple Budget Tracker Using Dictionaries

class BudgetTracker:
   def __init__(self):
      self.income = {}
      self.expenses = {}

   def add_income(self, amount, category):
      if category in self.income:
         self.income[category] += amount
      else:
         self.income[category] = amount

   def add_expense(self, amount, category):
      if category in self.expenses:
         self.expenses[category] += amount
      else:
         self.expenses[category] = amount

   def get_total_income(self):
      return sum(self.income.values())

   def get_total_expenses(self):
      return sum(self.expenses.values())

   def display_summary(self):
      print('Income Summary:')
      for category, amount in self.income.items():
         print(f'{category}: ${amount}')
      print('Total Income:', self.get_total_income())

      print('Expenses Summary:')
      for category, amount in self.expenses.items():
         print(f'{category}: ${amount}')
      print('Total Expenses:', self.get_total_expenses())

      print('Net Savings:', self.get_total_income() - self.get_total_expenses())

# Example Usage
tracker = BudgetTracker()
tracker.add_income(5000, 'Salary')
tracker.add_income(200, 'Freelance')
tracker.add_expense(1500, 'Rent')
tracker.add_expense(200, 'Groceries')
tracker.add_expense(100, 'Utilities')
tracker.display_summary()
