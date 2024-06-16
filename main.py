"""
This module contains the main functionality of the Steam User Reviews Scraper.
"""

import sys
import urllib.parse
import requests
import config
from app import database
from app import urlbuilder

class Main:
    """
    This class represents the main functionality of the Steam User Reviews Scraper.

    Attributes:
        url (str): The URL used for sending requests.
        url_builder (URLBuilder): An instance of the URLBuilder class for building URLs.
        database (Database): An instance of the Database class for interacting with the database.
    """

    def __init__(self) -> None:
        """
        Initializes the Main class.
        """
        self.url:str = ""
        self.url_builder:urlbuilder.URLBuilder = urlbuilder.URLBuilder()
        self.database:database.Database = database.Database()


    def request_reviews(self, url:str) -> dict:
        """
        Sends a GET request to the specified URL and returns the response as a JSON dictionary.

        Args:
            url (str): The URL to send the request to.

        Returns:
            dict: The response from the request as a JSON dictionary. If the request fails or
                    the response status code is not 200, an empty dictionary is returned.
        """
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        return {}

    def main(self, app:str|int = "*") -> None:
        """
        The main function of the Steam User Reviews Scraper.

        Args:
            app (str|int): The name or ID of the app to search for. Defaults to "*".

        Returns:
            None
        """
        if app == "*":
            app_ids = self.database.get_all_app_ids()
        elif app.isdigit():
            app_ids.append(self.database.get_app_name_from_id(app))
        elif app.isalpha():
            app_ids = self.database.get_app_ids_from_name(app)
        else:
            sys.exit(1)

        print(app_ids)
        for app_id in app_ids:
            cursor = config.CURSOR
            has_cursor = True
            while has_cursor:
                # build the URL
                self.url_builder.set_cursor(cursor)
                self.url_builder.set_appid(app_id)
                self.url_builder.build()
                self.url = self.url_builder.get_url()

                # request the reviews
                response = self.request_reviews(self.url)
                # check if the response contains reviews

                # * insert / update app info
                # * insert / update author info
                # * insert / update review info

                if len(response) > 0 and "reviews" in response:
                    for review in response.get("reviews"):
                        # TODO: implement the data processing
                        # if self.database.is_review_exists(data[0], data[1]):
                        #     self.database.update_review(data)
                        # else:
                        #     self.database.insert_review(data)
                        pass
                else:
                    has_cursor = False

                # * update cursor
                cursor = response.get("cursor", None)
                if cursor is not None:
                    cursor = urllib.parse.quote(cursor)
                else:
                    has_cursor = False

        self.database.close()


    def display_help(self, command: str = "") -> None:
        """
        Display help information for the command.

        Args:
            command (str): The command to display help for. Defaults to an empty string.

        Returns:
            None
        """
        if command == "":
            print("Usage: python main.py <app>")
            print("app: The name or id of the app to search for.")


if __name__ == "__main__":
    main = Main()

    if len(sys.argv) > 1 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        main.display_help()
    elif len(sys.argv) > 1:
        main.main(sys.argv[1])
    else:
        main.main("*")
    sys.exit(1)
