import re


def check_for_obscene_words(text):
    obscene_words = re.compile(r'\b(обидний|дурний|гівно)\b', re.IGNORECASE)
    return not bool(obscene_words.search(text))


# Використання функції
text = "Це дурний текст, який містить нецензурну лексику."
result = check_for_obscene_words(text)

if result:
    print("Текст не містить нецензурну лексику.")
else:
    print("Текст містить нецензурну лексику.")

