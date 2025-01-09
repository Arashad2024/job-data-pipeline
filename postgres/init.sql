CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    location VARCHAR(255),
    company VARCHAR(255),
    salary NUMERIC
);
