Wind Waker Randomizer Settings String Inventory
---

This project is a simple web page that displays a list of settings for [The Wind Waker Randomizer](https://github.com/LagoLunatic/wwrando) races. The site is hosted at: https://kenokeefe91.github.io/wwrando-permalinks/

## Setup 

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Generate the settings page

```bash
source .venv/bin/activate
python generate_page.py
```

After running this command, you will have a build directory generated with an `index.html` page in it.

## Contribute

To add a settings permalink, simply add it to the `permalinks.json` file and open a pull request. Once validated, the GitHub action will automatically update the site.
