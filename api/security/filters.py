import re


class ContentFilter:
    def __init__(self):
        self.email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        self.blacklist = ["internal_password", "secret_key_v1", "confidential_project_x"]

    def filter_output(self, text: str) -> str:
        text = self.email_pattern.sub("[EMAIL_REDACTED]", text)

        for word in self.blacklist:
            if word in text:
                return "Error: The response was blocked due to security policy."

        return text