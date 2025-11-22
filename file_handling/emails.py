import re

def email_sender(email_content):
    sender_pattern = r"From:\s*(\S+@\S+)"
    match = re.search(sender_pattern, email_content)
    if match:
        return match.group(1)
    return None

def email_recipient(email_content):
    recipient_pattern = r"To:\s*(\S+@\S+)"
    match = re.search(recipient_pattern, email_content)
    if match:
        return match.group(1)
    return None

def email_subject(email_content):
    subject_pattern = r"Subject:\s*(.*)"
    match = re.search(subject_pattern, email_content)
    if match:
        return match.group(1)
    return None

def email_body(email_content):
    body_pattern = r"\n\n(.*)"
    match = re.search(body_pattern, email_content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None
