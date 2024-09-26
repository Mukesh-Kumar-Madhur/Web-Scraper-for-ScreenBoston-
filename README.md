### **Project Folder Structure**
Organize  project folder as follows:
```
web-scraper-screenboston/
│
├── data/                     # Directory to store the scraped HTML data
│   └── html/
│       └── screenboston.html
│
├── web_scraper_screenboston.py  # Main Python script for web scraping
│
├── README.md                  # Documentation file 
│
└── screenshots/               # Directory for screenshots
    └── code_screenshot.png    # Code snippet screenshot
    └── result_screenshot.png  # Result screenshot (movie details)
```

```markdown
# Web Scraper for ScreenBoston 🎬

This Python project uses **BeautifulSoup** to scrape movie details from [ScreenBoston](https://screenboston.com). It collects information such as the movie title, director, genre, runtime, screening date, and theater information.

## 🔧 Technologies Used
- **Python**
- **BeautifulSoup**
- **Requests**
- **File Handling** for HTML storage

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Mukesh-Kumar-Madhur/web-scraper-screenboston.git
   ```
2. Navigate to the project directory:
   ```bash
   cd web-scraper-screenboston
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the scraper:
   ```bash
   python web_scraper_screenboston.py
   ```
5. The scraped HTML will be saved in the `data/html/` directory, and movie details will be printed to the console.

## 📁 File Structure
- `web_scraper_screenboston.py`: Python script for web scraping
- `data/html/screenboston.html`: Stored HTML file from ScreenBoston
- `screenshots/`: Screenshots of the code and results

## ✨ Features
- Automatically saves HTML to a local file
- Extracts movie details: title, directors, year, genre, runtime, theater, screening date, and times
- Handles errors and missing data gracefully

---

**Author:** Mukesh Kumar(https://www.linkedin.com/in/mukesh-kumar-6908a5325)
