def detect_inappropriate_language(text):

    inappropriate_words = ['inappropriate', 'offensive', 'profanity']

    for word in inappropriate_words:
        if word in text:
            return True

    return False
