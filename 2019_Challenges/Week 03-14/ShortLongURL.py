"""
Problem for DoJo on March 14, 2019.

Implement a URL shortener with the following methods:

shorten(URL), which shortens the URL into a six-character alphanumeric
string, such as zLg6wl.

restore(short), which expands the shortened string into the
original URL. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
"""
from string import ascii_letters, digits
from secrets import choice


class URLShortener(object):

    def __init__(self):
        self.url_dict: dict = dict()
        self.alphabet: str = ascii_letters + digits

    def shorten(self, long_url: str) -> str:
        """
        Remember this long URL and return a short string to replace it.

        :param long_url: original url
        :return: short url replacement
        """
        short_url = self.check_history(long_url)
        if short_url == None:
            short_url = self.get_new_short_url(long_url)
            self.add_long_url(long_url, short_url)
        return short_url

    def restore(self, short_url: str) -> str:
        """
        Restore the full url if known.

        :param short_url:
        :return:
        """
        full_url = None
        if short_url in self.url_dict:
            full_url = self.url_dict[short_url]
        return full_url

    def compare_lsl(self, orig_url, short_url, comparison_url):
        """
        Display the original url, the short replacement, and if we got the
        same back.

        :param orig_url:
        :param short_url:
        :param comparison_url:
        :return:
        """
        if orig_url == comparison_url:
            msg = 'Success!!!'
        else:
            msg = '>>>>> BAD <<<<<'
        print(f'LSL - Original: {orig_url}, short: {short_url}, returned: '
              f'{comparison_url}, Result: {msg} ')
        return

    def compare_dup(self, long_url, first_short_url, second_short_url):
        """
        Display the long url, both short urls, and match status.
        :param long_url:
        :param first_short_url:
        :param second_short_url:
        :return:
        """
        if first_short_url == second_short_url:
            msg = 'Success!!!'
        else:
            msg = '>>>>> BAD <<<<<'
        print(f'Dup Original: {long_url}, first: {first_short_url}, second: '
              f'{second_short_url}, result: {msg}')
        return

    def generate_short_url_6(self) -> str:
        """
        Generate a random sequence of letters and digits - six chars long.

        :return:
        """
        password = ''.join(choice(self.alphabet) for i in range(6))
        return password

    def get_new_short_url(self, long_url: str) -> str:
        """
        Get a random short url to add to url dictionary.

        :param long_url:
        :return: a short url associated with this long url in the dictionary
        """
        key_in_dict = True
        short_url = None
        while key_in_dict:
            short_url = self.generate_short_url_6()
            if not short_url in self.url_dict:
                self.url_dict[short_url] = long_url
                key_in_dict = False

        return short_url

    def add_long_url(self, long_url: str, short_url: str):
        """
        Add the short url to the dict with the long url as the key.

        :param long_url:
        :param short_url:
        :return:
        """
        self.url_dict[long_url] = short_url
        return

    def check_history(self, long_url: str) -> str:
        """
        Check to see if url has already been shortened before.

        :param long_url: url for which to search
        :return: short url if found or null
        """
        short_url = self.url_dict.get(long_url, None)
        return short_url


if __name__ == '__main__':
    # test data
    url_1 = 'http://localhost:63342/Food-Pantry-Inventory/docs/build/html' \
            '/UML%20Diagrams.html'
    url_2 = 'https://github.com/deeppunster/Christmas-Labels.git'
    url_3 = 'https://krebsonsecurity.com/'

    # establish instance of class
    short_long = URLShortener()

    # get short url for test data
    short_url_1 = short_long.shorten(url_1)
    short_url_2 = short_long.shorten(url_2)
    short_url_3 = short_long.shorten(url_3)

    # get the long url back
    long_url_1 = short_long.restore(short_url_1)
    long_url_2 = short_long.restore(short_url_2)
    long_url_3 = short_long.restore(short_url_3)

    # compare return values with original
    short_long.compare_lsl(url_1, short_url_1, long_url_1)
    short_long.compare_lsl(url_2, short_url_2, long_url_2)
    short_long.compare_lsl(url_3, short_url_3, long_url_3)

    # bonus - see if we get duplicate short url for same long url
    short_url_4 = short_long.shorten(url_1)
    short_url_5 = short_long.shorten(url_2)
    short_url_6 = short_long.shorten(url_3)

    # compare for duplicate short urls
    short_long.compare_dup(url_1, short_url_1, short_url_4)
    short_long.compare_dup(url_2, short_url_2, short_url_5)
    short_long.compare_dup(url_3, short_url_3, short_url_6)

# EOF
