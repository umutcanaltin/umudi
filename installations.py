import os
from airium import Airium
html_generator = Airium()

def initialize_html():
    html_generator('<!DOCTYPE html>')
    with html_generator.html():
        with html_generator.head():
            html_generator.meta(charset="utf-8")
            html_generator.meta(name="viewport",content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no")
            html_generator.title(_t="umudi blank page")
            html_generator.link(rel="stylesheet", href="css/fontawesome/fontawesome-all.css")
            html_generator.link(rel="stylesheet", href="css/fontawesome/fontawesome-brands.css")
            html_generator.link(rel="stylesheet", href="css/main.css")


    html = str(html_generator)
    print(html)



def check_ts_version():
    version_var = os.system("tsc -v")
    print(version_var)


def create_blank_page():
    return 0


initialize_html()