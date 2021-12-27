import pandas as pd
from sqlalchemy import create_engine

data = {
        'Country': ['Belgium', 'India', 'Brazil'],
        'Capital': ['Brussels', 'New Delhi', 'Brasilia'],
        'Population': [11190846, 1303171035, 207847528]
        }

Data_Table = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])

print(Data_Table)

Data_Table_AfterRemovingColumn = Data_Table.drop ('Capital', axis=1)

print('\n')
print(Data_Table_AfterRemovingColumn)

Data_Table_Sorted = Data_Table.sort_index
print("\n")
print(Data_Table_Sorted)

Data_Table_Sorted_Values = Data_Table.sort_values(by='Country')
print('\n')
print(Data_Table_Sorted_Values)

Data_Table_Rank = Data_Table.rank()
print('\n')
print(Data_Table_Rank)

print('************************* csv **********************')


# Starting CSV File with Pandas

Read_In_Data = pd.read_csv('data.csv', header=None)
#this is so that we remove the \t that appears
Data_ReadIn_Removetabs = Read_In_Data.replace("\t", "  ", regex=True)
print (Data_ReadIn_Removetabs)
Read_In_Data.to_csv('modifieddatafile.csv')

######


# Starting sql with Pandas

engine = create_engine('sqlite:///:memory:')
Data_Table.to_sql('my_table', 
engine)
Sql_Reading = pd.read_sql("SELECT Country FROM my_table;", engine)
print(Sql_Reading)

