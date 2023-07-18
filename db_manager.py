"""
Database Manager

Author: Ibrahim Oweidat
"""
import pyodbc

class DB:
    """
    Database class

    """

    def __init__(self):
        """
        Initialize a new instance of DB.

        Args:
            None

        Returns:
            None
        """
        try:
            self.__conn = None
            self.connect()
        except Exception as ex:
            print(f"{__file__} - __init__() Error: {ex}")

    def connect(self):
        """
        Connect to the database

        Args:
            None

        Returns:
            None
        """
        try:
            # Set up connection parameters
            server = 'server name'
            database = 'database name'
            driver = '{ODBC Driver 17 for SQL Server}'

            # Connect to the database using Windows authentication
            self.__conn = pyodbc.connect(f'DRIVER={driver};'
                                f'SERVER={server};'
                                f'DATABASE={database};'
                                'Trusted_Connection=yes;')
        except Exception as ex:
            print(f"{__file__} - connect() Error: {ex}")

    def disconnect(self):
        """
        Disconnect the db connection

        Args:
            None

        Returns:
            None
        """
        try:
            if self.__conn is not None:
                self.__conn.close()
        except Exception as ex:
            print(f"{__file__} - disconnect() Error: {ex}")

    def check_user(self, username, password):
        """
        check login user

        Args:
            username
            password

        Returns:
            one user with details
        """
        result = None
        cursor = None
        try:
            # Create a cursor object
            cursor = self.__conn.cursor()

            # Execute a query
            cursor.execute(f"SELECT * FROM Users where UserName = '{username}' \
                           and Password = '{password}'")

            # Fetch the results
            result = cursor.fetchone()

        except Exception as ex:
            print(f"{__file__} - check_user() Error: {ex}")
        finally:
            # Close cursor
            if cursor:
                cursor.close()

        return result

    def update_first_login(self, user_id):
        """
        Update FirstLogin field for the first time

        Args:
            user_id: user id primary key

        Returns:
            None
        """
        cursor = None
        try:
            # Create a cursor object
            cursor = self.__conn.cursor()

            # Execute update query
            cursor.execute(f"UPDATE Users SET FirstLogin = GETDATE() WHERE ID = {user_id}")

            # Commit changes
            self.__conn.commit()
        except Exception as ex:
            print(f"{__file__} - update_first_login() Error: {ex}")
        finally:
            # Close cursor
            if cursor:
                cursor.close()

    def update_last_login(self, user_id):
        """
        Update LastLogin field after login

        Args:
            user_id: user id primary key

        Returns:
            None
        """
        cursor = None
        try:
            # Create a cursor object
            cursor = self.__conn.cursor()

            # Execute update query
            cursor.execute(f"UPDATE Users SET LastLogin = GETDATE() WHERE ID = {user_id}")

            # Commit changes
            self.__conn.commit()
        except Exception as ex:
            print(f"{__file__} - update_last_login() Error: {ex}")
        finally:
            # Close cursor
            if cursor:
                cursor.close()

    def get_customers(self):
        """
        Get all customers with details

        Args:
            None

        Returns:
            List of customers
        """
        results = None
        cursor = None
        try:
            # Create a cursor object
            cursor = self.__conn.cursor()

            # Execute update query
            cursor.execute("select * from Customer")

            # Fetch the results
            results = cursor.fetchall()
        except Exception as ex:
            print(f"{__file__} - get_customers() Error: {ex}")
        finally:
            # Close cursor
            if cursor:
                cursor.close()

        return results

    def insert_customer(self, first_name, last_name, age, marital_status, employed):
        """
        Insert new customer on db

        Args:
            first_name
            last_name
            age
            marital_status
            employed
        Returns:
            None
        """
        cursor = None
        try:
            # Create a cursor object
            cursor = self.__conn.cursor()

            # Execute update query
            cursor.execute(f"insert into Customer values('{first_name}', '{last_name}', {age}, '{marital_status}', {employed})")

            # Commit changes
            self.__conn.commit()

        except Exception as ex:
            print(f"{__file__} - insert_customer() Error: {ex}")
        finally:
            # Close cursor
            if cursor:
                cursor.close()

    def update_customer(self, cus_id, first_name, last_name, age, marital_status, employed):
        """
        Update customer on db

        Args:
            cus_id: Customer ID
            first_name
            last_name
            age
            marital_status
            employed
        Returns:
            None
        """
        cursor = None
        try:
            # Create a cursor object
            cursor = self.__conn.cursor()

            # Execute update query
            cursor.execute(f"UPDATE Customer SET FirstName = '{first_name}', \
                           LastName = '{last_name}', Age = {age}, \
                            MaritalStatus = '{marital_status}', \
                                Employed = {employed} \
                                    WHERE ID = {cus_id}")

            # Commit changes
            self.__conn.commit()

        except Exception as ex:
            print(f"{__file__} - update_customer() Error: {ex}")
        finally:
            # Close cursor
            if cursor:
                cursor.close()
