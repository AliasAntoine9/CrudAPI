CREATE TABLE IF NOT EXISTS cars (
    id INTEGER AUTO_INCREMENT,
    make VARCHAR(200),
    model VARCHAR(200),
    body_style VARCHAR(200),
    production_years VARCHAR(200),
    horse_power INTEGER,
    weight_kg INTEGER,
    engine VARCHAR(200),
    engine_size VARCHAR(200)
);

INSERT INTO cars
VALUES
    (1,'ferari','modena','2 doors berlinetta','1999-2005',400,1290,'Tipo F131 V8','3.6L'),
    (2,'honda','S2000','2 doors convertible','1999-2009',240,1285,'VTEC F20C','2.0L');