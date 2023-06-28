import requests
import json
from flask import Flask

text = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").text

currencies = json.loads(text)

for currency in currencies['Valute']:
     print(currency)

     from flask import Flask

     app = Flask(__name__)


     @app.route("/")
     def hello() -> str:
         ext = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").text
         currencies = json.loads(text)
         result = ''
         for currency in currencies['Valute']:
            result += str(currency) + '<br>'
         return result


     if __name__ == "__main__":
         app.run()