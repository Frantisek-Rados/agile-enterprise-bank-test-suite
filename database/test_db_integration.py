import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'bank_test.db')

def test_transaction_saved():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Vyčistenie pred testom
    cursor.execute("DELETE FROM trans WHERE amount = 99.99")
    conn.commit()
    
    # Vloženie testovacej transakcie
    cursor.execute("""
        INSERT INTO trans (from_account_id, to_account_id, amount, status, description)
        VALUES (1, 2, 99.99, 'pending', 'Test z DB integracneho testu')
    """)
    conn.commit()
    
    # Overenie
    cursor.execute("SELECT COUNT(*) FROM trans WHERE amount = 99.99")
    count = cursor.fetchone()[0]
    conn.close()
    
    assert count == 1, f"Očakával som 1 transakciu, ale našiel som {count}"