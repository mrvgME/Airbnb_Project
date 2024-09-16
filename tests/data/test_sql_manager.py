import unittest
from src.data.sql_manager import SQLManager


class TestSQLManager(unittest.TestCase):

    def test_create_table(self):
        """
        Check if create table works.
        """

        # Create test table
        SQL_obj = SQLManager("postgres", "postgres", "1234", "localhost", 5432)
        SQL_obj.execute_query(
            """
            CREATE TABLE IF NOT EXISTS test_table (
            id INT PRIMARY KEY,
            name VARCHAR(255)
            );
            """
        )
        SQL_obj.commit_changes()

        # Get table names
        SQL_obj.execute_query(
            """
            SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public';
            """
        )

        tables = SQL_obj.cur.fetchall()
        self.assertTrue(("test_table",) in tables)

        SQL_obj.close_session()
