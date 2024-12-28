
# EverythingJS

## Overview

**EverythingJS** is a CLI tool for extracting JavaScript links from URLs or web pages, applying custom regex patterns to those JS files, and organizing the results in a structured JSON format. It’s designed for efficiency, with features like multi-threading, filtering irrelevant links, and customizable headers.

## Installation

Install EverythingJS via pip:

```bash
pip install everythingjs
```

## Features

- Extracts JavaScript links from a URL or a list of URLs.
- Converts relative links to absolute URLs.
- Applies a regex pattern to each JavaScript file, extracting relevant matches.
- Filters irrelevant JavaScript links using a predefined `nopelist`.
- Supports custom headers for HTTP requests.
- Outputs results in JSON format, tagged to respective JS links.
- Multi-threaded for fast processing.

## Usage

### Command-Line Arguments

```
usage: everythingjs [-h] [-i INPUT] [-db] [-f SERVER] [-o OUTPUT] [-v] [-H HEADER] [-s SECRETS_FILE] [-sjs SAVE_JS] [-store] [-m MONITOR] [-slack SLACK_WEBHOOK] [-j] [-silent]

Extract JS links from a URL or a list of URLs

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        URL or file containing URLs
  -db, --from_db        consume input from db, past results
  -f SERVER, --server SERVER
                        Provide output to launch web server
  -o OUTPUT, --output OUTPUT
                        Output JSON file to save results (optional, prints to CLI if not specified)
  -v, --verbose         Enable verbose logging
  -H HEADER, --header HEADER
                        Add custom header (can be used multiple times)
  -s SECRETS_FILE, --secrets_file SECRETS_FILE
                        Add your secrets.regex file containing compatible secrets file
  -sjs SAVE_JS, --save_js SAVE_JS
                        Save JS files to specific location.
  -store, --save_db     Save contents to database in ~/.everythingjs/scan_results.db
  -m MONITOR, --monitor MONITOR
                        Monitor the process at specified intervals (e.g., 2s, 2m, 1d, 4w)
  -slack SLACK_WEBHOOK, --slack_webhook SLACK_WEBHOOK
                        Pass the slack webhook url where you want to post the message updates
  -j, --jsonl           print output in jsonl format in stdout
  -silent, --silent     dont print anything except output
```

### Example Usage

#### 1. Extract JavaScript links from a single URL:

```bash
everythingjs -i https://example.com
```

#### 2. Extract JavaScript links from a file of URLs:

```bash
everythingjs -i urls.txt
```

#### 3. Save the output to a JSON file:

```bash
everythingjs -i https://example.com -o results.json
```

#### 4. Enable verbose logging:

```bash
everythingjs -i https://example.com -v
```

#### 5. Add custom headers:

```bash
everythingjs -i https://example.com -H "User-Agent: CustomAgent" -H "Authorization: Bearer TOKEN"
```

#### 6. Save beautified javascript to a local directory:

```bash
everythingjs -i urls.txt -sjs ./saved_js
```

#### 7. Launch a web server to navigate through results using a web ui (after generating output.json)
```bash
everythingjs -f output.json
```

#### 8. Monitoring JS files for changes on a given input and send udpates to slack
```bash
everythingjs -i https://example.com -slack https://hooks.slack.com/services/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
```

#### 9. Monitor JS files on all domains saved in DB and send updates to slack
```bash
everythingjs -db -slack https://hooks.slack.com/services/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
```


#### 10. Monitor JS files on all domains saved in DB and print jsonl output
```bash
everythingjs -db jsonl
```



## Output

- Outputs JSON in the format:

```json
{
  "https://example.com": {
    "js_links": [
      "https://example.com/static/script1.js",
      "https://example.com/static/script2.js"
    ],
    "regex_matches": {
      "https://example.com/static/script1.js": ["match1", "match2"],
      "https://example.com/static/script2.js": ["match3"]
    }
  }
}
```
- Domains without JavaScript links are excluded from the output.

## License

MIT License
