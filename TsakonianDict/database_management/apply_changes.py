
# Imports
import sqlite3
import pandas as pd

# Connect to main database
db_path = '../db.sqlite3'
conn = sqlite3.connect(db_path)

# Auxiliary functions
def query(query: str,
        cursor = conn.cursor()):

    cursor.execute(query)
    fetched = cursor.fetchall()

    if len(fetched) > 0:
            temp_df = pd.DataFrame(fetched, columns=[i[0] for i in cursor.description])
            return temp_df
    else:
            print('Query executed successfully. No results to show.')

# Load main dictionary
main_df = pd.read_excel('../../TsakonianDB/tables/main.xlsx')

# Copy the full dictionary into the database
main_df.to_sql('dictionary_entry', 
            conn, 
            if_exists='replace', 
            index=False,
            dtype = {'tsakonian': 'varchar(50)',
                        'greek': 'varchar(200)',
                        'paradigm': 'varchar(5)',
                        'source_id': 'bigint',
            })

# Add primary keys and foreign keys by recreating the table
# Obtained from SQLiteStudio
recreating_query = """PRAGMA foreign_keys = 0;

DROP TABLE sqlitestudio_temp_table;

CREATE TABLE sqlitestudio_temp_table AS SELECT *
                                        FROM dictionary_entry;

DROP TABLE dictionary_entry;

CREATE TABLE dictionary_entry (
    tsakonian VARCHAR (50)  PRIMARY KEY
                            NOT NULL,
    greek     VARCHAR (200),
    paradigm  VARCHAR (5),
    source    INTEGER       REFERENCES dictionary_source (id) 
);

INSERT INTO dictionary_entry (
                                tsakonian,
                                greek,
                                paradigm,
                                source
                            )
                            SELECT tsakonian,
                                    greek,
                                    paradigm,
                                    source
                            FROM sqlitestudio_temp_table;

DROP TABLE sqlitestudio_temp_table;

PRAGMA foreign_keys = 1;"""

# Execute the query
for i, q in enumerate(recreating_query.split(';')):
    print(i)
    query(q)
    input(f'{i}: ')


# Do not close window
print('Changes applied successfully.')
input('Press any key to exit.')