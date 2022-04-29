"""
This is the file that has the methods and attributes
for counting words
"""

from bs4 import BeautifulSoup

def add_two_numbers(a, b):
    return a + b

class WordCounter:
    """
    This is the class that does the job
    """

    def __init__(self, sentence):
        """
        class constructor
        :param sentence: str [this is a string of words]
        """
        assert isinstance(sentence, str), "input must be string"
        self.sentence = sentence

    def __repr__(self):
        """
        Class representaion
        :return: str
        """
        return f'<{self.sentence}>'

    def count_words(self):
        """
        Count the number of words in a sentence
        :return:
        """
        self.extract_text_from_possible_html()
        return len(self.sentence.split())

    def extract_text_from_possible_html(self):
        """
        Pass the sentence through a html filter
        and extract the text
        :return: str
        """
        soup = BeautifulSoup(self.sentence, "html.parser")
        text_list = [i.text for i in soup.find_all()]
        if len(text_list) != 0:
            self.sentence = " ".join(text_list)



if __name__ == "__main__":
    TEXT = "<p> I am studying at spiced </p>"
    word_instance = WordCounter(sentence=TEXT)
    print(word_instance.count_words())
