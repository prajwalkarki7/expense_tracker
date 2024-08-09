import datetime
expenses=[]
def add_expense():
    amount=input("print the amount")
    category=input("enter the category eg:food,rent,household")
    date=input("enter the date or leave blank for today")
    if not date:
        date=str(datetime.datetime.now())
    expenses.append({'amount':amount,'category':category,'date':date})
    print("the expenses added successfully")       
def display_expenses():
    if not expenses:
        print("no data to show")
    else:
        print("the data are:")
        for x in expenses:
            print(f"Date: {x['date']}\n, Amount: {x['amount']}\n, Category: {x['category']}\n")
            print("-"*50)        
def generate_report():
    period = input("Generate report for (week/month): ").lower()
    
    if period not in ['week', 'month']:
        print("Invalid period. Please choose 'week' or 'month'.")
        return

    report_expenses = {}
    
    for expense in expenses:
        if expense['category'] in report_expenses:
            report_expenses[expense['category']] += expense['amount']
        else:
            report_expenses[expense['category']] = expense['amount']

    if not report_expenses:
        print(f"No expenses found for this {period}.")
    else:
        print(f"\n{period.capitalize()} Report:")
        for category, total in report_expenses.items():
            print(f"{category}: {total}")              
def main():
    try:
         while True:
            choice = int(input("Enter your choice:1:add\n 2.display\n 3.generate report\n 4.exit\n "))
            
            if choice == 1:
                add_expense()
            elif choice == 2:
                display_expenses()
            elif choice == 3:
                generate_report()
            elif choice == 4:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except ValueError:
            print("Invalid input. Please enter a number.")

main()
