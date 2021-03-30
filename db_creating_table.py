import psycopg2
from insert_into_tl_security import *
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from argparse import ArgumentParser

def connect_to_database(dbname):
    try:
        connection = psycopg2.connect(user='postgres',
                                        password='***',
                                        host='127.0.0.1',
                                        port='5432',
                                        dbname=dbname)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return connection
    except Error as error:
        print(error)

def copy_data_from_csv(input_file, cursor):
    sql_table_create = '''CREATE TABLE lykkedataimport_tmp
                            (
                                tradedate character varying(254),
                                tradeid character varying(254),
                                asset character varying(254),
                                direction character varying(254),
                                volume character varying(254),
                                ordertype character varying(254),
                                orderid character varying(254),
                                orderdate character varying(254),
                                walletid character varying(254)
                            ); '''
    cursor.execute(sql_table_create)

    with open(input_file, 'r') as f_input:
        next(f_input)
        cursor.copy_from(f_input, 'lykkedataimport_tmp', sep=';')

def create_seq(cursor):
    sql_create_seq = '''CREATE SEQUENCE public.table_id_seq
                        INCREMENT 1
                        START 4968
                        MINVALUE 1
                        MAXVALUE 9223372036854775807
                        CACHE 1;
                        
                        CREATE SEQUENCE public.seq_security_id
                        INCREMENT 1
                        START 17383020
                        MINVALUE 1
                        MAXVALUE 2147483647
                        CACHE 1;

                        CREATE SEQUENCE public.agents_trade_test_id_seq
                        INCREMENT 1
                        START 5376613
                        MINVALUE 1
                        MAXVALUE 2147483647
                        CACHE 1;
                        '''

    cursor.execute(sql_create_seq)

def create_lykkedataimport(cursor):
    sql_table_create = '''CREATE TABLE lykkedataimport
                            (
                                tradedate date,
                                tradetime character varying(254),
                                tradeid character varying(254),
                                asset character varying(254),
                                direction character varying(254),
                                volume numeric,
                                ordertype character varying(254),
                                orderid character varying(254),
                                orderdate date,
                                ordertime character varying(254),
                                walletid character varying(254)
                            ); '''
    cursor.execute(sql_table_create)

def insert_into_lykkedataimport(cursor):
    sql_insert_query = '''insert into lykkedataimport (TRADEDATE,TRADETIME,TRADEID,ASSET,DIRECTION,
                            VOLUME,ORDERTYPE,ORDERID,ORDERDATE,ORDERTIME,WALLETID)
                            select 
                            to_date(substr(TRADEDATE,1,10), 'yyyy-mm-dd') as TRADEDATE,
                            substr(TRADEDATE,12,length(tradedate)) as TRADETIME,
                            TRADEID,ASSET,DIRECTION,
                            cast(VOLUME as numeric),ORDERTYPE,ORDERID,
                            case when length(orderdate) = 27 then to_date(substr(ORDERDATE,1,10), 'yyyy-mm-dd') else to_date(substr(TRADEDATE,1,10), 'yyyy-mm-dd') end as ORDERDATE,
                            case when length(orderdate) = 27 then substr(ORDERDATE,12,length(ORDERDATE)) else substr(TRADEDATE,12,length(tradedate)) end as ORDERTIME,
                            WALLETID from lykkedataimport_tmp;
                        '''
    cursor.execute(sql_insert_query)

def update_asset_names(cursor):
    sql_update_query = '''update LYKKEDATAIMPORT set ASSET = 'LTC' where ASSET = 'LiteCoin';
                            update LYKKEDATAIMPORT set ASSET = 'EOS' where ASSET = 'Eos';
                            update LYKKEDATAIMPORT set ASSET = 'BTS' where ASSET = 'Bitshares';
                            update LYKKEDATAIMPORT set ASSET = 'BTG' where ASSET = 'BitcoinGold';
                            update LYKKEDATAIMPORT set ASSET = 'STEEM' where ASSET = 'Steem'; --two new sec
                            update LYKKEDATAIMPORT set ASSET = 'APPC' where ASSET = 'AppCoins';
                            update LYKKEDATAIMPORT set ASSET = 'GCP' where ASSET = 'GCPcoin';
                            update LYKKEDATAIMPORT set ASSET = 'HGT' where ASSET = 'HelloGold';
                            update LYKKEDATAIMPORT set ASSET = 'NEO' where ASSET = 'Neo';
                        '''
    cursor.execute(sql_update_query)

