# SCHOOL PROJECT
<div>
<h4>This is my first repository which contains my first project from my school<h4>

<h1>Bill Management System</h1>
This is a menu-driven Python bill management system using the pickle module to store data persistently in a binary file (bill.dat). Here's a clear summary of the code and its working:

<h2>🧾 Purpose:</h2>
<p>To manage supermarket bills with features like:</p>
<ul>
         <li>Adding bill entries</li>
         <li>Viewing bills</li>
         <li>Searching bills</li>
         <li>Updating recipient details</li>
         <li>Deleting bills or specific items</li>
</ul>

<h2>📁 File Used</h2>
    <ul>
        <li><span class="code">bill.dat</span> - Binary file to store bill data using <span class="code">pickle</span></li>
    </ul>

<h2>🔧 Main Features</h2>
    <ol>
        <li><strong>Insert Data (<span class="code">data()</span>)</strong>:
            <ul>
                <li>Adds bill number, recipient details, and product list</li>
                <li>Stores data in binary format using <span class="code">pickle.dump()</span></li>
            </ul>
        </li>
        <li><strong>Display Bills (<span class="code">dis()</span>)</strong>:
            <ul>
                <li>Reads all data and prints formatted bill</li>
            </ul>
        </li>
        <li><strong>Search Bills (<span class="code">search()</span>)</strong>:
            <ul>
                <li>Search by Bill No, Name, Address, or Mobile No</li>
                <li>Option to print the found bill</li>
            </ul>
        </li>
        <li><strong>Update Bill (<span class="code">update()</span>)</strong>:
            <ul>
                <li>Update recipient name, address, or mobile number</li>
            </ul>
        </li>
        <li><strong>Delete Bill or Items (<span class="code">dle()</span>)</strong>:
            <ul>
                <li>Delete entire bill or just specific item(s) from it</li>
            </ul>
        </li>
    </ol>

<h2>🔁 Menu Loop</h2>
    <p>The program continuously shows a menu until Exit (0) is selected:</p>
    <pre class="code">
[1] Insert Data in Bill
[2] Display of Bill
[3] Search of Bill
[4] Update of Bill
[5] Deletion of Bill
[0] Exit
    </pre>

<h2>🧠 Data Format</h2>
    <p>Each bill is stored as a Python list:</p>
    <pre class="code">[BillNo, Name, Address, Mobile, [[Item1, Qty, Rate], [Item2, Qty, Rate], ...]]</pre>

<h2>📎 Notes</h2>
    <ul>
        <li>Each bill is stored as a list containing recipient details and a list of items.</li>
        <li>Each item is stored as a list containing item name, quantity, and rate.</li>
        <li>UI is entirely terminal-based with formatted text output.</li>
    </ul>

    <h2>✅ Sample Output Format</h2>
    <pre>
    |                           >SUPER MART<                           |
    |------------------------PHONE:01125268494-------------------------|
    |                              >BILL<                              |
    |==================================================================|
        ---->BILL NO : 001
        ---->NAME    : John Doe
        ---->ADDRESS : New Delhi
        ---->MOBILE  : 9876543210
        ---->DATE    : 02/08/2025 (15:34:22)
    |__________________________________________________________________|
       S.NO     ITEMS       QTY/KG/L   RATE     VALUE
         1      Soap            2        30       60
         2      Milk            1        50       50
    --------------------------------------------------------------------
             TOTAL ITEMS: 2                     TOTAL: ₹110
    ____________________________________________________________________
          THANKS FOR SHOPPING WITH SUPER MART
    ********************************************************************
    </pre>

<h2>✅ Advantages</h2>
    <ul>
        <li>Simple and menu-driven interface</li>
        <li>Persistent data using binary file</li>
        <li>Search, update, and delete features included</li>
        <li>Readable bill format output</li>
    </ul>



