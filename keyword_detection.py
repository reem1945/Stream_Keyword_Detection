from collections import Counter

# Liste des mots-clés à rechercher
keywords = ["data science", "python", "MLops"]

# Fonction de comptage des mots-clés
def count_keywords(text, keywords):
    words = text.lower().split()
    word_count = Counter(words)
    keyword_count = {keyword: word_count.get(keyword, 0) for keyword in keywords}
    return keyword_count
