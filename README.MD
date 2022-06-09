# Googoo - Google Search CLI Tool using [SerpApi](https://serpapi.com/)

## Overview
Googoo is a Google Search CLI(Command Line Interface) can be used in window cmd and linux shell environment. There is a similar tool called [googler](https://github.com/jarun/googler) which does the same thing. It trys to scrap google search page and extract useful information there and it works well. But it has a very important issue when using. Google is so intelligent that it can easily detect it and it regards the googler machine as a bot and it asks for reCaptcha which googler can't bypass itself.

By the help or SerpApi, we can have a tool without this limitation. Googoo is built on top of SerpApi and SerpApi does everything behind the hood.

## Requirements

- python
- pip

## Installation
```bash
$ pip install -r requirements.txt
```

## Usage

```bash
$ python3 googoo.py "search phrase here"
```
