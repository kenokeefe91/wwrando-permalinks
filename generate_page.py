import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from urllib import parse


def generate_setting_page():
    config = read_json_config("permalinks.json")
    setting_page_template = get_settings_page_template()

    page_data = generate_page_data_from(config)

    setting_html = setting_page_template.render(page_data)

    save_setting_page(setting_html)


def generate_page_data_from(config):
    page_data = {"rando_version": config["rando_version"], "settings": []}

    for setting in config["settings"]:
        if setting.get("is_coop"):
            tracker_url = "https://jaysc.github.io/tww-rando-tracker-coop"
        else:
            tracker_url = f"https://www.wooferzfg.me/tww-rando-tracker/#/tracker/new/{parse.quote(setting['permalink'], safe='')}"

        page_data["settings"].append(
            {
                "name": setting["name"],
                "permalink": setting["permalink"],
                "tracker_link": tracker_url,
            }
        )

    return page_data


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
