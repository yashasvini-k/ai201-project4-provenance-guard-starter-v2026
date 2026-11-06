
import requests
from statistics import mean

url = "http://127.0.0.1:5000/submit"

human_texts = [
    "In my experience, learning a new technical skill takes patience and consistent practice. I usually understand a concept better when I break it into smaller steps, try the code myself, and investigate errors instead of immediately looking for a solution.",
    "When I work on a project, I prefer to test each part before moving forward. This helps me identify problems earlier and understand why something works. I also keep track of the changes I make so I can revisit my decisions when I need to troubleshoot an issue.",
    "I love to listen to EDM music when I run because the beats match up with my heart rate depending on what zone I choose to run in.",
    "Higher education is an indicator of intelligence. The higher the degree, the higher the knowledge. Therefore, those with PhDs are the most intelligent.",
    "Food consumed by an individual shows how much effort they put into taking care of themselves."
]

ai_texts = [
    "Artificial intelligence is transforming the way organizations manage information and complete everyday tasks. By automating repetitive processes, businesses can improve efficiency, reduce operational costs, and allow employees to focus on more complex responsibilities.",
    "Cybersecurity plays an essential role in protecting digital systems from unauthorized access and malicious activity. Organizations should implement strong authentication, monitor network traffic, and regularly review security controls to reduce their exposure to potential threats.",
    "Effective communication is important when working in a team because it helps establish shared expectations and prevents misunderstandings. Clearly defined responsibilities also make it easier to track progress and address challenges throughout a project.",
    "Cloud computing provides organizations with flexible access to computing resources without requiring them to maintain all infrastructure themselves. Services such as storage, virtual machines, and managed databases can support applications as business requirements change.",
    "Developing a successful software application requires careful planning, testing, and continuous improvement. Developers should consider user needs, validate incoming data, and identify potential failures before deploying changes to a production environment."
]

for trial in range(1, 4):
    human_scores = []
    ai_scores = []

    print(f"\nTRIAL {trial}")

    for group, texts, scores in [
        ("HUMAN", human_texts, human_scores),
        ("AI", ai_texts, ai_scores)
    ]:
        for i, text in enumerate(texts, start=1):
            response = requests.post(
                url,
                json={
                    "text": text,
                    "creator_id": f"spread_{group.lower()}_t{trial}_s{i}"
                },
                timeout=90
            )

            data = response.json()

            if response.status_code != 200:
                print(f"{group} sample {i}: ERROR {response.status_code} - {data}")
                continue

            score = data["combined_score"]
            model_score = data["model_score"]
            style_score = data["style_score"]
            scores.append(score)

            print(
                f"{group} sample {i}: "
                f"Model={model_score:.4f} | "
                f"Style={style_score:.4f} | "
                f"Combined={score:.4f}"
            )

    if len(human_scores) == 5 and len(ai_scores) == 5:
        human_average = mean(human_scores)
        ai_average = mean(ai_scores)
        difference = ai_average - human_average

        print(f"Human average: {human_average:.4f}")
        print(f"AI average: {ai_average:.4f}")
        print(f"Score difference: {difference:.4f}")
        print("Result:", "PASS" if difference >= 0.20 else "FAIL")
    else:
        print("INCOMPLETE: Not all 10 samples were scored.")
