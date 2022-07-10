from SleepAPI import *
import pandas as pd

#sleep table
s = sleep()
s.s_host = "localhost"
s.s_dbname = "postgres"
s.s_user = "postgres"
s.s_password = "postgres"
s.s_port = 5432

s.create_sleeptable()
data = pd.read_excel("./sample_sleep.xlsx")
s.insert_sleeptable(data)

#mmse table
m = mmse()
m.m_host = "localhost"
m.m_dbname = "postgres"
m.m_user = "postgres"
m.m_password = "postgres"
m.m_port = 5432

m.create_mmsetable()
data = pd.read_excel("./sample_mmse.xlsx")
m.insert_mmsetable(data)

#processing table
n = navijam()
n.n_host = "localhost"
n.n_dbname = "postgres"
n.n_user = "postgres"
n.n_password = "postgres"
n.n_port = 5432

n.create_processing_table()
n.data_processing()

#processing table에서 원하는 데이터 추출
data = n.sleep_time_graph_table()
df = pd.DataFrame(data)   #딕셔너리 데이터프레임으로 변환
print(df)

data2 = n.sleep_score_graph_table()
df2 = pd.DataFrame(data2)   #딕셔너리 데이터프레임으로 변환
print(df2)