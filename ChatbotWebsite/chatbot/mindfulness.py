import json

# load mindfulness exercises from json file
with open("ChatbotWebsite/static/mindfulness/mindfulness.json") as file:
    mindfulness_exercises = json.load(file)


# get mindfulness exercise description and filename
def get_description(title):
    for exercise in mindfulness_exercises["mindfulness_exercises"]:
        if exercise["title"] == title:
            return exercise["description"], exercise["file_name"]
    return "Exercise not found"
