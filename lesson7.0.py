from words_finder import WordsFinder

if __name__ == "__main__":
    finder2 = WordsFinder('test.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('Tell'))  # 3 слово по счёту
    print(finder2.count('aRe'))