def create_tl_currency(cursor):
    sql_table_create = '''CREATE TABLE tl_currency
                            (
                                currency_id numeric NOT NULL,
                                isoident character varying(32) NOT NULL,
                                name character varying(256) NOT NULL,
                                shortname character varying(32),
                                decimals numeric
                            );'''
    cursor.execute(sql_table_create)

def insert_into_tl_currency(cursor):
    sql_insert_query = 'insert into tl_currency (CURRENCY_ID, ISOIDENT, NAME, SHORTNAME, DECIMALS) values(%s, %s, %s, %s, %s);'

    values_list = [(889, 'EUR', 'EUR', 'EUR', 8,),
    (890, 'LKK1Y', 'LKK1Y', 'LKK1Y', 8,),
    (891, 'ZAR', 'ZAR', 'ZAR', 8,),
    (892, 'PLN', 'PLN', 'PLN', 8,),
    (893, 'RUB', 'RUB', 'RUB', 8,),
    (894, 'TRY', 'TRY', 'TRY', 8,),
    (895, 'NZD', 'NZD', 'NZD', 8,),
    (896, 'SEK', 'SEK', 'SEK', 8,),
    (897, 'GBP', 'GBP', 'GBP', 8,),
    (898, 'JPY', 'JPY', 'JPY', 8,),
    (899, 'BTC', 'BTC', 'BTC', 8,),
    (900, 'LKK', 'LKK', 'LKK', 8,),
    (901, 'CZK', 'CZK', 'CZK', 8,),
    (902, 'HUF', 'HUF', 'HUF', 8,),
    (903, 'ILS', 'ILS', 'ILS', 8,),
    (904, 'NOK', 'NOK', 'NOK', 8,),
    (905, 'SGD', 'SGD', 'SGD', 8,),
    (906, 'CHF', 'CHF', 'CHF', 8,),
    (907, 'DKK', 'DKK', 'DKK', 8,),
    (908, 'HKD', 'HKD', 'HKD', 8,),
    (909, 'ETH', 'ETH', 'ETH', 8,),
    (910, 'USD', 'USD', 'USD', 8,),
    (911, 'CAD', 'CAD', 'CAD', 8,),
    (912, 'MXN', 'MXN', 'MXN', 8,)]
    cursor.executemany(sql_insert_query, values_list)

def create_tl_security(cursor):
    sql_table_create = '''CREATE TABLE public.tl_security
                        (
                            security_id numeric NOT NULL,
                            board_id numeric(12,0) NOT NULL,
                            ticker character varying(32),
                            shortname character varying(256),
                            name character varying(256),
                            facevalue numeric,
                            isin character varying(16),
                            issuedate date,
                            createdate date NOT NULL DEFAULT CURRENT_DATE,
                            creator_id numeric(12,0) NOT NULL,
                            issuesize numeric,
                            exchange_id numeric(12,0) NOT NULL,
                            securitytype_id numeric(12,0),
                            issuer_id numeric(12,0),
                            currency_id numeric(12,0),
                            regno character varying(64),
                            sec_grp_id numeric(12,0),
                            lotsize numeric,
                            deliverydate date,
                            strikeprice numeric,
                            optiontype_id numeric(12,0),
                            ident character varying(32),
                            settle_code character varying(32),
                            instr_id character varying(12),
                            marketsegmentid numeric,
                            actualdate date NOT NULL,
                            fut_type numeric,
                            inputdate date,
                            maturity_date date
                        );'''
    cursor.execute(sql_table_create)

