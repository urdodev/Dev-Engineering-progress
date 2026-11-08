import sqlite3
import sys


def test_python_version():
    assert sys.version_info >= (3, 12)
    
def test_sqlite_con_ventanas():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE t (x INTEGER)")
    conn.executemany("INSERT INTO t VALUES (?)", [(1,), (2,), (3,)])
    filas = conn.execute("SELECT x, SUM(x) OVER (ORDER BY x) FROM t").fetchall()
    assert filas[-1] == (3, 6)
