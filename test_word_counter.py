"""
This is the script that tests the word_counter.py
pytest is our module of choice to do our testing
"""
import pytest

from word_counter import WordCounter


# pylint: disable=R0201

class TestWordCounter:
    """
    Class must start with word Test to avoid
    being overlooked by pytest
    """

    def test_single_word(self):
        """
        test one word
        :return: None
        """
        text = "spiced"
        assert WordCounter(text).count_words() == 1

    def test_multiple_words(self):
        """
        testing more than one word
        :return: None
        """
        text = "This is our last week"
        assert WordCounter(text).count_words() == 5

    def test_line_breaks(self):
        """
        line breaks are characterised by '\n'
        :return: None
        """
        text = "I\nam\nhere waiting for \nyou"
        assert WordCounter(text).count_words() == 6

    def test_html(self):
        """
        Test if we can count words in a
        html content
        :return:
        """
        text = "<p> I want to drink coffee </p>"
        assert WordCounter(text).count_words() == 5

    def test_html_with_attributes(self):
        """
        Test if we can count words in a
        html content with attributes
        :return:
        """
        text = '<p class="spiced"> I want to drink coffee </p>'
        assert WordCounter(text).count_words() == 5

    def test_wrong_instance_type(self):
        """
        Testing the wrong instance type
        :return: None
        """
        text = ["my name is so and so"]
        with pytest.raises(Exception) as error:
            WordCounter(text).count_words()
        assert "input must be string" in str(error.value)
