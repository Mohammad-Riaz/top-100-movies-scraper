# 🎬 Top 100 Movies Scraper

This project uses Python, Requests, and BeautifulSoup to scrape Empire Online's list of the 100 Greatest Movies and save the results into a text file.

The program retrieves the webpage, extracts all movie titles, reverses the order so the rankings are displayed correctly, and stores them in a local file called `movies.txt`.

## 🚀 Features

* Fetches webpage content using Requests
* Parses HTML using BeautifulSoup
* Extracts movie titles automatically
* Saves results to a text file
* Uses UTF-8 encoding to support special characters

## 🧠 How It Works

1. Send a GET request to the archived Empire Online webpage.
2. Parse the HTML using BeautifulSoup.
3. Find all movie title elements.
4. Extract the text from each title.
5. Reverse the list to display rankings correctly.
6. Write all movie titles to `movies.txt`.

## 📦 Technologies Used

* Python
* Requests
* BeautifulSoup4

## ⚙️ Installation

Install the required packages:

```bash
pip install requests beautifulsoup4
```

## ▶️ Run

```bash
python main.py
```

After running, a file named `movies.txt` will be created containing all 100 movie titles.

## 📁 Project Structure

```text
├── main.py
├── movies.txt
└── README.md
```

## 🎯 What I Learned

* Making HTTP requests with Requests
* Parsing HTML with BeautifulSoup
* Extracting data from webpages
* Working with lists and file handling
* Handling Unicode text with UTF-8 encoding

## 📜 Disclaimer

This project is for educational purposes and uses an archived version of the Empire Online webpage.
