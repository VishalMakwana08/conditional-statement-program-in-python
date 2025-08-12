import msvcrt

# Hardcoded password
correct_password = "Python123"

# Maximum attempts allowed
max_attempts = 3

def get_password(prompt="Password: "):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        ch = msvcrt.getch()
        if ch in {b"\r", b"\n"}:  # Enter key
            print()
            break
        elif ch == b"\x08":  # Backspace
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        elif ch == b"\x03":  # Ctrl+C
            raise KeyboardInterrupt
        else:
            password += ch.decode("utf-8", errors="ignore")
            print("*", end="", flush=True)
    return password

# Main login loop
for attempt in range(1, max_attempts + 1):
    entered_password = get_password(f"Attempt {attempt}/{max_attempts} - Enter password: ")

    if entered_password == correct_password:
        print("Access Granted")
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Access Denied  | {remaining} attempt(s) left.")
        else:
            print("Too many failed attempts. Account locked")
