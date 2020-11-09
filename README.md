# Google Calendar event CLI

Google Calendar event CLI is command-line tool which allows you to create Google Calendar events in natural language from your CLI.

### Tech

Google Calendar event CLI is based on Dialogflow.

* [DialogFlow](https://cloud.google.com/dialogflow) - Dialogflow is a natural language understanding platform used to design and integrate a conversational user interface into mobile apps, web applications, devices, bots, interactive voice response systems, and so on.
* [Flask](https://flask.palletsprojects.com/) - Flask is a lightweight WSGI web application framework.
* [PythonAnywhere](https://www.pythonanywhere.com/) - Thanks to PythonAnywhere for the free hosting.

### Installation

Download the archive and extract it in a folder of your choice.
Then install the requirements
```sh
$ pip install -r requirements.txt
```

### Usage

```sh
$ python gcal-event-cli <your query>
```
This tool provides it's best use when used in combo with command line launchers like [Listary (Windows)](https://www.listary.com/), [Wox (Windows)](http://www.wox.one/), [Alfred (MacOS)](https://www.alfredapp.com/).

License
----

MIT
