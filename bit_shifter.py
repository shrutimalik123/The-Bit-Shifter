import random

def bit_shifter():
    # 1. Game Setup
    # Generate a random number between 1 and 255 (fits in 8 bits)
    target_decimal = random.randint(1, 255)
    
    # Calculate the correct binary answer (stripped of '0b' prefix and padded to 8 bits)
    correct_binary = bin(target_decimal)[2:].zfill(8)
    
    attempts = 5
    score = 0

    print("--- 🔢 THE BIT-SHIFTER 🔢 ---")
    print(f"Target Decimal: {target_decimal}")
    print("Convert this number into an 8-bit Binary string (e.g., 00101010).")
    print("Hint: Each position represents: 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1")

    # 2. Game Loop
    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        guess = input("Binary Input: ").strip()

        # 3. Validation
        if len(guess) != 8 or not all(bit in '01' for bit in guess):
            print("⚠️ INVALID FORMAT: Must be exactly 8 bits (only 0s and 1s).")
            continue

        if guess == correct_binary:
            print(f"✅ POSITIVE LINK! {guess} is {target_decimal} in binary.")
            score = attempts * 10
            break
        else:
            attempts -= 1
            # Provide a specific hint based on the guess
            guess_decimal = int(guess, 2)
            if guess_decimal < target_decimal:
                print("📉 TOO LOW: Your binary value is under the target.")
            else:
                print("📈 TOO HIGH: Your binary value is over the target.")

    # 4. End State
    if guess == correct_binary:
        print(f"\n🎊 DATA SYNC COMPLETE! Final Score: {score}")
    else:
        print(f"\n💀 CRITICAL ERROR: System lock. The correct bits were {correct_binary}.")

bit_shifter()
