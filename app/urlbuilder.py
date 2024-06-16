"""
This module provides a class for constructing and managing URLs for the Steam user reviews scraper.
"""

import config

class URLBuilder:
    """
    This class represents a URL for the Steam user reviews scraper.
    """

    __default_url = "https://store.steampowered.com/appreviews/"

    def __init__(self):
        """
        Initializes a new instance of the URL class.

        Args:
            url (str): The URL to be constructed.
        """
        self.appid = config.APP_ID
        self.filter_param = config.FILTER
        self.language = config.LANGUAGE
        self.day_range = config.DAY_RANGE
        self.cursor = config.CURSOR
        self.review_type = config.REVIEW_TYPE
        self.purchase_type = config.PURCHASE_TYPE
        self.num_per_page = config.NUM_PER_PAGE
        self.filter_offtopic_activity = config.FILTER_OFFTOPIC_ACTIVITY

        self.build()
        self.url = self.get_url()


    def build(self) -> None:
        """
        Builds the URL based on the provided parameters.

        The URL is constructed by appending the query parameters to the base URL.
        The query parameters include the app ID, filter parameter, language, day range,
        cursor, review type, purchase type, number of reviews per page, 
        and filter off-topic activity.

        Returns:
            None
        """
        self.url = f"{self.__default_url}{self.appid}?json=1"
        if self.filter_param is not None and self.filter_param != "":
            self.url += f"&filter={self.filter_param}"
        if self.language is not None and self.language != "":
            self.url += f"&language={self.language}"
        if self.day_range is not None and self.day_range != "":
            self.url += f"&day_range={self.day_range}"
        if self.cursor is not None and self.cursor != "*":
            self.url += f"&cursor={self.cursor}"
        if self.review_type is not None and self.review_type != "":
            self.url += f"&review_type={self.review_type}"
        if self.purchase_type is not None and self.purchase_type != "":
            self.url += f"&purchase_type={self.purchase_type}"
        if self.num_per_page is not None and self.num_per_page != "":
            self.url += f"&num_per_page={self.num_per_page}"
        if self.filter_offtopic_activity is not None and self.filter_offtopic_activity != "":
            self.url += f"&filter_offtopic_activity={self.filter_offtopic_activity}"


    def get_url(self) -> str:
        """
        Returns the URL associated with the current instance.
        
        Returns:
            str: The URL associated with the current instance.
        """
        return self.url

    def set_appid(self, appid:int) -> None:
        """
        Set the appid for the Steam user reviews scraper.

        Parameters:
        appid (int): The appid to set.

        Returns:
            None
        """
        self.appid = appid

    def set_filter_param(self, filter_param: str) -> None:
        """
        Set the filter parameter for the Steam user reviews scraper.

        Args:
            filter_param (str): The filter parameter to be set.

        Returns:
            None
        """
        self.filter_param = filter_param

    def set_language(self, language:str) -> None:
        """
        Set the language for the scraper.

        Parameters:
        language (str): The language to set for the scraper.

        Returns:
            None
        """
        self.language = language

    def set_day_range(self, day_range: str) -> None:
        """
        Sets the day range for scraping user reviews.

        Parameters:
        day_range (str): The day range to be set.

        Returns:
            None
        """
        self.day_range = day_range


    def set_cursor(self, cursor:str) -> None:
        """
        Sets the cursor value for the scraper.

        Parameters:
        cursor (str): The cursor value to be set.

        Returns:
            None
        """
        self.cursor = cursor

    def set_review_type(self, review_type: str) -> None:
        """
        Set the review type for the scraper.

        Parameters:
        review_type (str): The type of review to scrape (e.g., 'positive', 'negative', 'all').

        Returns:
            None
        """
        self.review_type = review_type

    def set_purchase_type(self, purchase_type: str) -> None:
        """
        Set the purchase type for the user.

        Args:
            purchase_type (str): The purchase type to be set.

        Returns:
            None
        """
        self.purchase_type = purchase_type

    def set_num_per_page(self, num_per_page: int) -> None:
        """
        Set the number of items per page.

        Args:
            num_per_page (int): The number of items per page.

        Returns:
            None
        """
        self.num_per_page = num_per_page

    def set_filter_offtopic_activity(self, filter_offtopic_activity: int) -> None:
        """
        Set the filter for off-topic activity.

        Parameters:
        filter_offtopic_activity (int): The value to set for the filter_offtopic_activity.

        Returns:
            None
        """
        self.filter_offtopic_activity = filter_offtopic_activity
