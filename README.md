# Rule-Based AI Chatbot

**DecodeLabs Artificial Intelligence — Project 1 (Industrial Training Kit)**  
A deterministic, rule-based conversational agent implemented in standard Python 3.

---

## 1. Project Objective

The objective of Project 1 is to establish the fundamental foundation of Artificial Intelligence engineering: **Control Flow and Logic**. Before building probabilistic or machine learning systems that learn from data, engineers must master teaching machines through explicit programmatic decision-making. 

This project implements a deterministic, white-box chatbot adhering to the **Input -> Process -> Output (IPO)** architecture, providing zero-hallucination predictability, robust input sanitization, and structured exception handling.

---

## 2. Key Features

- **Input-Process-Output (IPO) Architecture**: Strict separation of concerns between input collection, data normalization/intent matching, and response output.
- **Phase 1 Sanitization & Normalization**:
  - Lowercases all characters (`raw_input.lower()`).
  - Strips leading and trailing whitespace (`strip()`).
  - Strips ASCII punctuation (`string.punctuation`).
  - Collapses consecutive internal whitespace down to single spaces.
- **Robust Decision Logic**:
  - Structured `if / elif / else` ladder matching against grouped constant sets (`frozenset`).
  - Defends against substring false-matches (e.g., `"this is a test"` will never mistakenly trigger `"hi"`).
  - Explicit Knowledge Base dictionary mapping 7 discrete intents (exceeding the 5+ intents requirement from the project specification).
- **Graceful Lifecycle Management**:
  - Continuous `while True` execution loop.
  - Recognizes multiple exit aliases: `exit`, `quit`, `bye`, `goodbye`.
  - Empty or whitespace-only inputs prompt the user to type something without terminating or crashing the loop.
  - Catches `KeyboardInterrupt` (Ctrl+C) and `EOFError` (Ctrl+D/Ctrl+Z) cleanly with no traceback.
- **Modular & Testable**:
  - `main(input_func=input, output_func=print)` supports dependency injection for full automated testing.
  - Protected with `if __name__ == "__main__":` to ensure importing `chatbot` produces zero side effects.
- **Zero Third-Party Dependencies**: Built exclusively with Python 3 standard library modules.

---

## 3. Technology Stack

- **Language**: Python 3.8+ (Verified and tested on Python 3.14.5)
- **Standard Library Modules**: `string`, `sys`, `unittest`, `subprocess`, `ast`, `os`
- **External Dependencies**: None (No third-party packages, ML libraries, databases, web servers, or external AI APIs)

---

## 4. Project Structure

```
rule-based-ai-chatbot/
│
├── .gitignore               # Ignores __pycache__, bytecode, and virtual environments
├── chatbot.py               # Main application (IPO logic, intent ladder, normalization)
├── README.md                # Comprehensive project documentation
└── tests/
    ├── __init__.py          # Test package marker
    └── test_chatbot.py      # Automated unittest suite (25 test cases)
```

---

## 5. Prerequisites

- Python 3.8 or higher installed on your system.
- Standard terminal (PowerShell, Command Prompt, Bash, or Zsh).

---

## 6. Execution and Testing Commands

### Compile Check
Verify code syntax without running:
```bash
python -m py_compile chatbot.py
```

### Run the Chatbot
Launch the interactive terminal session:
```bash
python chatbot.py
```

### Run Automated Unit Tests
Run the entire test suite with verbose output:
```bash
python -m unittest discover -s tests -v
```

---

## 7. Sample Conversation (Real Execution Output)

The following transcript was captured directly from running `python chatbot.py`:

```
Welcome to the Rule-Based AI Chatbot!
Type 'help' to see what I can do. Type 'exit' to quit.
You: HELLO
Hello! How can I help you today?
You: what can you do?
I can respond to predefined commands and basic questions using simple rules.
You: who are you?
I am a rule-based AI chatbot built with Python.
You: how are you?
I'm doing well, thank you! How can I help you today?
You: help
Supported commands and questions:
  - Greetings: 'hello', 'hi', 'hey'
  - Capabilities: 'what can you do?'
  - Identity: 'who are you?'
  - Status: 'how are you?'
  - Gratitude: 'thanks', 'thank you'
  - Help: 'help'
  - Exit: 'exit', 'quit', 'bye', 'goodbye'
You: an unsupported question
I'm not sure how to answer that yet. Try 'help' to see what I can do.
You:    
Please type something.
You: thank you!
You're welcome! Glad I could help.
You: quit
Goodbye! Have a great day!
```

---

## 8. Limitations of Rule-Based Matching

While rule-based chatbots provide determinism, 100% explainability, and zero hallucination risk, they possess significant architectural limitations:

1. **Rigid Pattern Matching**: The chatbot can only recognize inputs matching explicitly predefined patterns or keywords. Synonyms or varied phrasing not anticipated by the rule author trigger the fallback response.
2. **Lack of Semantic Understanding**: Unlike vector embedding models or neural networks, the bot does not grasp the conceptual meaning of words. It cannot associate `"farewell"` with `"bye"` unless explicitly coded.
3. **Absence of Context & State**: Each turn is evaluated independently. The bot lacks conversational memory, making multi-turn dialogue or resolving pronouns (e.g., "what did you say before?") impossible without dedicated state machines.
4. **High Maintenance & Scalability Cost**: As the domain grows, maintaining sets of rules leads to complex rule overlap and high cognitive overhead for developers.
