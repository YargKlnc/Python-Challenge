#I make sure it is cross operating system compatible
import os
import csv

# set path for file, looking at one folder up and finding csv file, and also making sure it is os compatible too
budget_csv = os.path.join("Resources", "budget_data.csv")

#lists created to store data
date = []
profit_losses = []
#total_months = []
monthly_changes = []

#initialize variables
total = 0
profit_losses_total = 0
total_change_of_profits = 0
#initial_profit = 0
final_profit = 0

#this is a csv file so it has a comma delimiter
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #there is header so need to read header first
    csv_header = next(csvreader)
    first_row = next(csvreader)
    initial_profit = int(first_row[1])
    #read through each row of data after the header
    for row in csvreader: # now starts at row 3
        #this is to count and add total number of months
        #calculate total number of all months (dont touch +-) in the dataset
        #total_months = sum(int(row[1]))
        #total_months.append(str(row[1]))a different way than total+1?
        total = total + 1
        
        #add date, list.
        date.append(row[0]) 
        #add profit/losses to calculate profit_losses_total
        #calculate net total amount of all profit/losses over the entire period in the dataset
        profit_losses.append(int(row[1]))
        profit_losses_total = profit_losses_total + int(row[1])

        #calculate month to month change of profits
        #calculate average changes of profit and store in a list
        final_profit = int(row[1])
        change_to_profits_monthly = final_profit - initial_profit

        #store changes_to_profits in a list
        monthly_changes.append(change_to_profits_monthly)

        total_change_of_profits = total_change_of_profits + change_to_profits_monthly
        initial_profit = final_profit

        average_change = (total_change_of_profits/total)
        
        #calculate average in a different way
    #def average(numbers):
        #length = len(numbers)
        #total1 = 0.0
        #for total_change_of_profits in numbers:
            #total1 += total_change_of_profits
        #return total1 / length
    #print(average([total_change_of_profits]))

        #add greatest_increase & greatest_decrease 
        greatest_increase = max(monthly_changes)
        greatest_decrease = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase)]
        decrease_date = date[monthly_changes.index(greatest_decrease)]

#Splitting date possible 
# Split the place into county and state
#split_date = row[0].split("-")
#year.append(split_date[0])
#month.append(split_date[0])
#day.append(split_date[0])

print("Financial Analysis")
print("------------------------------------------------------------------------")
print("Total Months: " + str(total))
print("Total: $" + str(profit_losses_total))
print("Average Change: $" + str(int(average_change))) 
#print(average([total_change_of_profits]))possible if def average is used above
#print("Greatest Increase in Profits: " + month + "-" + year + " " + "(" + greatest_increase + ")" )possible if split date is used above
#print("Greatest Decrease in Profits: " + month + "-" + year + " " + "(" + greatest_decrease + ")" )possible if split date is used above

print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")" )
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")" )

output_file = os.path.join("analysis", "PyBank_Analysis.txt")
with open(output_file, "w") as text:
    text.write("Financial Analysis"+ "\n")
    text.write("-----------------------"+ "\n")
    text.write("Total Months: " + str(total)+ "\n")
    text.write("Total: $" + str(profit_losses_total)+ "\n")
    text.write("Average Change: $" + str(int(average_change))+ "\n") 
    #text.write(average([total_change_of_profits]))might also work if you use def average above
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")" + "\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")" + "\n")