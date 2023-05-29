import json
from jinja2 import Environment, FileSystemLoader, select_autoescape


def generate_setting_page():
    config = read_json_config("permalinks.json")
    setting_page_template = get_settings_page_template()

    setting_html = setting_page_template.render(config)

    save_setting_page(setting_html)


def read_json_config(path):
    with open(path, "r") as config_file:
        return json.load(config_file)


def get_settings_page_template():
    template_env = Environment(
        loader=FileSystemLoader(searchpath="./templates"),
        autoescape=select_autoescape(),
    )
    return template_env.get_template("settings_string.template.html")

def save_setting_page(content):
    with open("page/index.html", "w") as setting_page:
        setting_page.write(content)

if __name__ == "__main__":
    generate_setting_page()
