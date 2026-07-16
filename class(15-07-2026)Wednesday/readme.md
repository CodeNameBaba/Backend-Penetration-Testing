<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:000000,50:1C1C1C,100:e50000&text=Banking%20Architecture&fontAlign=50&fontAlignY=40&fontSize=38&fontColor=ffffff&animation=fadeIn"/>
</p>

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3000&pause=1000&color=e50000&center=true&vCenter=true&width=800&lines=System+Architecture+Guide.;Algorithmic+Breakdown.;Function+Execution+Logic.;Common+Engineering+Pitfalls." />
</p>

---

# 🏦 Core Banking & Modular Execution Guide

Welcome to Wednesday's session. In backend development and penetration testing, understanding how data moves between files and how state is preserved is critical. If you understand how a system is built, you understand how it can be broken.

This repository demonstrates **Modular Execution**. We are splitting our program into distinct tactical components: a database (`users.json`), an engine containing the logic (`main.py`), and the execution router (`bank.py`).

---

## 🧠 System Algorithm

Before looking at the syntax, you must understand the step-by-step logic of the backend application. This is the exact algorithm the banking system follows:

1. **System Initialization:** Open `users.json` in read mode and load the JSON string into a Python Dictionary in memory.
2. **Authentication Route:** Call the `login` function. Prompt the user for credentials.
3. **Validation:** Check if the provided username exists as a key in the database and if the provided password matches the stored password.
4. **Session Hand-off:** If authentication is successful, return the `username` string back to the main executable to represent the active "session".
5. **Transaction Routing:** Pass the database and the active `username` into the `transfer` function.
6. **Integrity Checks:** - Verify the payee exists in the database.
   - Prevent self-transfers (Sender != Payee).
   - Ensure the sender's balance is greater than or equal to the transfer amount.
7. **State Modification:** Deduct the integer amount from the sender's balance and add it to the payee's balance in the active memory dictionary.
8. **Persistence:** Open `users.json` in write mode and dump the modified Python Dictionary back into a JSON file, permanently saving the state.

---

## ⚙️ Function Breakdown & Execution Logic

Here is the exact explanation of every functional block in our repository.

### 📁 `main.py` (The Engine)
This file is treated as a **module**. It contains the business logic but does not execute itself.

* **`login(users)`**
    * *Purpose:* Handles credential verification.
    * *Logic:* It takes the active `users` dictionary as a parameter. It sanitizes the username input using `.lower()`. It uses an `if` statement to check two conditions: does the user exist, and does the password match?
    * *Return:* It only returns the valid `username` string if successful. If it fails, it prints an error and returns `None`.

* **`signUp(users)`**
    * *Purpose:* Registers new entities into the database.
    * *Logic:* Runs a `while True` loop to ensure successful completion. It checks for duplicate keys to prevent overwriting existing accounts. It features password confirmation. Once validated, it maps a new dictionary entry `users[username] = {"password": password}` and immediately executes a `json.dump()` to save the new user to disk.

* **`transfer(users, username)`**
    * *Purpose:* The transactional core that manipulates financial state.
    * *Logic:* It takes the database (`users`) and the currently authenticated actor (`username`). It handles all edge cases via `if/elif/else` blocks (sending to a non-existent user, sending to self, insufficient funds, negative numbers). It performs the mathematical operations on the nested dictionary keys `["balance"]` and finalizes the transaction by writing the updated dictionary back to `users.json`.

### 📁 `bank.py` (The Router / Executable)
This is the entry point of the application. This is the **only** file you should run in your terminal.

* *Logic:* It imports `main.py` using an alias (`import main as asad`). It handles the initial `json.load()` to bring the database into memory. It triggers `asad.login(users)`, captures the returned username in variable `x`, and then pipes that authenticated user directly into `asad.transfer(users, x)`.

---

## 📖 Comprehensive Syntax Guide

To succeed in this module, you must master the following Python concepts:

### 1. Cross-Module Imports
You don't want all your code in one massive file. We use imports to borrow logic from other files.

```python
# Inside bank.py
import main as asad

# We use the 'as' keyword to create an alias. 
# Now, any function inside main.py can be called using 'asad'.
x = asad.login(users)