HIGH_RISK = [
    "chest pain",
    "difficulty breathing",
    "heart attack",
    "stroke",
    "blood vomiting",
    "seizure",
    "unconscious"
]

MEDIUM_RISK = [
    "high fever",
    "persistent cough",
    "severe headache",
    "vomiting"
]


def detect_risk(text):

    text = text.lower()

    for item in HIGH_RISK:
        if item in text:
            return "🔴 HIGH"

    for item in MEDIUM_RISK:
        if item in text:
            return "🟠 MEDIUM"

    return "🟢 LOW"
