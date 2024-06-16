# Steam Review Scraper

A script for scraping user reviews from the gaming platform "Steam".

Steam Review API: [Documentation](https://partner.steamapps.com/doc/store/getreviews)

## Setup

Install the required libraries:

```bash
pip install sqlite3
pip install requests
```


# Create Database
Run the following script to create the database:

```bash
python create_database.py
```


# Insert Games

You can import your data from `data/apps.csv` or manually insert data into the apps table using a tool like `DB Browser for SQLite`.

```bash
python insert_apps.py
``` 

For help use:
```bash
python insert_apps.py --help
```

# Fetch Steam User Reviews
Run the following script to fetch user reviews:

```bash
python main.py`
```

For help use:
```bash
python main.py --help
```


# Database

Your database will be saved by default in `database/database.db`.




# Questions
...