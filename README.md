README.md

# ETL Weather Data

This repository contains Python code for an ETL (Extract, Transform, Load) process to retrieve, clean, and save weather data. The ETL process involves the following phases:

1. **Data Extraction**: The `get_weather` function retrieves weather data from the Open-Meteo API.

2. **Data Cleaning**: The `clean_data` function cleans the raw weather data by creating a Polars DataFrame, removing duplicates, and converting the time column to the desired format.

3. **Data Loading**: The `save_data` function saves the cleaned weather data to a database using a bulk insert operation.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/ccanasj/learn-etl.git
   cd learn-etl
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Set up the database:

   - Start the PostgreSQL database and Adminer (a web-based database management tool) using Docker Compose:

     ```shell
     docker-compose up -d
     ```

   > **_NOTE:_**
   >  - The PostgreSQL database will be accessible at **localhost:5432**
   >  - Adminer will be accessible at **localhost:8080**

4. Set up the environment variables:

   - Create a file named `.env` in the project root directory.

   - Add the following lines to the `.env` file, replacing the placeholder values with your own:

     ```plaintext
     POSTGRESQL_USER=admin_user
     POSTGRESQL_PASSWORD=super_secret_password
     POSTGRESQL_HOST=localhost
     POSTGRESQL_PORT=5432
     POSTGRESQL_DATABASE=database_name
     ```

   - Save the `.env` file.

## Usage

Run the main Python script:

```shell
python main.py
```


## License

This project is licensed under the [MIT License](LICENSE).
