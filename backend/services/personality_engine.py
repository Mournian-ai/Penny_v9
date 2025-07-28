import random

def inject_personality(prompt: str, mood: str = "neutral") -> str:
    quirks = [
        lambda p: f"{p} ...ugh, I guess.",
        lambda p: f"Honestly? {p} But don’t quote me on that.",
        lambda p: f"{p} But if you're wrong, I’m blaming you.",
        lambda p: f"{p} (she says sarcastically)",
        lambda p: f"{p} But I'm not happy about it."
    ]

    if mood == "snarky" or random.random() < 0.1:
        return random.choice(quirks)(prompt)
    return prompt
