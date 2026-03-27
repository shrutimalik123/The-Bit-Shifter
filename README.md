# 🔢 The Bit-Shifter - Binary Conversion Challenge

A mathematical puzzle game that tests your ability to translate between Decimal (Base-10) and Binary (Base-2). You are tasked with converting a random integer into its 8-bit equivalent. This is the fundamental language of CPU registers, memory addresses, and network protocols.

This project focuses on teaching:
* **Base-2 Number Systems:** Understanding the positional values of bits ($128, 64, 32, 16, 8, 4, 2, 1$).
* **String Padding:** Using `.zfill()` to ensure data fits a standard 8-bit "Byte" format.
* **Radix Conversion:** Using `int(string, 2)` to parse binary strings back into integers for comparison.
* **Input Validation:** Ensuring user data contains only valid bits ($0$ or $1$) and is the correct length.

---

## ✨ Features

* **Dynamic Target Generation:** Supports any number from $1$ to $255$, covering the full range of a single byte.
* **Automatic Padding:** Converts short binary strings into full 8-bit blocks automatically.
* **Intelligent Feedback:** Tells the player if their binary guess is mathematically higher or lower than the target.
* **Score Multiplier:** Rewards faster solving by multiplying remaining attempts by a base score.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `bit_shifter.py`.
2.  **Open Terminal:** Navigate to the folder containing the file.
3.  **Run the Script:**
    ```bash
    python bit_shifter.py
    ```

### 3. Gameplay Instructions
1.  **Observe the Decimal:** The computer provides a target number (e.g., $42$).
2.  **Calculate the Bits:** Determine which powers of 2 add up to that number ($32 + 8 + 2 = 42$).
3.  **Input the Byte:** Enter the 8-bit string ($00101010$).
4.  **Sync Data:** You have 5 attempts before the system locks you out.



---

## 🧠 Code Structure Highlights

### Managing the "0b" Prefix
In Python, the `bin()` function returns a string starting with `0b` to indicate it is binary. We use string slicing `[2:]` to remove those first two characters so we only have the raw bits.

```python
# Turns '0b1010' into '1010'
raw_bits = bin(target_decimal)[2:]

