<h1>Simple Banking System</h1>

<p>This Python script provides a basic banking system simulation where users can deposit, withdraw, and check their balance.</p>

<h2>Menu Options</h2>
<p>The following options are available in the menu:</p>
<pre>
    [1] Deposit
    [2] Withdraw
    [3] Check Balance
    [4] Quit
</pre>

<h2>Usage</h2>
<ol>
    <li>Run the script.</li>
    <li>Choose an option from the menu by entering the corresponding number.</li>
    <li>Follow the prompts to complete the selected action.</li>
</ol>

<h2>Features</h2>
<ul>
    <li><strong>Deposit:</strong> Allows users to deposit money into their account.</li>
    <li><strong>Withdraw:</strong> Permits users to withdraw money from their account, with a withdrawal limit and a balance check.</li>
    <li><strong>Check Balance:</strong> Displays the current account balance and transaction history.</li>
    <li><strong>Quit:</strong> Exits the program.</li>
</ul>

<h2>Usage Notes</h2>
<ul>
    <li>Users can make up to three withdrawals within the specified withdrawal limit.</li>
    <li>The withdrawal amount cannot exceed the preset limit.</li>
    <li>The balance cannot go below zero.</li>
</ul>

<h2>Example</h2>
<pre>
    [1] Deposit
    [2] Withdraw
    [3] Check Balance
    [4] Quit
    Choose an option: 1
    Insert the amount to deposit: 100
    Your balance is 100

    [1] Deposit
    [2] Withdraw
    [3] Check Balance
    [4] Quit
    Choose an option: 2
    Insert the amount to withdraw: 50
    Withdrawn done with success. Your balance is 50

    [1] Deposit
    [2] Withdraw
    [3] Check Balance
    [4] Quit
    Choose an option: 3
    Your balance now is: 50
    Operations:
    Withdrawn value: 50
    Balance at the time: 50

    [1] Deposit
    [2] Withdraw
    [3] Check Balance
    [4] Quit
    Choose an option: 4
    Au revoir, muchacho!
</pre>

<h2>Author</h2>
<p>Created by Kauana Tombolato to learn the basics of Python.</p>

