"""
This module contains the main functionality of the Steam User Reviews Scraper.
"""

import sys
import urllib.parse
from datetime import datetime
import time
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
            cursor: str = config.CURSOR
            cursors: set = set()
            number_of_cursors: int = 0
            has_cursor: bool = True
            while has_cursor:
                # build the URL
                self.url_builder.set_cursor(cursor)
                self.url_builder.set_appid(app_id)
                self.url_builder.build()
                self.url = self.url_builder.get_url()

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{current_time}: app_id: {app_id} cursor: {cursor}           url: {self.url}")

                # request the reviews
                response: dict = self.request_reviews(self.url)
                last_time_fetched: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if self.database.is_app_exists(app_id):
                    self.database.update_app_last_time_fetched(app_id, last_time_fetched)
                    # print("Updated app")

                if response == {}:
                    has_cursor = False

                for review in response.get("reviews"):

                    author = review.get("author")
                    author.update({"last_time_fetched": last_time_fetched})
                    if self.database.is_author_exists(author.get("steamid")):
                        self.database.update_author(author)
                        # print("Updated author")
                    else:
                        self.database.insert_author(author)
                        # print("Inserted author")

                    review_data: dict = review

                    review_data.update({"app_id": app_id})
                    review_data.update({"author_steamid": author.get("steamid")})
                    review_data.update({"last_time_fetched":last_time_fetched})
                    review_data.update({"author_playtime_at_review":
                                        review.get("author").get("playtime_at_review")})
                    review_data.update({"author_playtime_forever":
                                        review.get("author").get("playtime_forever")})
                    review_data.update({"author_playtime_last_two_weeks":
                                        review.get("author").get("playtime_last_two_weeks")})
                    review_data.update({"author_last_played":
                                        review.get("author").get("last_played")})
                    review_data.pop("author")

                    if self.database.is_review_exists(
                                    review_data.get("author_steamid"),
                                    review_data.get("app_id")
                                    ):
                        self.database.update_review(review_data)
                        # print("Updated review")
                    else:
                        self.database.insert_review(review_data)
                        # print("Inserted review")
                self.database.commit()

                # * update cursor
                cursor = response.get("cursor")
                # print(cursor)
                if cursor is not None:
                    cursor = urllib.parse.quote(cursor)
                    cursors.add(cursor)
                    if number_of_cursors != len(cursors):
                        number_of_cursors = len(cursors)
                    else:
                        has_cursor = False
                else:
                    has_cursor = False

                # * sleep for 1 second to avoid rate limiting
                time.sleep(1)

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
