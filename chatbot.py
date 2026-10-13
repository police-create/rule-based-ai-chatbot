"""Rule-Based AI Chatbot.

DecodeLabs AI Project 1: Industrial Training Kit.
Demonstrates deterministic control flow, Input-Process-Output (IPO) architecture,
input sanitization/normalization, explicit if/elif/else decision ladder,
and graceful loop/exception management using Python's standard library only.
"""

import string
import sys

# --- EXACT BEHAVIOR CONSTANTS ---
WELCOME_LINE_1 = "Welcome to the Rule-Based AI Chatbot!"
WELCOME_LINE_2 = "Type 'help' to see what I can do. Type 'exit' to quit."

GREETING_RESPONSE = "Hello! How can I help you today?"
CAPABILITY_RESPONSE = (
    "I can respond to predefined commands and basic questions using simple rules."
)
UNKNOWN_RESPONSE = (
    "I'm not sure how to answer that yet. Try 'help' to see what I can do."
)
EXIT_RESPONSE = "Goodbye! Have a great day!"
EMPTY_INPUT_RESPONSE = "Please type something."

HOW_ARE_YOU_RESPONSE = "I'm doing well, thank you! How can I help you today?"
IDENTITY_RESPONSE = "I am a rule-based AI chatbot built with Python."
GRATITUDE_RESPONSE = "You're welcome! Glad I could help."

HELP_RESPONSE = (
    "Supported commands and questions:\n"
    "  - Greetings: 'hello', 'hi', 'hey'\n"
    "  - Capabilities: 'what can you do?'\n"
    "  - Identity: 'who are you?'\n"
    "  - Status: 'how are you?'\n"
    "  - Gratitude: 'thanks', 'thank you'\n"
    "  - Help: 'help'\n"
    "  - Exit: 'exit', 'quit', 'bye', 'goodbye'"
)

# --- INTENT PATTERN SETS ---
# Grouped into sets for fast O(1) membership testing and concise if/elif branching
EXIT_INPUTS = frozenset({"exit", "quit", "bye", "goodbye"})
GREETING_INPUTS = frozenset(
    {
        "hello",
        "hi",
        "hey",
        "hello there",
        "hi there",
        "hey there",
        "greetings",
        "good morning",
        "good afternoon",
        "good evening",
    }
)
CAPABILITY_INPUTS = frozenset(
    {
        "what can you do",
        "what can you do?",
        "capabilities",
        "features",
        "what do you do",
    }
)
HELP_INPUTS = frozenset({"help", "commands", "menu", "options", "support"})
HOW_ARE_YOU_INPUTS = frozenset(
    {"how are you", "how are you?", "how are you doing", "how r u", "how do you do"}
)
IDENTITY_INPUTS = frozenset(
    {
        "who are you",
        "who are you?",
        "what are you",
        "what is your name",
        "tell me about yourself",
        "who made you",
    }
)
GRATITUDE_INPUTS = frozenset(
    {"thanks", "thank you", "thx", "thank you very much", "many thanks"}
)

# --- KNOWLEDGE BASE (Dictionary representation of 5+ intents, PDF Slide 17) ---
KNOWLEDGE_BASE = {
    "greetings": {
        "patterns": GREETING_INPUTS,
        "response": GREETING_RESPONSE,
    },
    "capabilities": {
        "patterns": CAPABILITY_INPUTS,
        "response": CAPABILITY_RESPONSE,
    },
    "help": {
        "patterns": HELP_INPUTS,
        "response": HELP_RESPONSE,
    },
    "how_are_you": {
        "patterns": HOW_ARE_YOU_INPUTS,
        "response": HOW_ARE_YOU_RESPONSE,
    },
    "identity": {
        "patterns": IDENTITY_INPUTS,
        "response": IDENTITY_RESPONSE,
    },
    "gratitude": {
        "patterns": GRATITUDE_INPUTS,
        "response": GRATITUDE_RESPONSE,
    },
    "exit": {
        "patterns": EXIT_INPUTS,
        "response": EXIT_RESPONSE,
    },
}


def normalize_input(raw_input: str) -> str:
    """Normalize input: lowercase, strip, remove punctuation, collapse repeated spaces.

    Adheres to Phase 1 sanitization:
    clean_input = raw_input.lower().strip(), followed by punctuation removal
    and whitespace collapsing.
    """
    if not isinstance(raw_input, str):
        return ""
    # 1. Lowercase and strip leading/trailing whitespace
    clean_input = raw_input.lower().strip()
    # 2. Remove punctuation
    clean_input = clean_input.translate(str.maketrans("", "", string.punctuation))
    # 3. Collapse repeated spaces
    clean_input = " ".join(clean_input.split())
    return clean_input


def is_exit_command(cleaned_input: str) -> bool:
    """Return True if the input matches any recognized exit command alias."""
    if not isinstance(cleaned_input, str):
        return False
    # Defensively normalize in case raw text was passed
    normalized = normalize_input(cleaned_input)
    return normalized in EXIT_INPUTS


def get_response(cleaned_input: str) -> str:
    """Return a response using an explicit if / elif / else decision ladder.

    Grouped sets are evaluated to keep the ladder concise, robust, and
    resistant to substring false-matching.
    """
    if not isinstance(cleaned_input, str):
        return EMPTY_INPUT_RESPONSE

    # Defensively normalize to ensure uniform pattern matching
    clean = normalize_input(cleaned_input)

    if not clean:
        return EMPTY_INPUT_RESPONSE
    elif clean in EXIT_INPUTS:
        return EXIT_RESPONSE
    elif clean in GREETING_INPUTS:
        return GREETING_RESPONSE
    elif clean in CAPABILITY_INPUTS:
        return CAPABILITY_RESPONSE
    elif clean in HELP_INPUTS:
        return HELP_RESPONSE
    elif clean in HOW_ARE_YOU_INPUTS:
        return HOW_ARE_YOU_RESPONSE
    elif clean in IDENTITY_INPUTS:
        return IDENTITY_RESPONSE
    elif clean in GRATITUDE_INPUTS:
        return GRATITUDE_RESPONSE
    else:
        return UNKNOWN_RESPONSE


def main(input_func=input, output_func=print) -> None:
    """Run the main interactive chatbot loop.

    Follows the Input -> Process -> Output (IPO) structure, runs in a continuous
    `while True` loop, breaks on exit commands, and handles KeyboardInterrupt
    and EOFError gracefully with no traceback.
    """
    try:
        output_func(WELCOME_LINE_1)
        output_func(WELCOME_LINE_2)

        while True:
            # 1. INPUT
            try:
                try:
                    raw_input = input_func("You: ")
                except TypeError:
                    raw_input = input_func()
            except (KeyboardInterrupt, EOFError):
                output_func(EXIT_RESPONSE)
                break

            # 2. PROCESS
            clean_input = normalize_input(raw_input)

            if not clean_input:
                # 3. OUTPUT: Empty input handling
                output_func(get_response(clean_input))
                continue

            if is_exit_command(clean_input):
                # 3. OUTPUT: Exit handling & clean loop break
                output_func(get_response(clean_input))
                break

            response = get_response(clean_input)

            # 3. OUTPUT: Standard response
            output_func(response)

    except (KeyboardInterrupt, EOFError):
        try:
            output_func(EXIT_RESPONSE)
        except Exception:
            pass


if __name__ == "__main__":
    main()
