def Cost_Of_Ticket (adults, children, discount):
    cost = 37550.00
    Gross_price = (cost * adults) + (children * cost/3)
    After_tax = 0.07 * Gross_price + Gross_price
    if discount > 0:
        Total_cost = After_tax -((discount/100)*After_tax)
    else:
        Total_cost = After_tax
    return Total_cost

a = int (input("No.of Adults:"))
c = int (input("No. of children: "))
print ("Total Cost of ticket is : ", Cost_Of_Ticket(a,c,10))

