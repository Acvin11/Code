import pymongo
import os


mongo_host = "mongo2"


collection = pymongo.MongoClient("mongodb://" + mongo_host)["fashion"]["cookie_requests"]


documents = collection.find({"active" : True}).sort("browser", 1)


html_page = "<!DOCTYPE html>\n<html><table border = 5 cellpadding = 5>"


fieldnames = ["browser", "host", "cookies"]
fieldnames = ["<th>" + x + "</th>" for x in fieldnames]


html_page += "\n<tr> " + " ".join(fieldnames)  + " </tr>"


for document in documents:

    browser = str(document["browser"])

    host = str(document["host"])

    cookies = ", ".join(document["cookies"])


    data = [browser, host, cookies]
    data = [x.encode('utf-8').decode('latin-1') for x in data]
    data = ["<td>" + x + "</td>" for x in data]

    html_page += "\n<tr> " + " ".join(data) + " </tr>"


html_page += "\n</table></html>"


email = "mumbaicrawlingteam@intelligencenode.com"

subject = "Dynamic Cookies Export"

command = 'echo "{}" | mutt -e "set content_type=text/html" {} -s "{}"'.format(html_page, email, subject)

os.system(command)
