from flask import Flask, render_template
from bs4 import BeautifulSoup
import csv
import logging
import os
import requests
i  # Imports

# Flask application
app = Flask(__name__, template_folder='.')

# URL of the web page
url = "http://quotes.toscrape.com/"

# Execute GET-Request
response = requests.get(url)
logging.info("GET-Request was successful")

# Parse the HTML file of BeautifulSoup from the source text
html = BeautifulSoup(response.text, 'html.parser')

# Extract all the quotes and authors from the HTML file
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")

# Create a list of the quotes and authors
quotes_and_authors = list()
for quote, author in zip(quotes_html, authors_html):
    quotes_and_authors.append((quote.text, author.text))

# Main route of the web application


@app.route('/')
def index():
    # Render the HTML template 'index.html' and pass the quotes and authors as arguments
    return render_template('index.html', quotes_and_authors=quotes_and_authors)


if __name__ == '__main__':
    # Execute the Flask application on the port defined by the environment variable 'PORT'
    # port = int(os.environ.get("PORT", 3000))
    # Get the port number from the environment variable PORT
    port = int(os.getenv('PORT', 8080))

    # Print the port number
    print("Starting app on port %d" % port)

    # Run the app on the port number
    app.run(debug=True, port=port, host="
