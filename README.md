# SCHOOL
<div>
<h4>This is my first repository which contains my first project from my school which has: <h4>
  
This is a menu-driven Python bill management system using the pickle module to store data persistently in a binary file (bill.dat). Here's a clear summary of the code and its working:

🧾 Purpose:
To manage supermarket bills with features like:

Adding bill entries

Viewing bills

Searching bills

Updating recipient details

Deleting bills or specific items

📁 File Used:
bill.dat (binary file storing bills using pickle)

💡 Main Features:
1. data(): Insert new bills
Takes input for:

Bill number

Recipient's name, address, mobile number

Products purchased (name, quantity, rate)

Stores all this as a list structure and saves to bill.dat using pickle.dump.

2. dis(): Display all bills
Reads all bill data from bill.dat using pickle.load.

Displays bills in a printable receipt format with:

Shop name

Bill info

Product list with total value

3. search(): Search specific bill
Lets user search by:

Bill number

Recipient name

Address

Mobile number

If found, it asks whether to print the full bill or not.

4. update(): Update bill details
Updates recipient info by bill number:

Name

Address

Mobile number

Overwrites updated data back into the file.

5. dle(): Delete bill or item
Two options:

Delete full bill by bill number

Delete a specific product from a bill

Updates the file accordingly.

6. Main Menu Loop
Repeatedly displays a menu until user chooses Exit (0)

User chooses:
[1] Insert Bill
[2] Display Bills
[3] Search Bill
[4] Update Bill
[5] Delete Bill/Items
[0] Exit

🧠 Data Structure Used:
Each bill is stored as a list:

python
Copy
Edit
[d, e, f, g, [[item1_name, qty, rate], [item2_name, qty, rate], ...]]
Where:

d: Bill no.

e: Recipient name

f: Address

g: Mobile no.

The last element is a list of products.

✅ Advantages:
Easy-to-use menu system

Persistent storage via pickle

Supports bill search and updates

Simple binary file management
