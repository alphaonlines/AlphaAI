import json
import os

# Define the new event data
new_event = {
    "year": 2026,
    "month": "Jan",
    "title": "AGI Breakthrough",
    "visual": "🧠",
    "summary": "First verified instance of Artificial General Intelligence.",
    "why": "Machines can now perform any intellectual task a human can.",
    "stockReaction": "Global markets halt trading due to volatility.",
    "emoji": "🤯",
    "imgQuery": "futuristic artificial general intelligence brain"
}

def update_timeline(new_entry):
    file_path = 'timeline.json'
    
    # 1. Read existing data
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    # 2. Add new entry to the top (since your timeline is newest-first)
    data.insert(0, new_entry)

    # 3. Save back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully added '{new_entry['title']}' to timeline.json")

if __name__ == "__main__":
    update_timeline(new_event)