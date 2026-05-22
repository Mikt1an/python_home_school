# 1
import re

text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."

def find_date(date : str):
    """
        Extracts dates from a text string using regular expressions.

        Args:
            date (str):
                Input text containing dates.
        Returns:
            list:
                List of all detected dates.

        Description:
            The function searches for dates written in formats:
            - DD/MM/YYYY
            - DD.MM.YYYY
            - DD-MM-YYYY

            The pattern:
                \\d{2}\\D\\d{2}\\D\\d{4}

            means:
            - \\d{2} → exactly 2 digits
            - \\D     → any non-digit separator
            - \\d{2} → exactly 2 digits
            - \\D     → any non-digit separator
            - \\d{4} → exactly 4 digits

        Example:
            Input:
                "15/03/2025 and 01.12.2024"
            Output:
                ['15/03/2025', '01.12.2024']
    """
    return re.findall(r"(\d{2}\D\d{2}\D\d{4})", date)

res = find_date(text)
for item in res:
    print(item)


# 2
tag_input = "python, data-science / machine learning; AI neural-networks"


def find_tag(tag_list : str):
    """
        Splits a tag string into separate tags using multiple delimiters.

        Args:
            tag_list (str):
                String containing tags separated by symbols or spaces.
        Returns:
            list:
                List of separated tags.

        Description:
            The function uses `re.split()` to split text by:
            - commas
            - semicolons
            - slashes
            - spaces

            Regex pattern:
                [,;/\\s]+

            means:
            - ,     → comma
            - ;     → semicolon
            - /     → slash
            - \\s    → whitespace
            - +     → one or more separators

        Example:
            Input:
                "python, AI / machine-learning"
            Output:
                ['python', 'AI', 'machine-learning']
    """
    return re.split(r"[,;/\s]+", tag_input)


res = find_tag(tag_input)
print(res)