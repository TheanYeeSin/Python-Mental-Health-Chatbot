import json

# load tests from json file
with open("ChatbotWebsite/static/data/tests.json") as file:
    tests = json.load(file)


# get test questions
def get_questions(title):
    for test in tests["tests"]:
        if test["title"] == title:
            return test["questions"]
    return "Test not found"


# get test score message
def get_test_messages(title, score):
    score = int(score)
    message = ""
    if title.lower() == "depression test":  # depression test
        if score > 20:
            message = "Depression Test: Severe Depression"
        elif score > 15:
            message = "Depression Test: Moderately Severe Depression"
        elif score > 10:
            message = "Depression Test: Moderate Depression"
        elif score > 5:
            message = "Depression Test: Mild Depression"
        else:
            message = "Depression Test: No Depression"
        message += (
            " - Score: "
            + str(score)
            + "/27 (Your responses indicate that you may be at risk of harming yourself. If you need immediate help, you can reach the mental health service by clicking the SOS button on top right!)"
        )
    elif title.lower() == "anxiety test":  # anxiety test
        if score > 15:
            message = "Anxiety Test: Severe Anxiety"
        elif score > 10:
            message = "Anxiety Test: Moderate Anxiety"
        elif score > 5:
            message = "Anxiety Test: Mild Anxiety"
        else:
            message = "Anxiety Test: No Anxiety"
        message += " - Score: " + str(score) + "/21"
    else:
        message = "Test Title not found"
    message += ". These results are not meant to be a diagnosis. You can meet with a doctor or therapist to get a diagnosis and/or access therapy or medications. Sharing these results with someone you trust can be a great place to start."
    return message
