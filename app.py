import requests
import csv
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

# Dirección de la página web
url = "http://quotes.toscrape.com/"

# Ejecutar GET-Request
response = requests.get(url)

# Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')

# Extraer todas las citas y autores del archivo HTML
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")

# Crear una lista de las citas y autores
quotes_and_authors = list()
for quote, author in zip(quotes_html, authors_html):
    quotes_and_authors.append((quote.text, author.text))

# Ruta principal de la aplicación web
@app.route('/')
def index():
    # Renderizar la plantilla HTML 'index.html' y pasar las citas y autores como argumentos
    return render_template('index.html', quotes_and_authors=quotes_and_authors)

if __name__ == '__main__':
    # Ejecutar la aplicación Flask en el puerto definido por la variable de entorno 'PORT'
    # port = int(os.environ.get("PORT", 3000))
    app.run(debug=True, port=8080, host="0.0.0.0")

