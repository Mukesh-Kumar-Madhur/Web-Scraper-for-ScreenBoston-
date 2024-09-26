## import all required libraries
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import os.path
from IPython.core.display import HTML
from IPython import display



# Define the URL and file path and load html data
url = 'https://screenboston.com'
file_path = 'data/html/screenboston.html'

# Check if the file already exists
if not os.path.isfile(file_path):
    # Make the HTTP request
    response = requests.get(url)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the HTML content to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)
    
    print(f"HTML content saved to {file_path}")
else:
    print(f"File {file_path} already exists. Skipping download.")


## Logic to scrap the data from html file
# Load the HTML file
with open("data/html/screenboston.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Initialize list to store movie details
movies = []

# Find all movie elements (each movie inside a <button> tag)
movie_elements = soup.find_all('button')

# Loop through each movie element and extract details
for movie in movie_elements:
    try:
        # Extract title (inside <p> tag with class "big")
        title_element = movie.find("p", class_="big")
        title = title_element.get_text(strip=True) if title_element else "Unknown Title"
        # print(f"Title: {title}")  # fixed


        # Extract directors (assumed to be the first <p> in the second <div> under <button>)
        directors_element = movie.find_all("div")[8].find("p")
        directors = directors_element.get_text(strip=True) if directors_element else "Unknown Directors"
        # print(f"Directors: {directors}")  # fixed

        # Extract year, genre, runtime (in the second <p> in the same <div>)
        details_element = movie.find_all("p")[-3]   
        details_text = details_element.get_text(strip=True).split(", ") if details_element else []
        year = details_text[0] if len(details_text) > 0 and details_text[0].isdigit() else "Unknown"
        genre = details_text[1] if len(details_text) > 1 else "Unknown"
        runtime = details_text[2] if len(details_text) > 2 else "Unknown"
        # print("year: ", year, "genre: ", genre, "runtime: ", runtime)  ## fixed

        # Extract theater (assumed to be in the second <div> under <button>, next <p>)
        theater_element = movie.find_all("p")[-2]
        theater = theater_element.get_text(strip=True) if theater_element else "Unknown Theater"
        # print("Theater: ", theater)  #fixed

        # Extract screening date (from the previous sibling <div> with class "uppercase")
        screen_date_element = movie.find_previous("div", class_="uppercase")
        screen_date = screen_date_element.get_text(strip=True) if screen_date_element else "Unknown Date"
        # print("Screen_date: ", screen_date)  # Fixed

        # Extract screening times (last <p> under the second <div>)
        screen_times_element = movie.find_all("p")[-1]
        screen_times = screen_times_element.get_text(strip=True) if screen_times_element else "Unknown Times"
        # print("Screen_time: ", screen_times)  #fixed

        # Build movie dictionary
        movie_dict = {
            "title": title,
            "directors": directors,
            "year": year,
            "genre": genre,
            "runtime": runtime,
            "theater": theater,
            "screen_date": screen_date,
            "screen_times": screen_times
        }

        # Append movie dictionary to the list
        movies.append(movie_dict)

    except Exception as e:
        print(f"Error processing movie: {e}")

# Display an example dictionary
if movies:
    print("Total Count of Movies = ,", len(movies))
    # for movie in movies: 
    #     print(movie)
else:
    print("\nNo movies were found.")

