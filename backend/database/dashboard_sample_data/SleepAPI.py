import psycopg2

class sleep:   #sleep 엑셀 데이터 처리
    s_host = ""
    s_dbname = ""
    s_user = ""
    s_password = ""
    s_port = 0

    def create_sleeptable(self):   #create sleep table 함수
        conn = psycopg2.connect(host=self.s_host, dbname=self.s_dbname, user=self.s_user, password=self.s_password, port=self.s_port)
        curs = conn.cursor()

        mk_table = (
            'create table if not exists sleep' +
            '(' +
            'EMAIL varchar(100),' +
            'sleep_awake int,' +
            'sleep_bedtime_end varchar(100),' +
            'sleep_bedtime_start varchar(100),' +
            'sleep_breath_average float,' +
            'sleep_deep int,' +
            'sleep_duration int,' +
            'sleep_efficiency int,' +
            'sleep_hr_5min float,' +
            'sleep_hr_average float,' +
            'sleep_hr_lowest int,' +
            'sleep_hypnogram_5min float,' +
            'sleep_is_longest int,' +
            'sleep_light int,' +
            'sleep_midpoint_at_delta int,' +
            'sleep_midpoint_time int,' +
            'sleep_onset_latency int,' +
            'sleep_period_id int,' +
            'sleep_rem int,' +
            'sleep_restless int,' +
            'sleep_rmssd int,' +
            'sleep_rmssd_5min float,' +
            'sleep_score int,' +
            'sleep_score_alignment int,' +
            'sleep_score_deep int,' +
            'sleep_score_disturbances int,' +
            'sleep_score_efficiency int,' +
            'sleep_score_latency int,' +
            'sleep_score_rem int,' +
            'sleep_score_total int,' +
            'sleep_temperature_delta float,' +
            'sleep_temperature_deviation float,' +
            'sleep_total int' +
            ');'
        )
        curs.execute(mk_table)

        conn.commit()
        curs.close()
        conn.close()

    def insert_sleeptable(self, data):   #insert sleep table 함수
        conn = psycopg2.connect(host=self.s_host, dbname=self.s_dbname, user=self.s_user, password=self.s_password, port=self.s_port)
        curs = conn.cursor()

        sql = (
            'INSERT INTO sleep' +
            '(' +
            'EMAIL,' +
            'sleep_awake,' +
            'sleep_bedtime_end,' +
            'sleep_bedtime_start,' +
            'sleep_breath_average,' +
            'sleep_deep,' +
            'sleep_duration,' +
            'sleep_efficiency,' +
            'sleep_hr_5min,' +
            'sleep_hr_average,' +
            'sleep_hr_lowest,' +
            'sleep_hypnogram_5min,' +
            'sleep_is_longest,' +
            'sleep_light,' +
            'sleep_midpoint_at_delta,' +
            'sleep_midpoint_time,' +
            'sleep_onset_latency,' +
            'sleep_period_id,' +
            'sleep_rem,' +
            'sleep_restless,' +
            'sleep_rmssd,' +
            'sleep_rmssd_5min,' +
            'sleep_score,' +
            'sleep_score_alignment,' +
            'sleep_score_deep,' +
            'sleep_score_disturbances,' +
            'sleep_score_efficiency,' +
            'sleep_score_latency,' +
            'sleep_score_rem,' +
            'sleep_score_total,' +
            'sleep_temperature_delta,' +
            'sleep_temperature_deviation,' +
            'sleep_total' +
            ') ' +
            'VALUES ' +
            '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        )

        for idx in range(len(data)):
            curs.execute(sql, tuple(data.values[idx]))
        conn.commit()

        curs.close()
        conn.close()



class mmse:   #mmse 데이터 처리
    m_host = ""
    m_dbname = ""
    m_user = ""
    m_password = ""
    m_port = 0

    def create_mmsetable(self):   #create mmse table 함수
        conn = psycopg2.connect(host=self.m_host, dbname=self.m_dbname, user=self.m_user, password=self.m_password, port=self.m_port)
        curs = conn.cursor()

        mk_table = (
            'create table if not exists mmse' +
            '(' +
            'SAMPLE_EMAIL varchar(100),' +
            'DIAG_SEQ int,' +
            'DIAG_NM varchar(50),' +
            'DOCTOR_NM int,' +
            'MMSE_NUM int,' +
            'MMSE_KIND int,' +
            'Q01 int,' +
            'Q02 int,' +
            'Q03 int,' +
            'Q04 int,' +
            'Q05 int,' +
            'Q06 int,' +
            'Q07 int,' +
            'Q08 int,' +
            'Q09 int,' +
            'Q10 int,' +
            'Q11_1 int,' +
            'Q11_2 int,' +
            'Q11_3 int,' +
            'Q12_1 int,' +
            'Q12_2 int,' +
            'Q12_3 int,' +
            'Q12_4 int,' +
            'Q12_5 int,' +
            'Q12_TOTAL int,' +
            'Q13_1 int,' +
            'Q13_2 int,' +
            'Q13_3 int,' +
            'Q14_1 int,' +
            'Q14_2 int,' +
            'Q15 int,' +
            'Q16_1 int,' +
            'Q16_2 int,' +
            'Q16_3 int,' +
            'Q17 int,' +
            'Q18 int,' +
            'Q19 int,' +
            'TOTAL int' +
            ');'
        )
        curs.execute(mk_table)

        conn.commit()
        curs.close()
        conn.close()

    def insert_mmsetable(self, data):   #insert mmse 함수
        conn = psycopg2.connect(host=self.m_host, dbname=self.m_dbname, user=self.m_user, password=self.m_password, port=self.m_port)
        curs = conn.cursor()

        sql = (
            'INSERT INTO mmse' +
            '(' +
            'SAMPLE_EMAIL,' +
            'DIAG_SEQ,' +
            'DIAG_NM,' +
            'DOCTOR_NM,' +
            'MMSE_NUM,' +
            'MMSE_KIND,' +
            'Q01,' +
            'Q02,' +
            'Q03,' +
            'Q04,' +
            'Q05,' +
            'Q06,' +
            'Q07,' +
            'Q08,' +
            'Q09,' +
            'Q10,' +
            'Q11_1,' +
            'Q11_2,' +
            'Q11_3,' +
            'Q12_1,' +
            'Q12_2,' +
            'Q12_3,' +
            'Q12_4,' +
            'Q12_5,' +
            'Q12_TOTAL,' +
            'Q13_1,' +
            'Q13_2,' +
            'Q13_3,' +
            'Q14_1,' +
            'Q14_2,' +
            'Q15,' +
            'Q16_1,' +
            'Q16_2,' +
            'Q16_3,' +
            'Q17,' +
            'Q18,' +
            'Q19,' +
            'TOTAL' +
            ') ' +
            'VALUES ' +
            '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        )

        for idx in range(len(data)):
            curs.execute(sql, tuple(data.values[idx]))
        conn.commit()

        curs.close()
        conn.close()

class navijam:   #데이터 가공 및 그래프 그리기 위한 테이블 설계
    n_host = ""
    n_dbname = ""
    n_user = ""
    n_password = ""
    n_port = 0

    def create_processing_table(self):   #데이터 1차 가공, create processing table
        conn = psycopg2.connect(host=self.n_host, dbname=self.n_dbname, user=self.n_user, password=self.n_password, port=self.n_port)
        curs = conn.cursor()

        mk_table = (
                'create table if not exists processing' +
                '(' +
                'EMAIL varchar(100),' +
                'diag_nm varchar(50),' +
                'duravg float,' +
                'efficiency float,' +
                'durstd float,' +
                'sleep_score float'
                ');'
        )
        curs.execute(mk_table)

        conn.commit()
        curs.close()
        conn.close()

    def data_processing(self):   #데이터 1차 가공, insert processing table
        conn = psycopg2.connect(host=self.n_host, dbname=self.n_dbname, user=self.n_user, password=self.n_password, port=self.n_port)
        curs = conn.cursor()

        sql = ('insert into processing select EMAIL, diag_nm, durAVG, efficiency, durSTD, sleep_score from mmse inner join' +
               '(select EMAIL, avg(sleep_duration)/60/60 as durAVG, avg(sleep_efficiency) as efficiency,' +
               'STDDEV(sleep_duration) as durSTD, avg(sleep_score) as sleep_score from sleep group by email) as AvgSleep ' +
               'on AvgSleep.EMAIL = mmse.SAMPLE_EMAIL ;')

        curs.execute(sql)
        conn.commit()

        curs.close()
        conn.close()



    def sleep_time_graph_table(self):   #치매, 평균 수면 시간 테이블
        conn = psycopg2.connect(host=self.n_host, dbname=self.n_dbname, user=self.n_user, password=self.n_password, port=self.n_port)
        curs = conn.cursor()

        sql = ('select diag_nm, sum(case when durAVG<7 then 1 else 0 end) as "7시간 미만", ' +
               'sum(case when durAVG>=7 and durAVG<9 then 1 else 0 end) as "9시간 미만", ' +
               'sum(case when durAVG>=9 then 1 else 0 end) as "9시간 이상" from processing group by diag_nm;')

        curs.execute(sql)
        result = curs.fetchall()   #읽어온 데이터 딕셔너리 변환
        conn.commit()

        curs.close()
        conn.close()
        return result

    def sleep_score_graph_table(self):   #치매, 수면 종합 점수 테이블
        conn = psycopg2.connect(host=self.n_host, dbname=self.n_dbname, user=self.n_user, password=self.n_password, port=self.n_port)
        curs = conn.cursor()

        sql = ('select diag_nm, sum(case when sleep_score>=50 and sleep_score<60 then 1 else 0 end) as "50~59점", '
               'sum(case when sleep_score>=60 and sleep_score<70 then 1 else 0 end) as "60~69점", '
               'sum(case when sleep_score>=70 and sleep_score<80 then 1 else 0 end) as "70~79점", '
               'sum(case when sleep_score>=80 and sleep_score<90 then 1 else 0 end) as "80~89점", '
               'sum(case when sleep_score>=90 then 1 else 0 end) as "90~100점" from processing group by diag_nm;')

        curs.execute(sql)
        result = curs.fetchall()   #읽어온 데이터 딕셔너리 변환
        conn.commit()

        curs.close()
        conn.close()
        return result