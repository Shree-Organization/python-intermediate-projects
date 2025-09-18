# 🌞 Daily Motivation CLI App

A Python command-line tool that delivers motivational quotes to brighten your day.
Stay inspired with random quotes, add your own, track your history, and even listen with text-to-speech 🎙️.

## ✨ Features

✅ Random Motivational Quote – Get a fresh quote every time.

✅ Add Your Own Quotes – Personalize your motivation.

✅ History Tracking – See all past quotes with timestamps.

✅ Voice Output – Uses pyttsx3 to read quotes aloud.

✅ Persistent Storage – Quotes are saved in a JSON file.

## 🛠️ Tech Stack

Language: Python 3

Libraries:

json (store quotes)

random (pick quotes)

datetime (timestamps)

os (file handling)

pyttsx3 (text-to-speech)

## ⚡ Installation

Clone the repo:
```
git clone https://github.com/your-username/daily-motivation-cli.git
cd daily-motivation-cli
```

Install dependencies:
```
pip install pyttsx3
```

Run the program:
```
python motivation.py
```

## 📖 Usage

Once started, you’ll see the menu:
```
--- 🌞 Daily Motivation CLI App ---
1. Show random quote
2. Add new quote
3. Show history
4. Exit
```

👉 Example:
```
Enter choice: 1

🌞 Motivational Quote:
"Success is the sum of small efforts repeated daily."

🔊 Do you want me to speak it? (y/n): y
```
## 📂 Project Structure
```
daily-motivation-cli/
│── motivation.py       # Main program
│── quotes.json         # Stores quotes
│── history.txt         # Logs shown quotes with timestamps
│── README.md           # Documentation
```

📝 Sample History
```
2025-09-18 09:42:21 - Believe in yourself and all that you are.
2025-09-18 10:15:09 - Push yourself, because no one else will do it for you.
```

## 🚀 Future Enhancements

🔹 Add categories (Success, Focus, Positivity, etc.)

🔹 Daily quote notifications (via cron or task scheduler)

🔹 Export history to CSV/Excel

🔹 Create a GUI version (Tkinter/PyQt)

🔹 Build a mobile app version

## 👨‍💻 Author

Crafted with ✨ by Mantra Patil – *because motivation should always be just one command away!*