def create_tl_agent(cursor):
    sql_table_create = '''CREATE TABLE public.tl_agent
                        (
                            agent_id numeric NOT NULL DEFAULT nextval('table_id_seq'::regclass),
                            ident character varying(250) COLLATE pg_catalog."default" NOT NULL,
                            broker_id numeric,
                            exchange_id numeric(9,0),
                            agenttype character varying(15) COLLATE pg_catalog."default" NOT NULL,
                            name character varying(250) COLLATE pg_catalog."default" NOT NULL,
                            details character varying(250) COLLATE pg_catalog."default",
                            subdetails character varying(250) COLLATE pg_catalog."default",
                            createdate date NOT NULL DEFAULT CURRENT_DATE,
                            creator_id numeric(12,0) NOT NULL DEFAULT NULL::numeric,
                            clientcode character varying(250) COLLATE pg_catalog."default",
                            is_resident character(1) COLLATE pg_catalog."default" NOT NULL DEFAULT 'Y'::bpchar,
                            marker_count numeric(9,0) DEFAULT 0,
                            descr character varying(4000) COLLATE pg_catalog."default",
                            is_creditorg character(1) COLLATE pg_catalog."default" DEFAULT NULL::bpchar,
                            countrycode character varying(3) COLLATE pg_catalog."default",
                            crossdeals character varying(1) COLLATE pg_catalog."default",
                            indinvcount character varying(1) COLLATE pg_catalog."default",
                            subject_id numeric(12,0),
                            status character varying(1) COLLATE pg_catalog."default",
                            date_status date,
                            open_time date,
                            close_time date,
                            type_cd integer,
                            agg_name character varying(250) COLLATE pg_catalog."default",
                            agg_by_broker_id numeric,
                            agg_by_agent_id numeric,
                            investigation_count numeric NOT NULL DEFAULT 0,
                            offender_count numeric NOT NULL DEFAULT 0
                        ); '''
    cursor.execute(sql_table_create)

def insert_into_tl_agents(cursor):
    sql_insert_query = '''INSERT INTO TL_AGENT (
                        IDENT, BROKER_ID,
                        EXCHANGE_ID, AGENTTYPE, NAME, 
                        DETAILS, SUBDETAILS, CREATEDATE, 
                        CREATOR_ID, CLIENTCODE, IS_RESIDENT, 
                        MARKER_COUNT, DESCR, IS_CREDITORG, 
                        COUNTRYCODE, CROSSDEALS, INDINVCOUNT, 
                        SUBJECT_ID, STATUS, DATE_STATUS, 
                        OPEN_TIME, CLOSE_TIME, TYPE_CD, 
                        AGG_NAME, AGG_BY_BROKER_ID, AGG_BY_AGENT_ID, 
                        INVESTIGATION_COUNT, OFFENDER_COUNT) 
                        select a.walletid,
                            null,
                            1010,
                            'null',
                            a.walletid,
                            a.walletid,
                            a.walletid,
                            current_date,
                            105,
                            null,
                            0,
                            null,
                            'System record',
                            null,
                            null,
                            null,
                            null,
                            null,
                            null,
                            null,
                            null,
                            null,
                            null,
                            null,
                            null,
                            null,
                            0,
                            0
                        from (select distinct walletid 
                        from lykkedataimport l 
                        where not exists (select null 
                                            from tl_agent b 
                                            where  l.walletid=b.details)) a; '''
    cursor.execute(sql_insert_query)

def create_stg_lykkedataimport(cursor):
    sql_table_create = '''CREATE TABLE stg_lykkedataimport
                        (
                            security_id character varying(509),
                            tradedate date,
                            tradetime timestamp(6) without time zone,
                            tradeid character varying(254),
                            agent_id character varying(254),
                            buysell character(1),
                            price numeric,
                            volume numeric,
                            value numeric,
                            orderno character varying(254),
                            ordertime timestamp(6) without time zone,
                            orderprice numeric,
                            ordervolume numeric,
                            ordtype character varying(254),
                            cp_agent_id character varying(254),
                            cp_orderno character varying(254),
                            cp_ordertime timestamp(6) without time zone,
                            cp_orderprice numeric,
                            cp_ordervolume numeric,
                            cp_ordtype character varying(254));'''
    cursor.execute(sql_table_create)

