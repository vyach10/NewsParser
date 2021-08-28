from search import search_pages_by_day
import json

labels = ["link", "title", "txt", "img_link", "parsed_at"]
page_data = '{"link": "", "title": "", "txt": "", "img_link": "", "parsed_at": ""}'
page_data = json.loads(page_data)
export_data = ""

for news in search_pages_by_day(3):
    for i in range(0,len(labels)):
        page_data[labels[i]] = str(news[i])
    export_data += str(page_data)
    export_data += ","

export_data = json.dumps(export_data[0:-1])

print(export_data)