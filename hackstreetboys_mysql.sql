CREATE DATABASE hackstreetdb;
use hackstreetdb;
 
CREATE TABLE news_country (
    id INT AUTO_INCREMENT PRIMARY KEY,
    article_index INT,
    country_name VARCHAR(50)
);
 
CREATE TABLE wikileaks_country (
 id INT AUTO_INCREMENT PRIMARY KEY,
    article_index INT,
    country_name VARCHAR(50)
);
 
CREATE TABLE news_organisations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    article_index INT,
    organisation_name VARCHAR(50)
);
 
CREATE TABLE wikileaks_organisations (
 id INT AUTO_INCREMENT PRIMARY KEY,
    article_index INT,
    organisation_name VARCHAR(50)
);
 
CREATE TABLE news_people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    article_index INT,
    person_name VARCHAR(50)
);
 
CREATE TABLE wikileaks_people (
 id INT AUTO_INCREMENT PRIMARY KEY,
    article_index INT,
    person_name VARCHAR(50)
);
 
 
LOAD DATA LOCAL INFILE "/Applications/MAMP/is112/news_countries.csv"
INTO TABLE hackstreetdb.news_country
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(article_index, country_name);
 
LOAD DATA LOCAL INFILE "/Applications/MAMP/is112/wikileaks_countries.csv"
INTO TABLE hackstreetdb.wikileaks_country
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(article_index, country_name);
 
LOAD DATA LOCAL INFILE "/Applications/MAMP/is112/news_organisations.csv"
INTO TABLE hackstreetdb.news_organisations
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(article_index, organisation_name);
 
LOAD DATA LOCAL INFILE "/Applications/MAMP/is112/wikileaks_organisations.csv"
INTO TABLE hackstreetdb.wikileaks_organisations
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(article_index, organisation_name);
 
LOAD DATA LOCAL INFILE "/Applications/MAMP/is112/news_persons.csv"
INTO TABLE hackstreetdb.news_people
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(article_index, person_name);
 
LOAD DATA LOCAL INFILE "/Applications/MAMP/is112/wikileaks_persons.csv"
INTO TABLE hackstreetdb.wikileaks_people
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(article_index, person_name);
