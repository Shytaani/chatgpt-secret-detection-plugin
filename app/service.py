import re

import openai
import yaml


def detect_sensitive_info(prompt: str) -> (bool, list[str]):
    """Detect sensitive information in the prompt.

    Args:
        prompt (str): The prompt to detect sensitive information in.

    Returns:
        (bool, list[str]): A tuple containing a boolean indicating whether sensitive information was detected
        and a list of messages to display to the user.
    """
    messages = []
    with open("rules.yml", "r") as f:
        rules = yaml.safe_load(f).items()
    for rule in rules:
        matched_word = re.search(rule[1]["pattern"], prompt)
        if matched_word:
            messages.append(f"{rule[1]['message']}: {matched_word}")
    if messages:
        return True, messages
    else:
        return False, []


def send_prompt(prompt: str) -> str:
    """Send the prompt to ChatGPT.

    Args:
        prompt (str): The prompt to send to ChatGPT.

    Returns:
        str: The response from ChatGPT.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    return response["choices"][0]["message"]["content"]
