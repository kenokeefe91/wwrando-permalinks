Wind waker randomizer Settings String inventory
---

This project is a simple web page automatically generated and uploaded on the following gh page : https://kenokeefe91.github.io/wwrando-permalinks/

## Setup 

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Generate the setting page

```bash
source .venv/bin/activate
python generate_page.py
```

Running this command you will have a build directory generated with an index.html page in it.

## Contribute

To add a setting string simply add it to `data.json` file open a PR and once validated the github action will update the page
