CREATE DATABASE IF NOT EXISTS crud_api;
CREATE SCHEMA IF NOT EXISTS cars;
CREATE TABLE IF NOT EXISTS cars.cars (
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
CREATE SCHEMA IF NOT EXISTS bikes;
CREATE TABLE IF NOT EXISTS bikes.bikes (
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