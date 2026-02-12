'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

13/02/2026

Version - 1.5.1

mail - navtejsingh15032011@gmail.com

'''




from google import genai
import time
import sys
import os

from FILES.api import apikey
from FILES.data import system_promt
from FILES.modelID import *
from FILES.logo import logo


from DATA.sandbox import run_in_sandbox
from DATA.behavior import score_behavior



os.system("clear")


RED = "\033[1;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
PURPLE = "\033[1;35m"
RESET = "\033[0m"



def slowprint(s):
        for c in s + '\n' :
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(4. / 100)


slowprint(RED + logo)



API_KEY = apikey
client = genai.Client(api_key=API_KEY)

file = input(GREEN+"[*] Enter file path ..>> ")

if not os.path.isfile(file):
    print(RED + "[!] Invalid file path")
    exit()

with open(file, "r", errors="ignore") as reading:
    user_input = reading.read()


def start_scan():
    print(RESET+"SCANNING...")

    # ---------------- Sandbox Layer ----------------
    print(RED+"\n--- Sandbox Execution ---")

    sandbox_report = run_in_sandbox(file)
    behavior_score = score_behavior(sandbox_report)

    print(GREEN+"[+] Timeout:", sandbox_report["timeout"])
    print("[+] Created files:", sandbox_report["created_files"])
    print("[+] Behavior Score:", behavior_score)

    # ---------------- AI Layer ----------------


    print(RED+"\n--- AI SCANING ---")
    print("[*] IT MAY TAKE A FEW SECONDS")

    try:
        response = client.models.generate_content(
            model=model_id,
            contents=system_promt + "\n\nSANDBOX REPORT:\n"
                     + str(sandbox_report)
                     + "\nBehavior score: "
                     + str(behavior_score)
                     + "\n\nCODE:\n"
                     + user_input,
        )

        if not response.text:
            print(PURPLE+"[!] AI: [No response generated]")
            return

        print(GREEN+"\n[+] AI:")
        print(response.text)

        final_code = response.text.strip().splitlines()[-1]

        if final_code == "99":
            print(RED+"[!] DANGEROUS")
            print(RED+"[!] NEED TO BE DELETED")

            delete = input(GREEN+"[*] WANT TO DELETE THIS FILE? [Y/N] : ").lower()

            if delete == "y":
                try:
                    os.remove(file)
                    print(GREEN+"[+] File deleted safely.")
                except Exception as err:
                    print(RED+"[!] Could not delete file:", err)

            else:
                print(RED+"[!] ABORTED")

        elif final_code == "55":
            print(GREEN+"[*] SAFE — NO NEED TO REMOVE")

    except Exception as e:
        print(RED+"[!] Detailed Error:", e)


if __name__ == "__main__":
    start_scan()

