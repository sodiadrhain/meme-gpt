import pymysql
import logging
from config.env import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from db.schema import USER_SCHEMA

logger = logging.getLogger(__name__)

# Database connection settings
db_config = {
    'host': DB_HOST,
    'user': DB_USER, 
    'password': DB_PASSWORD, 
    'database': DB_NAME, 
    'autocommit': True  
}

def initialize_database():
    logger.info("Connecting to database...")
    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = connection.cursor()

    logger.info("Database connected...")

    # Create the database if it doesn't exist
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')
    connection.close()

    # Reconnect to the specific database
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # CREATE TABLES HERE BY ADDING FROM SCHEMA
    # Create the users table
    cursor.execute(USER_SCHEMA)
    connection.close()

def execute(query: str, args: object = None):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query, args)
    connection.close()
    return cursor