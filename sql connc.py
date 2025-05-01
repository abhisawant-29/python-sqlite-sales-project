#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3

# Create (or reset) the database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Drop the table if exists (clean start)
cursor.execute('DROP TABLE IF EXISTS sales')

# Create sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Grocery sale Data
sample_data = [
    # Rice transactions
    ('Rice', 100, 40.0),
    ('Rice', 120, 42.0),
    ('Rice', 90, 41.5),
    ('Rice', 150, 43.0),

    # Wheat transactions
    ('Wheat', 80, 30.0),
    ('Wheat', 90, 32.0),
    ('Wheat', 75, 31.0),
    ('Wheat', 100, 33.5),

    # Sugar transactions
    ('Sugar', 60, 35.0),
    ('Sugar', 70, 36.0),
    ('Sugar', 50, 34.5),
    ('Sugar', 80, 37.0),

    # Tea transactions
    ('Tea', 40, 150.0),
    ('Tea', 50, 155.0),
    ('Tea', 30, 152.0),
    ('Tea', 45, 158.0),

    # Coffee transactions
    ('Coffee', 30, 200.0),
    ('Coffee', 25, 210.0),
    ('Coffee', 35, 205.0),
    ('Coffee', 40, 215.0),

    # New Products
    ('Dal', 60, 90.0),
    ('Dal', 80, 95.0),
    ('Oil', 20, 120.0),
    ('Oil', 25, 125.0),
    ('Salt', 100, 15.0),
    ('Salt', 120, 16.0),
    ('Spices', 15, 250.0),
    ('Spices', 20, 270.0),
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)

# Commit and close
conn.commit()
conn.close()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Connect to DB
conn = sqlite3.connect('sales_data.db')

# Query
query = '''
    SELECT 
        product, 
        SUM(quantity) AS total_quantity,
        SUM(quantity * price) AS total_revenue
    FROM sales
    GROUP BY product
'''
df = pd.read_sql_query(query, conn)

conn.close()

# Print results
print(df)

# Bar Chart
plt.figure(figsize=(10,6))
plt.bar(df['product'], df['total_revenue'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Revenue (INR)')
plt.title('Total Revenue per Product in India (Expanded Data)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:




