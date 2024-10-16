import pyodbc
class DBPropertyUtil:
    @staticmethod
    def get_parameters():
        return {
            'Driver':'{SQL Server}',
            'host': 'Chandana\SQLEXPRESS',
            'database': 'SISDB',
            'user': 'Chandana',
            'password': 'Chandana03'
        }

class DBConnection:
    @staticmethod
    def getConnection():
        try:
            params = DBPropertyUtil.get_parameters()
            conn = pyodbc.connect(
                driver=params['Driver'],
                host=params['host'],
                database=params['database'],
                user=params['user'],
                password=params['password']
            )
            if conn:
                print('DB is connected: ')
            return conn
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None
