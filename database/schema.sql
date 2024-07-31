/*
* This file contains the DDL for the database.
*/

-- DROP TABLE IF EXISTS "author";
-- DROP TABLE IF EXISTS "app";
-- DROP TABLE IF EXISTS "review";


/*
* This table contains the user information.
* The steam_id is the primary key.
*/
CREATE TABLE "author"(
    "steamid" integer NOT NULL,
    "num_games_owned" integer,
    "num_reviews" integer,
    "last_time_fetched" varchar(255),
    PRIMARY KEY("steamid")
);

-- INSERT INTO author VALUES(?, ?, ?, ?);

/*
* This table contains the game information.
* The id is the primary key.
*/
CREATE TABLE "app" (
    "id" integer NOT NULL,
    "name" varchar(255) NOT NULL,
    "shop_url" varchar(255) DEFAULT NULL,
    "last_time_fetched" varchar(255),
    PRIMARY KEY("id")
);

-- INSERT INTO app VALUES(?, ?, ?, ?);

/*
* This table is a many-to-many relationship between the author and game tables.
* The review table has a composite primary key of author_steamid and game_id.
*/
CREATE TABLE "review" (
    "author_steamid" integer NOT NULL, 
    "app_id" integer NOT NULL,
    "comment_count" integer,
    "hidden_in_steam_china" boolean,
    "language" varchar(255),
    "received_for_free" boolean,
    "recommendationid" integer,
    "review" text,
    "steam_china_location" varchar(255),
    "steam_purchase" boolean,
    "timestamp_created" integer,
    "timestamp_updated" integer,
    "voted_up" boolean,
    "votes_funny" integer,
    "votes_up" integer,
    "weighted_vote_score" real,
    "written_during_early_access" boolean,
    "author_playtime_at_review" integer,
    "author_playtime_forever" integer,
    "author_playtime_last_two_weeks" integer,
    "author_last_played" integer,
    "developer_response" text,
    "timestamp_dev_responded" text,
    "last_time_fetched" varchar(255),
    PRIMARY KEY("author_steamid", "app_id"),
    FOREIGN KEY("author_steamid") REFERENCES "author"("steamid"),
    FOREIGN KEY("app_id") REFERENCES "app"("id")
);

-- INSERT INTO review VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);