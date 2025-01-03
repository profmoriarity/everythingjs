
# EverythingJS

## Overview

**EverythingJS** is a versatile CLI tool designed to extract JavaScript links from URLs or web pages, apply custom regex patterns to these files, and organize the results in a structured, easy-to-use JSON format. It is built for efficiency, with multi-threading support, the ability to filter irrelevant links, and customizable HTTP headers for requests. The tool also provides flexibility in saving results, whether in a JSON file, a database, or by monitoring JS files for changes.

<img width="1424" alt="image" src="https://github.com/user-attachments/assets/928554d4-5649-4ae2-a861-0bafae4a7db3" />


## Installation

Install EverythingJS via pip:

```bash
pip install everythingjs
```

## Features

- Extract JavaScript links from a URL or a list of URLs using the `-i` flag.
- Automatically convert relative links into absolute URLs.
- Apply user-defined regex patterns to extract relevant matches from each JavaScript file with the `-s` flag.
- Filter out unwanted JS links using a predefined "nopelist" file.
- Add custom headers for HTTP requests using the `-H` flag to handle server configurations or bypass restrictions.
- Structure the results in a clean JSON format, categorizing JavaScript links and their associated regex matches, with the `-o` flag to save them.
- Speed up processing by running tasks concurrently for multiple URLs using multi-threading.
- Save the extracted JavaScript links and matches to a JSON file or database using the `-o` or `-store` flags.
- Launch a simple web server to view and navigate through the extracted results using the `-f` flag.
- Send updates on the process to a Slack channel via a webhook with the `-slack` flag.
- Optionally save the JavaScript files locally for further analysis using the `-sjs` flag.
- Monitor JS files for changes and trigger actions like Slack notifications or updates to the database using the `-m` flag.


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
#### WEB UI showing api endpoints, secrets, links, dom sinks, JS search.
<img width="1321" alt="image" src="https://github.com/user-attachments/assets/afa5b993-ccbf-476a-af98-ce5290bddd02" />

#### search through the beautified JS files (works only if -sjs is used when running command)
<img width="1318" alt="image" src="https://github.com/user-attachments/assets/59e59ae1-273b-4ef8-920e-dfe4f7c6a653" />


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


## Credits
- Borrowed templates from ProjectDiscovery nuclei templates (to all those who contributed to them)
- @GerbenJavado for inspring with Linkfinder and Regex expressions

## License

MIT License
