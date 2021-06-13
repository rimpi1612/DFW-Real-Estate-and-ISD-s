-- DB Name rental_db
-- Drop table

DROP TABLE IF EXISTS isd_capita;

CREATE TABLE isd_capita (
	"year" varchar(32) NULL,
	rate int4 NULL
);

--- Use per-capita-rates.csv file to upload data in the table isd_capita