def insert_into_stg_lykkedataimport(cursor):
    sql_insert_query = '''insert into stg_lykkedataimport
                            select b.asset||'/'||a.asset as security_id,
                            a.tradedate as tradedate, 
                            TO_TIMESTAMP(to_char(a.tradedate,'dd.mm.yyyy')||' '||a.tradetime,' dd.mm.yyyyhh24:mi:ss,FF9') as TRADETIME, 
                            a.tradeId as tradeid, 
                            a.walletid as Agent_ID, 
                            'S' as BUYSELL,  
                            a.volume/b.volume as PRICE, 
                            b.volume as VOLUME, 
                            a.volume as VALUE,
                            a.orderid as ORDERNO,
                            TO_TIMESTAMP(to_char(a.orderdate,'dd.mm.yyyy')||' '||a.ordertime,' dd.mm.yyyyhh24:mi:ss,FF9') as ORDERTIME, 
                            a.volume/b.volume as orderprice,
                            
                            b.volume as ordervolume, 
                            a.ordertype as OrdType, 
                            b.walletid as CP_AGENT_ID,
                            b.orderid as CP_ORDERNO,
                            TO_TIMESTAMP(to_char(b.orderdate,'dd.mm.yyyy')||' '||b.ordertime,' dd.mm.yyyyhh24:mi:ss,FF9') as CP_ORDERTIME,
                            a.volume/b.volume as CP_orderprice,
                            
                            b.volume as CP_ordervolume,
                            b.ordertype as CP_OrdType
                    from lykkedataimport a,
                            lykkedataimport b
                    where a.tradedate=b.tradedate  
                        and a.tradetime=b.tradetime
                        and a.tradeId=b.tradeID
                        and a.walletid<>b.walletid
                        and a.direction='Buy' and b.direction='Buy' 
                    
                    union all
                    select a.asset||'/'||b.asset as security, 
                            b.tradedate as tradedate, 
                            TO_TIMESTAMP(to_char(b.tradedate,'dd.mm.yyyy')||' '||b.tradetime,' dd.mm.yyyyhh24:mi:ss,FF9') as TRADETIME, 
                            b.tradeId as tradeid, 
                            b.walletid as Agent_ID, 
                            'B' as BUYSELL,  
                            
                            b.volume/a.volume as PRICE, 
                            a.volume as VOLUME,
                            b.volume as VALUE,
                            b.orderid as ORDERNO,
                            TO_TIMESTAMP(to_char(b.orderdate,'dd.mm.yyyy')||' '||b.ordertime,' dd.mm.yyyyhh24:mi:ss,FF9') as ORDERTIME, 
                            b.volume/a.volume as orderprice,
                            a.volume as ordervolume,
                            b.ordertype as OrdType, 
                            a.walletid as CP_AGENT_ID,
                            a.orderid as CP_ORDERNO,
                            TO_TIMESTAMP(to_char(a.orderdate,'dd.mm.yyyy')||' '||a.ordertime,' dd.mm.yyyyhh24:mi:ss,FF9') as CP_ORDERTIME,
                            b.volume/a.volume as CP_orderprice,

                            a.volume  as CP_ordervolume,
                            a.ordertype as CP_OrdType
                    from lykkedataimport a,
                            lykkedataimport b
                    where a.tradedate=b.tradedate  
                        and a.tradetime=b.tradetime
                        and a.tradeId=b.tradeID
                        and a.walletid<>b.walletid
                        and a.direction='Sell' and b.direction='Sell'
                    
                    order by tradedate, tradetime; '''

    cursor.execute(sql_insert_query)

def create_agents_trade(cursor):
    sql_table_create = '''CREATE TABLE agents_trade
                        (
                            security_id character varying(509),
                            tradedate date,
                            tradetime timestamp(6) without time zone,
                            tradeid character varying(254),
                            agent_id character varying(254),
                            buysell character(1),
                            price numeric,
                            buyvolume numeric,
                            sellvolume numeric,
                            value numeric,
                            orderno character varying(254),
                            ordertime timestamp(6) without time zone,
                            orderprice numeric,
                            ordervolume numeric,
                            ordtype character varying(254),
                            cp_agent_id character varying(254),
                            cp_orderno character varying(254),
                            cp_ordertime timestamp(6) without time zone,
                            cp_orderprice numeric,
                            cp_ordervolume numeric,
                            cp_ordtype character varying(254),
                            totalvolume numeric
                        ); '''

    cursor.execute(sql_table_create)

def insert_agents_trade(cursor):
    sql_insert_query = '''insert into agents_trade
                            select 
                            security_id,
                            tradedate,
                            tradetime,
                            tradeid,
                            a.agent_id,
                            buysell,
                            price,
                            case when l.buysell like 'B' then (select distinct volume from stg_lykkedataimport s where s.tradeid = l.tradeid and buysell like 'B' and s.agent_id = l.agent_id) else null end as buyvolume,
                            case when l.buysell like 'S' then (select distinct volume from stg_lykkedataimport s where s.tradeid = l.tradeid and buysell like 'S' and s.agent_id = l.agent_id) else null end as sellvolume,
                            value,
                            orderno,
                            ordertime,
                            orderprice,
                            ordervolume,
                            ordtype,
                            c.agent_id,
                            cp_orderno,
                            cp_ordertime,
                            cp_orderprice,
                            cp_ordervolume,
                            cp_ordtype
                            from stg_lykkedataimport l, tl_agent a, tl_agent c
                            where l.agent_id = a.ident
                            and l.cp_agent_id = c.ident;'''
    cursor.execute(sql_insert_query)

