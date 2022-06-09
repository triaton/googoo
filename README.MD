# Googoo - Google Search CLI Tool using [SerpApi](https://serpapi.com/)

## Overview
Googoo is a Google Search CLI(Command Line Interface) can be used in Windows cmd or in linux shell environment. There is a similar tool called [googler](https://github.com/jarun/googler) which does the same thing. It trys to scrap google search page and extract useful information there and it works well. But it has a very important issue when using. Google is so intelligent that it can easily detect it and it regards the googler machine as a bot and it asks for reCaptcha which googler can't bypass itself.

By the help or SerpApi, we can have a tool without this limitation. Googoo is built on top of SerpApi and SerpApi does everything behind the hood.

SerpApi has a free plan that allows 100 requests per month. You can buy your subscription and increase the request limit.
## Requirements

- python
- pip

## Environment Variable
Please sign up on https://serpapi.com/ and you can find your API key from https://serpapi.com/manage-api-key.

Set environment variable `SERP_API_KEY`.

```bash
$ export SERP_API_KEY=2e35def6...
```

## Installation
```bash
$ pip install -r requirements.txt
```

## Usage

```bash
$ python3 googoo.py "search phrase here"
```
