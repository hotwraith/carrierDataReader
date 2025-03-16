# Elite: Dangerous journal data reader for carriers
Small tool that allows users to check the last journal recorded data for their carrier(s) for the game Elite: Dangerous.

## Contents
- [Elite: Dangerous journal data reader for carriers](#elite-dangerous-journal-data-reader-for-carriers)
    - [Contents](#contents)
    - [Getting started](#getting-started)
        - [.exe version](#exe-version)
        - [Python version](#python-version)
    - [Limitations & bugs](#limitations--bugs)

## Getting started

### .exe version

- Download the .exe file from the latest release
- Put the .exe in a (preferabily) dedicated folder
- Double click the .exe
- Add your carriers (ID + shortname) /!\ The search depends on the ID only
- Let the script scrap the info from your journals and keep what's interesting !

### Python version

Requires [Python 3.x](https://www.python.org/downloads/)
- Download the source code from the latest release
- Extract and put the .py file in a (preferabily) dedicated folder
- Double click the .py
- Add your carriers (ID + shortname) /!\ The search depends on the ID only
- Let the script scrap the info from your journals and keep what's interesting !

## Limitations & bugs

- The script can only read journals from the current or past sessions, i.e. it is unable to know the info about your carrier state if you're not in game or haven't been recently.
- E:D journals are specific to each machine you're playing on, if you last played on another computer/device you might notice some difference with reality.
- This works only on Windows atm