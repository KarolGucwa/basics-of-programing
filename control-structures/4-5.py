import emails

file_name = 'email.txt'

with open(file_name, 'r', encoding='utf-8') as file:
    email_content = file.read()

sender = emails.email_sender(email_content)
recipient = emails.email_recipient(email_content)
subject = emails.email_subject(email_content)
body = emails.email_body(email_content)

print(f"Sender: {sender}")
print(f"Recipient: {recipient}")
print(f"Subject: {subject}")
print(f"Body:\n{body}")