def create_agents_trade_test(cursor):
    sql_table_create = '''CREATE TABLE agents_trade_test
                        (
                            id integer NOT NULL DEFAULT nextval('agents_trade_test_id_seq'::regclass),
                            security_id character varying(509),
                            tradedate date,
                            tradetime timestamp(6) without time zone,
                            tradeid character varying(254),
                            agent_id integer,
                            buyvolume numeric,
                            sellvolume numeric,
                            cp_agent_id integer,
                            CONSTRAINT agents_trade_test_pkey PRIMARY KEY (id)
                        ); '''
    cursor.execute(sql_table_create)

def insert_agents_trade_test(cursor):
    sql_insert_query = '''insert into agents_trade_test (security_id, tradedate, tradetime, tradeid, agent_id, buyvolume, sellvolume, cp_agent_id)
                        select
                        security_id,
                        tradedate,
                        tradetime,
                        tradeid,
                        cast(agent_id as integer),
                        coalesce(buyvolume, (select distinct a.buyvolume from agents_trade a where a.agent_id = ag.agent_id and a.tradeid = ag.tradeid and a.buysell like 'B' and a.cp_agent_id = ag.cp_agent_id )) as buyvolume,
                        coalesce(sellvolume, (select distinct a.sellvolume from agents_trade a where a.agent_id = ag.agent_id and a.tradeid = ag.tradeid and a.buysell like 'S' and a.cp_agent_id = ag.cp_agent_id )) as sellvolume,
                        cast(cp_agent_id as integer)
                        from agents_trade ag;'''
    cursor.execute(sql_insert_query)

def create_groups_iteration(cursor):
    sql_table_create = '''CREATE TABLE public.groups_iteration
                        (
                            groupnumber numeric,
                            iteration numeric,
                            agent_id integer,
                            cp_agent_id integer,
                            security_id character varying(509),
                            tradedate date,
                            tradetime timestamp(6) without time zone,
                            buyvolume numeric,
                            sellvolume numeric,
                            totalvolume numeric,
                            crossvolume numeric,
                            relnetposition numeric
                        ); '''
    cursor.execute(sql_table_create)

def createParser():
    parser = ArgumentParser()
    
    parser.add_argument('-d', '--database', default='lykke')
    parser.add_argument('-f', '--file_input', default='combined_csv.csv')

    return parser

def create_everything(dbname, file_input):
    connection = connect_to_database(dbname)
    cursor = connection.cursor()
    copy_data_from_csv(file_input, cursor)
    create_seq(cursor)
    create_lykkedataimport(cursor)
    insert_into_lykkedataimport(cursor)
    update_asset_names(cursor)
    create_tl_currency(cursor)
    insert_into_tl_currency(cursor)
    create_tl_security(cursor)
    insert_into_tl_security(cursor)
    create_tl_agent(cursor)
    insert_into_tl_agents(cursor)
    create_stg_lykkedataimport(cursor)
    insert_into_stg_lykkedataimport(cursor)
    create_agents_trade(cursor)
    insert_agents_trade(cursor)
    create_agents_trade_test(cursor)
    insert_agents_trade_test(cursor)
    create_groups_iteration(cursor)


    cursor.close()
    connection.close()
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    connection = connect_to_database(namespace.database)
    cursor = connection.cursor()
    copy_data_from_csv(namespace.file_input, cursor)
    create_seq(cursor)
    create_lykkedataimport(cursor)
    insert_into_lykkedataimport(cursor)
    update_asset_names(cursor)
    create_tl_currency(cursor)
    insert_into_tl_currency(cursor)
    create_tl_security(cursor)
    insert_into_tl_security(cursor)
    create_tl_agent(cursor)
    insert_into_tl_agents(cursor)
    create_stg_lykkedataimport(cursor)
    insert_into_stg_lykkedataimport(cursor)
    create_agents_trade(cursor)
    insert_agents_trade(cursor)
    create_agents_trade_test(cursor)
    insert_agents_trade_test(cursor)
    create_groups_iteration(cursor)


    cursor.close()
    connection.close()
    
