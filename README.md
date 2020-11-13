# Google Calendar event CLI

Google Calendar event CLI is command-line tool which allows you to create Google Calendar events in natural language from your CLI.

### Tech

Google Calendar event CLI is based on Dialogflow.

* [DialogFlow](https://cloud.google.com/dialogflow) - Dialogflow is a natural language understanding platform used to design and integrate a conversational user interface into mobile apps, web applications, devices, bots, interactive voice response systems, and so on.
* [Flask](https://flask.palletsprojects.com/) - Flask is a lightweight WSGI web application framework.
* [PythonAnywhere](https://www.pythonanywhere.com/) - Thanks to PythonAnywhere for the free hosting.

![Sequence Diagram](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/efcc8cf1-d73a-4426-9c0d-9339b46fa180/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201113T100315Z&X-Amz-Expires=86400&X-Amz-Signature=953d51d41c15cbe2cb67ad21a27a6251d4d1d7a1171db03f6ba5e794bc69b61a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

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
