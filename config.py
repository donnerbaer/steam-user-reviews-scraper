""" Configuration file for the application.
"""

DATABASE_PATH = "database/database.db" # Path to the database file
SCHEMA_PATH = "database/schema.sql" # Path to the schema file
APPS_PATH = "data/apps.csv" # Path to the apps file

NUMBER_AUTHOR_COLUMNS = 4 # Number of columns for the author data
NUMBER_GAME_COLUMNS = 4 # Number of columns for the app data
NUMBER_REVIEWS_COLUMNS = 22 # Number of columns for the genre data

CSV_GAMES_SEPARATOR = "," # Separator used in the CSV files, default is comma

# Steam API: https://partner.steamgames.com/doc/store/getreviews
# APP_ID is required
APP_ID = ""  # replace with your app id, or leave empty to fetch from database
# CURSOR = * is used for the first page, then it will be replaced with the cursor from the response
CURSOR = "*"  # cursor to get next page, empty for first page

# use type: None or "" (empty string) for don't filter
FILTER = ""  # all, recent, updated, all_time, funny, helpful, awards
LANGUAGE = "german,english"  # replace with your language, for multiple languages use comma "german,english"
DAY_RANGE = ""  # 0, 1, 7, 30, 90, 180, max = 365
REVIEW_TYPE = ""  # all, positive, negative
PURCHASE_TYPE = ""  # all, non_steam_purchase, steam
NUM_PER_PAGE = "100"  # max 100, default 20
FILTER_OFFTOPIC_ACTIVITY = ""  # 0, 1
