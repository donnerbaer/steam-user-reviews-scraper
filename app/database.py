""" This module contains the Database class, which is responsible for connecting to the SQLite database and inserting data into it.
"""

import sqlite3
import config
from datetime import datetime

class Database:
    """
    A class representing a database connection.

    Attributes:
        connection (sqlite3.Connection): The connection to the SQLite database.
        cursor (sqlite3.Cursor): The cursor object for executing SQL queries.

    Methods:
        __init__: Connects to the SQLite database and initializes the connection and cursor.
        close: Closes the database connection and cursor.
        insert_app: Inserts a app into the database.
        insert_author: Inserts an author into the database.
        insert_review: Inserts a review into the database.
    """

    def __init__(self) -> None:
        """
        Connects to the SQLite database and returns the database connection and cursor.
        """
        try:
            self.connection = sqlite3.connect(config.DATABASE_PATH)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Error {e}: for connecting to {config.DATABASE_PATH}.")


    def close(self) -> None:
        """
        Closes the database connection and cursor.

        Returns:
            None
        """
        try:
            self.cursor.close()
            self.connection.close()
        except sqlite3.Error as e:
            print(f"Error {e}: for closing connection {self.connection} and cursor {self.cursor}.")


    def insert_app(self, data: tuple) -> None:
        """
        Inserts a app into the database.

        Args:
            data (tuple): A tuple containing the app data.

        Returns:
            None
        """
        try:
            self.cursor.execute("INSERT INTO app VALUES (?, ?, ?, ?)", data)
        except sqlite3.Error as e:
            print(f"Error {e}: for {data}")
        # self.connection.commit()


    def is_app_exists(self, app_id: int) -> bool:
        """
        Check if a app exists in the database for a given app ID.

        Args:
            app_id (int): The ID of the app.

        Returns:
            bool: True if a app exists, False otherwise.
        """
        self.cursor.execute("SELECT * FROM app WHERE id = ?", (app_id,))
        return self.cursor.fetchone() is not None

    def update_app_last_time_fetched(self, app_id: int, last_time_fetched: str) -> None:
        """
        Update the last time fetched for a specific app in the database.

        Args:
            app_id (int): The ID of the app to update.
            last_time_fetched (str): The last time the app was fetched.

        Returns:
            None
        """
        data = (last_time_fetched, app_id)
        try:
            self.cursor.execute("UPDATE app SET last_time_fetched = ? WHERE id = ?", data)
        except sqlite3.Error as e:
            print(f"Error {e}: for {data}")
        # self.connection.commit()

    def insert_author(self, author: dict) -> None:
        """
        Inserts author data into the database.

        Args:
            author (dict): A dictionary containing author information.

        Returns:
            None
        """
        data = (author.get("steamid"),
                author.get("num_games_owned"),
                author.get("num_reviews"),
                author.get("last_time_fetched")
                )
        try:
            self.cursor.execute("INSERT INTO author VALUES(?, ?, ?, ?);", data)
        except sqlite3.Error as e:
            print(f"Error {e}: for {data}")
        # self.connection.commit()

    def is_author_exists(self, steamid: int) -> bool:
        """
        Check if an author exists in the database for a given Steam ID.

        Args:
            steamid (int): The Steam ID of the author.

        Returns:
            bool: True if an author exists, False otherwise.
        """
        self.cursor.execute("SELECT * FROM author WHERE steamid = ?", (steamid,))
        return self.cursor.fetchone() is not None

    def update_author(self, author: dict) -> None:
        """
        Updates an author in the database.

        Args:
            author (dict): A dictonary containing the author data.

        Returns:
            None
        """
        data = (author.get("num_games_owned"),
                author.get("num_reviews"),
                author.get("last_time_fetched"),
                author.get("steamid")
                )

        try:
            self.cursor.execute("""
                                UPDATE author 
                                SET 
                                    num_games_owned = ?, 
                                    num_reviews = ?, 
                                    last_time_fetched = ? 
                                WHERE steamid = ?
                                """, data)
        except sqlite3.Error as e:
            print(f"Error {e}: for {data}")
        # self.connection.commit()



    def insert_review(self, review: dict) -> None:
        """
        Inserts a review into the database.

        Args:
            review (dict): A dictionary containing the review data.

        Returns:
            None
        """
        data: tuple = (
            review.get("author_steamid"),
            review.get("app_id"),
            review.get("comment_count"),
            review.get("hidden_in_steam_china"),
            review.get("language"),
            review.get("received_for_free"),
            review.get("recommendationid"),
            review.get("review"),
            review.get("steam_china_location"),
            review.get("steam_purchase"),
            review.get("timestamp_created"),
            review.get("timestamp_updated"),
            review.get("voted_up"),
            review.get("votes_funny"),
            review.get("votes_up"),
            review.get("weighted_vote_score"),
            review.get("written_during_early_access"),
            review.get("author_playtime_at_review"),
            review.get("author_playtime_forever"),
            review.get("author_playtime_last_two_weeks"),
            review.get("author_last_played"),
            review.get("last_time_fetched")
        )

        try:
            self.cursor.execute("""
                        INSERT INTO review
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, data)
        except sqlite3.Error as e:
            print(f"Error {e}: for {data}")
        # self.connection.commit()

    def update_review(self, review: dict) -> None:
        """
        Update a review in the database.

        Args:
            review (dict): The review data to be updated.

        Returns:
            None
        """
        data: tuple = (review.get("comment_count"),
                review.get("hidden_in_steam_china"),
                review.get("language"),
                review.get("received_for_free"),
                review.get("recommendationid"),
                review.get("review"),
                review.get("steam_china_location"),
                review.get("steam_purchase"),
                review.get("timestamp_created"),
                review.get("timestamp_updated"),
                review.get("voted_up"),
                review.get("votes_funny"),
                review.get("votes_up"),
                review.get("weighted_vote_score"),
                review.get("written_during_early_access"),
                review.get("author_playtime_at_review"),
                review.get("author_playtime_forever"),
                review.get("author_playtime_last_two_weeks"),
                review.get("author_last_played"),
                review.get("last_time_fetched")
        )
        author_steamid: str = review.get("author_steamid")
        app_id: str = review.get("app_id")
        data = data + (author_steamid, app_id)

        try:
            self.cursor.execute("""
                    UPDATE review
                    SET comment_count = ?,
                        hidden_in_steam_china = ?,
                        language = ?,
                        received_for_free = ?,
                        recommendationid = ?,
                        review = ?,
                        steam_china_location = ?,
                        steam_purchase = ?,
                        timestamp_created = ?,
                        timestamp_updated = ?,
                        voted_up = ?,
                        votes_funny = ?,
                        votes_up = ?,
                        weighted_vote_score = ?,
                        written_during_early_access = ?,
                        author_playtime_at_review = ?,
                        author_playtime_forever = ?,
                        author_playtime_last_two_weeks = ?,
                        author_last_played = ?,
                        last_time_fetched = ?
                    WHERE author_steamid = ?
                    AND app_id = ?
                    """,
                data)
        except sqlite3.Error as e:
            print(f"Error {e}: for {review}")
        # self.connection.commit()

    def is_review_exists(self, author_steamid: int, app_id: int) -> bool:
        """
        Check if a review exists in the database for a given author Steam ID and app ID.

        Args:
            author_steamid (int): The Steam ID of the author.
            app_id (int): The ID of the app.

        Returns:
            bool: True if a review exists, False otherwise.
        """
        self.cursor.execute("""SELECT * FROM review WHERE author_steamid = ? and app_id = ?""",
                            (author_steamid, app_id))
        return self.cursor.fetchone() is not None

    def get_all_app_ids(self) -> list:
        """
        Get all app IDs from the database.

        Returns:
            list: A list of app IDs.
        """
        self.cursor.execute("SELECT id FROM app")
        return [row[0] for row in self.cursor.fetchall()]

    def get_app_name_from_id(self, app_id: int) -> tuple:
        """
        Get a app from the database for a given app ID.

        Args:
            app_id (int): The ID of the app.

        Returns:
            tuple: A tuple containing the app data.
        """
        self.cursor.execute("SELECT name FROM app WHERE id = ?", (app_id,))
        return self.cursor.fetchone()

    def get_app_ids_from_name(self, app_name: str) -> list:
        """
        Get the id from the database for a given app name.

        Args:
            app_name (str): The name of the app.

        Returns:
            list: A tuple containing the app data.
        """
        self.cursor.execute('SELECT id FROM app WHERE name LIKE "%?%"', (app_name,))
        return [row[0] for row in self.cursor.fetchall()]

    def get_cursor(self) -> str:
        """
        Get the cursor from the database.

        Returns:
            str: The cursor.
        """
        return self.cursor

    def commit(self) -> None:
        """
        Commit the transaction to the database.

        Returns:
            None
        """
        self.connection.commit()
