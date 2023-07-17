import json

# load topics from json file
with open("ChatbotWebsite/static/data/topics.json") as file:
    topics = json.load(file)


# get topic content
def get_content(title):
    for topic in topics["topics"]:
        if topic["title"] == title:
            return topic["content"]
    return "Topic not found"
