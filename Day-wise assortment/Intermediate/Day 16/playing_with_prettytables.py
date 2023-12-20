# Importing prettytable module
import prettytable

# Created an object named table
table = prettytable.PrettyTable()


# Creating Table row by row
# But We can also create table column by column
table.field_names = ["Name", "Department", "Batch", "Roll No."]
table.add_row(["Keshav PJ", "EE", 22, 30015])
table.add_row(["Priyashi Goyul", "EC", 22, 10060])
table.add_row(["Madho", "CE", 22, 10034])
table.add_row(["Sparsh", "EE", 22, 10069])

# Since we can change a variable by assigning a different value and align is also an attribute to table
table.align["Name"] = 'l'

# Printing the final table
print(table)
