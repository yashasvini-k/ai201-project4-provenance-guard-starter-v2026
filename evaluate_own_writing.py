
import requests

url = "http://127.0.0.1:5000/submit"

texts = [
    "In my experience, learning a new technical skill takes patience and consistent practice. I usually understand a concept better when I break it into smaller steps, try the code myself, and investigate errors instead of immediately looking for a solution.",
    "When I work on a project, I prefer to test each part before moving forward. This helps me identify problems earlier and understand why something works. I also keep track of the changes I make so I can revisit my decisions when I need to troubleshoot an issue.",
    "What I need right now is an iced coffee with toasted marshmallow syrup!",
    "I love to listen to EDM music when I run because the beats match up with my heart rate depending on what zone I choose to run in.",
    "I play games online to meet people and challenge them.",
    "Some writers have exceptional stories that are worth reading. Others may or may not depending on the storyline and how much the reader relates to it.",
    "Higher education is an indicator of intelligence. The higher the degree, the higher the knowledge. Therefore, those with PhDs are the most intelligent.",
    "Behavior is a result of a person's upbringing and the affect of those around them.",
    "An average person needs to drink atleast 3 gallons of water a day.",
    "Food consumed by an individual shows how much effort they put into taking care of themselves."
]

for trial in range(1, 4):
    ai_count = 0
    print(f"\nTRIAL {trial}")

    for i, text in enumerate(texts, start=1):
        response = requests.post(
            url,
            json={
                "text": text,
                "creator_id": f"own_writing_t{trial}_s{i}"
            },
            timeout=90
        )

        data = response.json()

        if response.status_code != 200:
            print(f"Sample {i}: ERROR {response.status_code} - {data}")
            continue

        guess = data.get("guess")
        if guess == "ai":
            ai_count += 1

        print(f"Sample {i}: {guess} | Confidence: {data.get('confidence')}")

    print(f"AI classifications: {ai_count}/10")
    print("Result:", "PASS" if ai_count <= 1 else "FAIL")
