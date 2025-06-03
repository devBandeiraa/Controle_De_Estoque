import pyodbc

def conectar():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-K9PK1FO;'
        'DATABASE=EstoqueDB;'
        'Trusted_Connection=yes;'
    )
    return conn
