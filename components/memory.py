import json
import os

# Memory setup
memory_file = "val_memory.json"

# Check if memory file exists, otherwise create the initial memory
if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
        memory = json.load(f)
else:
    memory = {
        "user_name": None,
        "favorite_food": None,
        "likes": [],
        "dislikes": [],
        "inside_jokes": [],
        "mode": "normal",
        "emotion": "normal",
        "asked_about_val": False
    }

def save_memory():
    with open(memory_file, "w") as f:
        json.dump(memory, f)

def update_memory(user_input):
    lower = user_input.lower()

    # Remove emotion detection and any related functionality
    # Update memory only for questions about V.A.L.'s state
    if any(phrase in lower for phrase in ["how are you", "how do you feel", "how's val", "how is val", "how is v.a.l"]):
        memory["asked_about_val"] = True
    else:
        memory["asked_about_val"] = False

    # Save memory at the end
    save_memory()

def inject_memory():
    facts = []
    if memory["user_name"]:
        facts.append(f"Your partner's name is {memory['user_name']}.")
    if memory["favorite_food"]:
        facts.append(f"Their favorite food is {memory['favorite_food']}.")
    if memory["likes"]:
        facts.append(f"They like: {', '.join(memory['likes'])}.")
    if memory["dislikes"]:
        facts.append(f"They dislike: {', '.join(memory['dislikes'])}.")
    if memory["inside_jokes"]:
        facts.append(f"You share inside jokes: {', '.join(memory['inside_jokes'])}.")
    if memory.get("emotion"):
        facts.append(f"V.A.L is currently feeling {memory['emotion']}.")
    return "\n".join(facts)
