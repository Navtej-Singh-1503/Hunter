'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

13/02/2026


mail - navtejsingh15032011@gmail.com

'''

import os
from google import genai
from api import apikey
from pathlib import Path

# Create client
client = genai.Client(api_key=apikey)

print("--- Fetching Available Models ---")

available_models = []

try:
    for m in client.models.list():
        if 'generateContent' in m.supported_actions:
            available_models.append(m.name)

except Exception as e:
    print(f"Error fetching models: {e}")
    exit()

# Model mapping
model_options = {
    "1": "model/gemini-3-pro-preview",
    "2": "model/gemini-3-flash-preview",
    "3": "model/gemini-2.5-pro",
    "4": "model/gemini-2.5-flash",
    "5": "model/gemini-2.5-flash-lite",
    "6": "model/gemini-2.0-flash"
}

print("\nAvailable Choices:")
print("1. gemini-3-pro-preview")
print("2. gemini-3-flash-preview")
print("3. gemini-2.5-pro")
print("4. gemini-2.5-flash")
print("5. gemini-2.5-flash-lite")
print("6. gemini-2.0-flash")

user_choice = input("\nWHICH MODEL YOU WANT TO USE (IN NUMBER) ...>> ")

if user_choice in model_options:
    
    model_id = model_options[user_choice]

    # Create FILES directory if not exists
    files_dir = Path("../FILES")
    files_dir.mkdir(exist_ok=True)

    model_file = files_dir / "modelID.py"

    # Write model ID
    with open(model_file, "w") as f:
        f.write(f'model_id = "{model_id}"')

    print(f"\n[✓] Model set to {model_id}")

else:
    print("[!] Invalid choice")

