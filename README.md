# Essay-Generator

## What it Does

- The project Essay-Generator will generate essay and save it to a .txt file.
- This project also supports audio playback.

## How it Works

This project is based on Web Scrapping which will fetch the information by using Selenium and find the content by using the id and tag_name of webpage(html).

## Setup

- Install webdriver of your browser and paste it in your python directory. Download link below. 
- For Chrome [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
- For Firefox [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
- Disable Pylint.

## Modules to be Installed
* Install Pyaudio:
```
  pip install pyaudio
```
## NOTE 
- If the above command doesn't work for installation of pyaudio(you have to do it manually)
- Go to [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- And choose any version and execute the command in cmd by
- For example
```
  pip install PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl
```

## MODULES USED

* Install selenium:

```
  pip install selenium

```
* Install playsound.
 
 ```
  pip install playsound
 
 ```
* Install playsound.
 
 ```
  pip install PyQt5
 
 ```

* Install gtts:
 ```
  pip install gTTS

  ```


## Run the Application

From the main directory:

## Step 1
- Enter the topic of the Essay
## Step 2
- Choose the browser 
## Step 3
- Click "GENERATE" to begin the process.

## NOTE
- The PyQt5 GUI may show the message not responding and will freeze the GUI, please don't exit the program. It will be responsive again when the process will get executed.
- This project also have audio playback which will play the audio file after the .txt file get saved.
- The gTTS conversion all depends on the Internet Connection, faster the connection, faster will be the conversion.
- Please note that the PyQt basically works like a Queue which means process get executed one-by-one. It basically requires the knowledge of "Threading", which is very complex to implement. So, please cooperate with app, it'll do its' work.
- If you see message on the console or cmd like "gtts.tts.gTTSError: 500 (Internal Server Error) from TTS API. Probable cause: Uptream API error. Try again later." then please close the terminal or cmd. Because if from client side so much Google API requests are made then Google automatically blocked you (temporarily).
- Source [https://github.com/pndurette/gTTS/issues/114](https://github.com/pndurette/gTTS/issues/114)
