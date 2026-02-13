# Hunter
AI powered powerful Anti-virus contain sandbox and Gemini AI 

# AI Sandbox Powered Antivirus

Advanced AI-driven antivirus with integrated behavioral sandbox analysis.

Developed by Navtej Singh  
Version 1.5.1  
Release Date: 13/02/2026  

---

## Overview

AI Sandbox Powered Antivirus is a hybrid security tool that combines:

- Static code inspection
- Behavioral sandbox execution
- AI-powered threat intelligence
- Automated deletion of malicious files

This project is built for educational and cybersecurity research purposes.

---

## Architecture

The antivirus operates in two main layers:

### 1. Sandbox Execution Layer

The file is executed inside a controlled environment.

Behavioral data collected:
- Execution timeout
- Files created
- Runtime behavior patterns
- Suspicious activity indicators

The behavior engine assigns a numerical threat score.

Modules:
- `DATA/sandbox.py`
- `DATA/behavior.py`

---

### 2. AI Threat Analysis Layer

The system sends:

- The original file code
- Sandbox execution report
- Behavior score

To a Gemini AI model for advanced reasoning-based analysis.


Model selection is dynamically configurable via:
```
FILES/modelID.py
```

---

## Project Structure

```
Antivirus/
│
├── main.py
├── setup.py
├── contactme.txt
│
├── FILES/
│   ├── api.py
│   ├── data.py
│   ├── modelID.py
│   └── logo.py
│
├── DATA/
│   ├── sandbox.py
│   └── behavior.py
│
└── modify/
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/Navtej-Singh-1503/Hunter
cd Antivirus
```

### 2. Install dependencies

```
sudo python3 setup.py
```

## Usage

Run:

```
python main.py
```

Then enter the file path to scan.

Example:

```
[*] Enter file path ..>> suspicious_script.py
```

---

## Detection Workflow

1. Validate file existence
2. Execute inside sandbox
3. Score behavior
4. Send code + report to AI
5. Receive classification
6. Optionally delete malicious file

---

## Security Notice

- This tool is designed for educational use.
- AI-based analysis should not replace professional antivirus software.

---

## License

Choose a license before publishing.

Recommended:
- MIT License (open and flexible)
- GPL v3 (strong open-source protection)

Add a `LICENSE` file before public release.

---

## Author

Navtej Singh Saggar  
Cybersecurity Student & Developer  

Contact: navtejsingh15032011@gmail.com

---

## Disclaimer

This software is provided for educational and research purposes only.  
The author is not responsible for misuse or damage caused by this tool.


---

## Support My Work

You can support me via cryptocurrency:

- LTC : ltc1qspfztcvax7g9caqgdmp3ex6fytrr0dlssr0r45
- URL : litecoin:LTC1QSPFZTCVAX7G9CAQGDMP3EX6FYTRR0DLSSR0R45

---

Copyright © 2026 Navtej Singh Saggar

All rights reserved.

This project and its source code are the intellectual property of
Navtej Singh Saggar. No part of this project may be copied, modified,
distributed, or used for commercial purposes without prior written
permission from the author.

This project is intended strictly for educational and personal learning use.
