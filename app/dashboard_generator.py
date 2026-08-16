from jinja2 import Template


def generate_dashboard(data):

    with open(
        "templates/dashboard_template.html",
        "r"
    ) as file:

        template = Template(file.read())


    html = template.render(
        incident=data
    )


    with open(
        "reports/dashboard_INC-001.html",
        "w"
    ) as file:

        file.write(html)


    print("Dashboard Generated Successfully")