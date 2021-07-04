from profil3r.core.colors import Colors
import json
import os
from jinja2 import Template
import datetime
import csv

# Generate a report in JSON format containing the collected data
# Report will be in "./reports/json"
# You can modify th path in the config.json file
def generate_json_report(self):
    # Create ./reports/json directory if not exists
    if not os.path.exists('reports/json'):
        os.makedirs('reports/json')

    separators = [value for key, value in self.CONFIG["separators"].items()]

    file_name = self.CONFIG["json_report_path"].format("_".join([item for item in self.items if item not in separators]))
    try:
        with open(file_name, 'w') as fp:
            json.dump(self.result, fp, indent=2)
    except Exception as e:
        print(e)

    print("\n" + Colors.BOLD + "[+] " + Colors.ENDC + "JSON report was generated in {}".format(file_name))

# Generate a report in HTML format containing the collected data
# Report will be in "./reports/html"
# You can modify th path in the config.json file
def generate_HTML_report(self):
    # Create ./reports/html directory if not exists
    if not os.path.exists('reports/html'):
        os.makedirs('reports/html')

    separators = [value for key, value in self.CONFIG["separators"].items()]

    dirname = os.path.dirname(__file__)
    html_content = open(os.path.join(dirname, './ressources/report.tpl')).read()
    css_content = open(os.path.join(dirname, './ressources/report.css')).read()
    js_content = open(os.path.join(dirname, './ressources/report.js')).read()

    html_report = Template(html_content).render(
        title = " ".join(self.items),
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        version = self.version,
        results = self.result.items(),
        style = css_content,
        script = js_content
    )

    file_name = self.CONFIG["html_report_path"].format("_".join([item for item in self.items if item not in separators]))
    try:
        with open(file_name, 'w') as fp:
            fp.write(html_report)
    except Exception as e:
        print(e)

    print(Colors.BOLD + "[+] " + Colors.ENDC + "HTML report was generated in {}".format(file_name))

# Generate a report in CSV format containing the collected data
# Report will be in "./reports/csv"
# You can modify th path in the config.json file
def generate_csv_report(self):
    # Create ./reports/csv directory if not exists
    if not os.path.exists('reports/csv'):
        os.makedirs('reports/csv')

    separators = [value for key, value in self.CONFIG["separators"].items()]

    file_name = self.CONFIG["csv_report_path"].format("_".join([item for item in self.items if item not in separators]))
    try:
        with open(file_name, 'w', newline='') as fp:
            writer = csv.writer(fp)
            # columns titles
            writer.writerow(["service", "category", "profile", "breached"])

            for service, result in self.result.items():
                result_service = service
                result_type = result["type"]
                for account in result["accounts"]:
                    result_value = account["value"]
                    result_breached = account["breached"] if result_type == "email" else False 
                    # row values
                    writer.writerow([result_service, result_type, result_value, result_breached])

    except Exception as e:
        print(e)

    print(Colors.BOLD + "[+] " + Colors.ENDC + "CSV report was generated in {}".format(file_name))

def generate_report(self):
    # Create ./reports directory if not exists
    if not os.path.exists('reports'):
        os.makedirs('reports')

    self.generate_json_report()
    self.generate_HTML_report()
    self.generate_csv_report()