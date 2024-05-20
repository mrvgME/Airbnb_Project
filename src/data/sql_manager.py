
import pandas as pd
import psycopg2
import psycopg2.extras as extras


class SQLManager():

    def __init__(self, database: str, user: str, password: str, host: str, port: int):
        """
        Create connection to postgresql database. Create cursor too.

        Parameters:
            database: database name.
            user: username.
            password: credential.
            host: host name.
            port: port service.
        """

        self.conn = psycopg2.connect(
            database = database,
            user = user,
            password = password,
            host = host,
            port = port,
        )

        self.cur = self.conn.cursor()

    def execute_query(self, query: str):
        """
        Execute SQL query.

        Parameter:
            query: SQL query.
        """

        self.cur.execute(query)
        # return self.cur.fetchone()

    def insert_dataframe(self, df: pd.DataFrame, table: str):
        """
        Insert pandas dataframe to postgresql table.

        Parameters:
            df: pandas dataframe.
            table: table name from database.
        """

        # Fill pandas NaN with NULL
        df = df.fillna(psycopg2.extensions.AsIs('NULL'))

        # Dataframe rows and cols
        rows = [tuple(x) for x in df.to_numpy()] 
        cols = ','.join(list(df.columns)) 

        # SQL query to execute 
        query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)

        try: 
            extras.execute_values(self.cur, query, rows) 
            self.commit_changes()
        except (Exception, psycopg2.DatabaseError) as error: 
            print("Error: %s" % error) 
            self.conn.rollback() 
            self.close_session()
            return 1
        
        print("the dataframe is inserted") 

    def commit_changes(self):
        """
        Make databases changes persistent.
        """

        self.conn.commit()

    def close_session(self):
        """
        Close connection.
        """

        self.cur.close()
        self.conn.close()

     