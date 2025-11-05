import json
import random
import datetime
import os
import pyttsx3

QUOTES_FILE = "quotes.json"
HISTORY_FILE = "history.txt"

# Load quotes
def load_quotes():
    if not os.path.exists(QUOTES_FILE):
        # Default quotes
        quotes = [
            "Believe in yourself and all that you are.",
            "Success is the sum of small efforts repeated daily.",
            "Your limitation—it’s only your imagination.",
            "Push yourself, because no one else will do it for you.",
            "Great things never come from comfort zones."
        ]
        with open(QUOTES_FILE, "w") as f:
            json.dump(quotes, f, indent=4)
    else:
        with open(QUOTES_FILE, "r") as f:
            quotes = json.load(f)
    return quotes

# Save new quote
def add_quote(new_quote):
    quotes = load_quotes()
    quotes.append(new_quote)
    with open(QUOTES_FILE, "w") as f:
        json.dump(quotes, f, indent=4)
    print(f"✅ Added new quote: {new_quote}")

# Show random quote
def show_quote():
    quotes = load_quotes()
    quote = random.choice(quotes)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n🌞 Motivational Quote:\n\"{quote}\"\n")
    
    # Save to history
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{now} - {quote}\n")
    return quote

# Speak quote aloud
def speak_quote(quote):
    engine = pyttsx3.init()
    engine.say(quote)
    engine.runAndWait()

# Show history
def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("📭 No history yet!")
    else:
        print("\n📝 Quote History:")
        with open(HISTORY_FILE, "r") as f:
            for line in f:
                print(line.strip())

# --- Main Program --
def main():
    while True:
        print("\n--- 🌞 Daily Motivation CLI App ---")
        print("1. Show random quote")
        print("2. Add new quote")
        print("3. Show history")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            quote = show_quote()
            speak = input("🔊 Do you want me to speak it? (y/n): ").lower()
            if speak == "y":
                speak_quote(quote)

        elif choice == "2":
            new_quote = input("Enter your motivational quote: ")
            add_quote(new_quote)

        elif choice == "3":
            show_history()

        elif choice == "4":
            print("👋 Stay motivated! Goodbye.")
            break
        else:
            print("❌ Invalid option. Try again!")

if __name__ == "__main__":
    main()

