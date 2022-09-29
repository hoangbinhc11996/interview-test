-- CREATE TABLE 
CREATE TABLE EnglishVietnameseTable
(
    id INT NOT NULL PRIMARY KEY,
    text VARCHAR(4096) NOT NULL,
    audio_url VARCHAR(4096),
    translate_id INT,
    translate_text VARCHAR(4096),
);

GO

-- IMPORT data from the csv file into SQL server
BULK INSERT EnglishVietnameseTable
FROM '<path_to_the_file>/eng-viet.csv'
WITH
(
    FIRSTROW = 2, -- the first row is 2 because 1st is header
    FIELDTERMINATOR = '\t', -- csv delimeter
    ROWTERMINATOR = '\n',  -- shift the control pointer to next row
    TABLOCK
)





