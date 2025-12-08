import json
import os

# Define the file path (Ensure this matches where you store your data)
FILE_PATH = 'timeline.json'

def get_user_input():
    """Helper to get data via terminal for quick additions."""
    print("\n--- Add New Timeline Event ---")
    try:
        return {
            "year": int(input("Year (YYYY): ")),
            "month": input("Month (Short, e.g. 'Jan') [Optional]: ") or "",
            "title": input("Title: "),
            "visual": input("Emoji/Visual: "),
            "summary": input("Summary (1 sentence): "),
            "market_analysis": input("Market Analysis (Stocks/Impact): "),
            "products": input("Products (comma separated, e.g. Steel, Coal): ").split(','),
            "wiki_url": input("Wikipedia URL: ")
        }
    except ValueError:
        print("❌ Error: Year must be a number.")
        return None

def update_timeline(new_entry):
    # 1. Read existing data
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # 2. Clean up list (trim whitespace from products)
    if 'products' in new_entry and isinstance(new_entry['products'], list):
        new_entry['products'] = [p.strip() for p in new_entry['products']]

    # 3. Add new entry and Sort by Year (Newest First)
    data.append(new_entry)
    data.sort(key=lambda x: x['year'], reverse=True)

    # 4. Save back to file
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Successfully added '{new_entry['title']}' to {FILE_PATH}")

def add_industrial_revolution_pack():
    """Adds the missing era mentioned in README checklist."""
    events = [
        {
            "year": 1856,
            "title": "Bessemer Process",
            "visual": "🏗️",
            "summary": "First inexpensive industrial process for mass-production of steel.",
            "market_analysis": "Steel prices dropped 80%, enabling skyscrapers and railroads. Carnegie Steel boom.",
            "products": ["Railroad Tracks", "Skyscrapers", "Suspension Bridges"],
            "wiki_url": "https://en.wikipedia.org/wiki/Bessemer_process"
        },
        {
            "year": 1800,
            "title": "Voltaic Pile",
            "visual": "🔋",
            "summary": "Alessandro Volta invents the first true electric battery.",
            "market_analysis": "Precursor to all modern electronics energy storage sectors.",
            "products": ["Batteries", "Electroplating"],
            "wiki_url": "https://en.wikipedia.org/wiki/Voltaic_pile"
        }
    ]
    for event in events:
        update_timeline(event)

if __name__ == "__main__":
    print("1. Add Single Event (Interactive)")
    print("2. Add Industrial Revolution Pack (From Checklist)")
    choice = input("Select an option (1/2): ")

    if choice == "1":
        entry = get_user_input()
        if entry: update_timeline(entry)
    elif choice == "2":
        add_industrial_revolution_pack()