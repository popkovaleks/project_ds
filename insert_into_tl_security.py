def insert_into_tl_security(cursor):
    sql_insert_query = '''Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262973, 6685608, 'BTC', 'BTC', 'BTC', 
                            NULL, NULL, NULL, TO_DATE('01/30/2019 15:18:36', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/30/2019 15:18:36', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262974, 6685608, 'USD', 'USD', 'USD', 
                            NULL, NULL, NULL, TO_DATE('01/30/2019 15:19:05', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/30/2019 15:19:05', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262975, 6685608, 'CHF', 'CHF', 'CHF', 
                            NULL, NULL, NULL, TO_DATE('01/30/2019 15:19:57', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/30/2019 15:19:57', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262976, 6685608, 'LKK1Y', 'LKK1Y', 'LKK1Y', 
                            NULL, NULL, NULL, TO_DATE('01/30/2019 15:20:53', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/30/2019 15:20:53', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262977, 6685608, 'ETH', 'ETH', 'ETH', 
                            NULL, NULL, NULL, TO_DATE('01/30/2019 15:25:03', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/30/2019 15:25:03', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262978, 6685608, 'EUR', 'EUR', 'EUR', 
                            NULL, NULL, NULL, TO_DATE('01/30/2019 15:25:12', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/30/2019 15:25:12', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263047, 6685608, 'CAD', 'CAD', 'CAD', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263048, 6685608, 'QNTU', 'QNTU', 'QNTU', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263049, 6685608, 'MXN', 'MXN', 'MXN', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263050, 6685608, 'REQ', 'REQ', 'REQ', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263051, 1, 'BTC/USD CMC', 'BTC/USD CoinMarketCap', 'BTC/USD CoinMarketCap Indexes', 
                            NULL, NULL, NULL, TO_DATE('02/21/2019 13:43:47', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 2, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/21/2019 13:43:47', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263052, 1, 'ETH/USD CMC', 'ETH/USD CoinMarketCap', 'ETH/USD CoinMarketCap Indexes', 
                            NULL, NULL, NULL, TO_DATE('02/22/2019 00:08:12', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 2, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/22/2019 00:08:12', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262746, 6685608, 'AIONETH', 'AION/ETH', 'AION/ETH', 
                            1, 'AION/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262747, 6685608, 'AMLTBTC', 'AMLT/BTC', 'AMLT/BTC', 
                            1, 'AMLT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262748, 6685608, 'AMLTETH', 'AMLT/ETH', 'AMLT/ETH', 
                            1, 'AMLT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262749, 6685608, 'APPCBTC', 'APPC/BTC', 'APPC/BTC', 
                            1, 'APPC/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262750, 6685608, 'APPCETH', 'APPC/ETH', 'APPC/ETH', 
                            1, 'APPC/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262751, 6685608, 'AUDUSD', 'AUD/USD', 'AUD/USD', 
                            1, 'AUD/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262752, 6685608, 'BCHBTC', 'BCH/BTC', 'BCH/BTC', 
                            1, 'BCH/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262753, 6685608, 'BCHCHF', 'BCH/CHF', 'BCH/CHF', 
                            1, 'BCH/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262754, 6685608, 'BCHUSD', 'BCH/USD', 'BCH/USD', 
                            1, 'BCH/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262755, 6685608, 'BMCBTC', 'BMC/BTC', 'BMC/BTC', 
                            1, 'BMC/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262756, 6685608, 'BMCETH', 'BMC/ETH', 'BMC/ETH', 
                            1, 'BMC/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262757, 6685608, 'BNTBTC', 'BNT/BTC', 'BNT/BTC', 
                            1, 'BNT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262758, 6685608, 'BNTETH', 'BNT/ETH', 'BNT/ETH', 
                            1, 'BNT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262759, 6685608, 'BSVBTC', 'BSV/BTC', 'BSV/BTC', 
                            1, 'BSV/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262760, 6685608, 'BSVUSD', 'BSV/USD', 'BSV/USD', 
                            1, 'BSV/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262761, 6685608, 'BTCCHF', 'BTC/CHF', 'BTC/CHF', 
                            1, 'BTC/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262762, 6685608, 'BTCEUR', 'BTC/EUR', 'BTC/EUR', 
                            1, 'BTC/EUR', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 889, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262763, 6685608, 'BTCGBP', 'BTC/GBP', 'BTC/GBP', 
                            1, 'BTC/GBP', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 897, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262764, 6685608, 'BTCJPY', 'BTC/JPY', 'BTC/JPY', 
                            1, 'BTC/JPY', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262765, 6685608, 'BTCLKK', 'BTC/LYKKE', 'BTC/LYKKE', 
                            1, 'BTC/LYKKE', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 900, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262766, 6685608, 'BTCLKK1Y', 'BTC/LKK1Y', 'BTC/LKK1Y', 
                            1, 'BTC/LKK1Y', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 890, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262767, 6685608, 'BTCUSD', 'BTC/USD', 'BTC/USD', 
                            1, 'BTC/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262768, 6685608, 'BTGBTC', 'BTG/BTC', 'BTG/BTC', 
                            1, 'BTG/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262769, 6685608, 'BTGUSD', 'BTG/USD', 'BTG/USD', 
                            1, 'BTG/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262770, 6685608, 'BTSBTC', 'BTS/BTC', 'BTS/BTC', 
                            1, 'BTS/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262771, 6685608, 'BTSUSD', 'BTS/USD', 'BTS/USD', 
                            1, 'BTS/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262772, 6685608, 'CANBTC', 'CAN/BTC', 'CAN/BTC', 
                            1, 'CAN/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262773, 6685608, 'CANETH', 'CAN/ETH', 'CAN/ETH', 
                            1, 'CAN/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262774, 6685608, 'CHFJPY', 'CHF/JPY', 'CHF/JPY', 
                            1, 'CHF/JPY', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262775, 6685608, 'CLNBTC', 'CLN/BTC', 'CLN/BTC', 
                            1, 'CLN/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262776, 6685608, 'CLNETH', 'CLN/ETH', 'CLN/ETH', 
                            1, 'CLN/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262777, 6685608, 'CVCBTC', 'CVC/BTC', 'CVC/BTC', 
                            1, 'CVC/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262778, 6685608, 'CVCETH', 'CVC/ETH', 'CVC/ETH', 
                            1, 'CVC/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262779, 6685608, 'DASHBTC', 'DASH/BTC', 'DASH/BTC', 
                            1, 'DASH/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262780, 6685608, 'DASHUSD', 'DASH/USD', 'DASH/USD', 
                            1, 'DASH/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262781, 6685608, 'DATBTC', 'DAT/BTC', 'DAT/BTC', 
                            1, 'DAT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262782, 6685608, 'DATETH', 'DAT/ETH', 'DAT/ETH', 
                            1, 'DAT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262783, 6685608, 'DEBBTC', 'DEB/BTC', 'DEB/BTC', 
                            1, 'DEB/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262784, 6685608, 'DEBETH', 'DEB/ETH', 'DEB/ETH', 
                            1, 'DEB/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262785, 6685608, 'DENTBTC', 'DENT/BTC', 'DENT/BTC', 
                            1, 'DENT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262786, 6685608, 'DENTETH', 'DENT/ETH', 'DENT/ETH', 
                            1, 'DENT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262787, 6685608, 'DNTBTC', 'DNT/BTC', 'DNT/BTC', 
                            1, 'DNT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262788, 6685608, 'DNTETH', 'DNT/ETH', 'DNT/ETH', 
                            1, 'DNT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262789, 6685608, 'DTHBTC', 'DTH/BTC', 'DTH/BTC', 
                            1, 'DTH/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262790, 6685608, 'DTHETH', 'DTH/ETH', 'DTH/ETH', 
                            1, 'DTH/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262791, 6685608, 'ENGBTC', 'ENG/BTC', 'ENG/BTC', 
                            1, 'ENG/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262792, 6685608, 'ENGETH', 'ENG/ETH', 'ENG/ETH', 
                            1, 'ENG/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262793, 6685608, 'EOScoinBTC', 'EOS/BTC', 'EOS/BTC', 
                            1, 'EOS/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262794, 6685608, 'EOScoinETH', 'EOS/ETH', 'EOS/ETH', 
                            1, 'EOS/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262795, 6685608, 'EOScoinUSD', 'EOS/USD', 'EOS/USD', 
                            1, 'EOS/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262796, 6685608, 'ETCBTC', 'ETC/BTC', 'ETC/BTC', 
                            1, 'ETC/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262797, 6685608, 'ETCUSD', 'ETC/USD', 'ETC/USD', 
                            1, 'ETC/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262798, 6685608, 'ETHBTC', 'ETH/BTC', 'ETH/BTC', 
                            1, 'ETH/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262799, 6685608, 'ETHCHF', 'ETH/CHF', 'ETH/CHF', 
                            1, 'ETH/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262800, 6685608, 'ETHEUR', 'ETH/EUR', 'ETH/EUR', 
                            1, 'ETH/EUR', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 889, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262801, 6685608, 'ETHGBP', 'ETH/GBP', 'ETH/GBP', 
                            1, 'ETH/GBP', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 897, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262802, 6685608, 'ETHLKK', 'ETH/LKK', 'ETH/LKK', 
                            1, 'ETH/LKK', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 900, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262803, 6685608, 'ETHOSBTC', 'ETHOS/BTC', 'ETHOS/BTC', 
                            1, 'ETHOS/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262804, 6685608, 'ETHOSETH', 'ETHOS/ETH', 'ETHOS/ETH', 
                            1, 'ETHOS/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262805, 6685608, 'ETHUSD', 'ETH/USD', 'ETH/USD', 
                            1, 'ETH/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262806, 6685608, 'EURCHF', 'EUR/CHF', 'EUR/CHF', 
                            1, 'EUR/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262807, 6685608, 'EURGBP', 'EUR/GBP', 'EUR/GBP', 
                            1, 'EUR/GBP', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 897, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262741, 6685608, 'AEBTC', 'AE/BTC', 'AE/BTC', 
                            1, 'AE/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262742, 6685608, 'AEETH', 'AE/ETH', 'AE/ETH', 
                            1, 'AE/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262743, 6685608, 'AGIBTC', 'AGI/BTC', 'AGI/BTC', 
                            1, 'AGI/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262744, 6685608, 'AGIETH', 'AGI/ETH', 'AGI/ETH', 
                            1, 'AGI/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262745, 6685608, 'AIONBTC', 'AION/BTC', 'AION/BTC', 
                            1, 'AION/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262808, 6685608, 'EURJPY', 'EUR/JPY', 'EUR/JPY', 
                            1, 'EUR/JPY', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262809, 6685608, 'EURUSD', 'EUR/USD', 'EUR/USD', 
                            1, 'EUR/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262810, 6685608, 'EURZAR', 'EUR/ZAR', 'EUR/ZAR', 
                            1, 'EUR/ZAR', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 891, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262816, 6685608, 'FRECETH', 'FREC/ETH', 'FREC/ETH', 
                            1, 'FREC/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262817, 6685608, 'GATBTC', 'GAT/BTC', 'GAT/BTC', 
                            1, 'GAT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262818, 6685608, 'GATETH', 'GAT/ETH', 'GAT/ETH', 
                            1, 'GAT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262819, 6685608, 'GBPCHF', 'GBP/CHF', 'GBP/CHF', 
                            1, 'GBP/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262820, 6685608, 'GBPJPY', 'GBP/JPY', 'GBP/JPY', 
                            1, 'GBP/JPY', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262821, 6685608, 'GBPUSD', 'GBP/USD', 'GBP/USD', 
                            1, 'GBP/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262822, 6685608, 'GCPcoinBTC', 'GCP/BTC', 'GCP/BTC', 
                            1, 'GCP/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262823, 6685608, 'GCPcoinETH', 'GCP/ETH', 'GCP/ETH', 
                            1, 'GCP/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262824, 6685608, 'GNOBTC', 'GNO/BTC', 'GNO/BTC', 
                            1, 'GNO/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262825, 6685608, 'GNOETH', 'GNO/ETH', 'GNO/ETH', 
                            1, 'GNO/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262826, 6685608, 'GNTBTC', 'GNT/BTC', 'GNT/BTC', 
                            1, 'GNT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262827, 6685608, 'GNTETH', 'GNT/ETH', 'GNT/ETH', 
                            1, 'GNT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262828, 6685608, 'GVTBTC', 'GVT/BTC', 'GVT/BTC', 
                            1, 'GVT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262829, 6685608, 'GVTETH', 'GVT/ETH', 'GVT/ETH', 
                            1, 'GVT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262830, 6685608, 'HBZBTC', 'HBZ/BTC', 'HBZ/BTC', 
                            1, 'HBZ/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262831, 6685608, 'HBZETH', 'HBZ/ETH', 'HBZ/ETH', 
                            1, 'HBZ/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262832, 6685608, 'HCPBTC', 'TREE/BTC', 'TREE/BTC', 
                            1, 'TREE/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262833, 6685608, 'HCPCHF', 'TREE/CHF', 'TREE/CHF', 
                            1, 'TREE/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262834, 6685608, 'HCPEUR', 'TREE/EUR', 'TREE/EUR', 
                            1, 'TREE/EUR', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 889, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262835, 6685608, 'HCPGBP', 'TREE/GBP', 'TREE/GBP', 
                            1, 'TREE/GBP', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 897, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262836, 6685608, 'HCPUSD', 'TREE/USD', 'TREE/USD', 
                            1, 'TREE/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262837, 6685608, 'HGTBTC', 'HGT/BTC', 'HGT/BTC', 
                            1, 'HGT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262838, 6685608, 'HGTETH', 'HGT/ETH', 'HGT/ETH', 
                            1, 'HGT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262839, 6685608, 'HMQBTC', 'HMQ/BTC', 'HMQ/BTC', 
                            1, 'HMQ/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262840, 6685608, 'HVNBTC', 'HVN/BTC', 'HVN/BTC', 
                            1, 'HVN/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262841, 6685608, 'HVNETH', 'HVN/ETH', 'HVN/ETH', 
                            1, 'HVN/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262842, 6685608, 'ICXBTC', 'ICX/BTC', 'ICX/BTC', 
                            1, 'ICX/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262843, 6685608, 'ICXETH', 'ICX/ETH', 'ICX/ETH', 
                            1, 'ICX/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262844, 6685608, 'INDBTC', 'IND/BTC', 'IND/BTC', 
                            1, 'IND/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262845, 6685608, 'INDETH', 'IND/ETH', 'IND/ETH', 
                            1, 'IND/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262846, 6685608, 'IOSTBTC', 'IOST/BTC', 'IOST/BTC', 
                            1, 'IOST/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262847, 6685608, 'IOSTETH', 'IOST/ETH', 'IOST/ETH', 
                            1, 'IOST/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262848, 6685608, 'IPSBTC', 'IPS/BTC', 'IPS/BTC', 
                            1, 'IPS/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262849, 6685608, 'IPSETH', 'IPS/ETH', 'IPS/ETH', 
                            1, 'IPS/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262850, 6685608, 'KEYBTC', 'KEY/BTC', 'KEY/BTC', 
                            1, 'KEY/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262851, 6685608, 'KEYETH', 'KEY/ETH', 'KEY/ETH', 
                            1, 'KEY/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262852, 6685608, 'LCDBTC', 'LCD/BTC', 'LCD/BTC', 
                            1, 'LCD/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262853, 6685608, 'LCDETH', 'LCD/ETH', 'LCD/ETH', 
                            1, 'LCD/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262854, 6685608, 'LGLBTC', 'LGL/BTC', 'LGL/BTC', 
                            1, 'LGL/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262855, 6685608, 'LGLETH', 'LGL/ETH', 'LGL/ETH', 
                            1, 'LGL/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262856, 6685608, 'LKK1YCHF', 'LKK1Y/CHF', 'LKK1Y/CHF', 
                            1, 'LKK1Y/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262857, 6685608, 'LKK1YEUR', 'LKK1Y/EUR', 'LKK1Y/EUR', 
                            1, 'LKK1Y/EUR', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 889, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262858, 6685608, 'LKK1YGBP', 'LKK1Y/GBP', 'LKK1Y/GBP', 
                            1, 'LKK1Y/GBP', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 897, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262859, 6685608, 'LKK1YJPY', 'LKK1Y/JPY', 'LKK1Y/JPY', 
                            1, 'LKK1Y/JPY', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262860, 6685608, 'LKK1YLKK', 'LKK1Y/LKK', 'LKK1Y/LKK', 
                            1, 'LKK1Y/LKK', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 900, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262861, 6685608, 'LKK1YUSD', 'LKK1Y/USD', 'LKK1Y/USD', 
                            1, 'LKK1Y/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262862, 6685608, 'LKK2YCHF', 'LKK2Y/CHF', 'LKK2Y/CHF', 
                            1, 'LKK2Y/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262863, 6685608, 'LKKCHF', 'LYKKE/CHF', 'LYKKE/CHF', 
                            1, 'LYKKE/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262864, 6685608, 'LKKEUR', 'LYKKE/EUR', 'LYKKE/EUR', 
                            1, 'LYKKE/EUR', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 889, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262865, 6685608, 'LKKGBP', 'LYKKE/GBP', 'LYKKE/GBP', 
                            1, 'LYKKE/GBP', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 897, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262866, 6685608, 'LKKJPY', 'LYKKE/JPY', 'LYKKE/JPY', 
                            1, 'LYKKE/JPY', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262867, 6685608, 'LKKUSD', 'LYKKE/USD', 'LYKKE/USD', 
                            1, 'LYKKE/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262868, 6685608, 'LOCBTC', 'LOC/BTC', 'LOC/BTC', 
                            1, 'LOC/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262869, 6685608, 'LOCETH', 'LOC/ETH', 'LOC/ETH', 
                            1, 'LOC/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262870, 6685608, 'LRCBTC', 'LRC/BTC', 'LRC/BTC', 
                            1, 'LRC/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262871, 6685608, 'LRCETH', 'LRC/ETH', 'LRC/ETH', 
                            1, 'LRC/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262872, 6685608, 'LTCBTC', 'LTC/BTC', 'LTC/BTC', 
                            1, 'LTC/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262873, 6685608, 'LTCCHF', 'LTC/CHF', 'LTC/CHF', 
                            1, 'LTC/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262874, 6685608, 'LTCUSD', 'LTC/USD', 'LTC/USD', 
                            1, 'LTC/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262875, 6685608, 'MANABTC', 'MANA/BTC', 'MANA/BTC', 
                            1, 'MANA/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262876, 6685608, 'MANAETH', 'MANA/ETH', 'MANA/ETH', 
                            1, 'MANA/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262811, 6685608, 'EVXBTC', 'EVX/BTC', 'EVX/BTC', 
                            1, 'EVX/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262812, 6685608, 'EVXETH', 'EVX/ETH', 'EVX/ETH', 
                            1, 'EVX/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262813, 6685608, 'FDZBTC', 'FDZ/BTC', 'FDZ/BTC', 
                            1, 'FDZ/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262814, 6685608, 'FDZETH', 'FDZ/ETH', 'FDZ/ETH', 
                            1, 'FDZ/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262815, 6685608, 'FRECBTC', 'FREC/BTC', 'FREC/BTC', 
                            1, 'FREC/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262877, 6685608, 'MCOBTC', 'MCO/BTC', 'MCO/BTC', 
                            1, 'MCO/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262878, 6685608, 'MSPBTC', 'MSP/BTC', 'MSP/BTC', 
                            1, 'MSP/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262879, 6685608, 'MSPETH', 'MSP/ETH', 'MSP/ETH', 
                            1, 'MSP/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262880, 6685608, 'MTLBTC', 'MTL/BTC', 'MTL/BTC', 
                            1, 'MTL/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262885, 6685608, 'MYSTETH', 'MYST/ETH', 'MYST/ETH', 
                            1, 'MYST/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262886, 6685608, 'OMGBTC', 'OMG/BTC', 'OMG/BTC', 
                            1, 'OMG/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262887, 6685608, 'OMGETH', 'OMG/ETH', 'OMG/ETH', 
                            1, 'OMG/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262888, 6685608, 'PASSBTC', 'PASS/BTC', 'PASS/BTC', 
                            1, 'PASS/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262889, 6685608, 'PASSETH', 'PASS/ETH', 'PASS/ETH', 
                            1, 'PASS/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262890, 6685608, 'PCLcoinBTC', 'PCL/BTC', 'PCL/BTC', 
                            1, 'PCL/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262891, 6685608, 'PCLcoinETH', 'PCL/ETH', 'PCL/ETH', 
                            1, 'PCL/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262892, 6685608, 'PKTBTC', 'PKT/BTC', 'PKT/BTC', 
                            1, 'PKT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262893, 6685608, 'PKTETH', 'PKT/ETH', 'PKT/ETH', 
                            1, 'PKT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262894, 6685608, 'POWRBTC', 'POWR/BTC', 'POWR/BTC', 
                            1, 'POWR/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262895, 6685608, 'POWRETH', 'POWR/ETH', 'POWR/ETH', 
                            1, 'POWR/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262896, 6685608, 'PPTBTC', 'PPT/BTC', 'PPT/BTC', 
                            1, 'PPT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262897, 6685608, 'PPTETH', 'PPT/ETH', 'PPT/ETH', 
                            1, 'PPT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262898, 6685608, 'QNTUBTC', 'QNTU/BTC', 'QNTU/BTC', 
                            1, 'QNTU/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262899, 6685608, 'QNTUETH', 'QNTU/ETH', 'QNTU/ETH', 
                            1, 'QNTU/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262900, 6685608, 'REPBTC', 'REP/BTC', 'REP/BTC', 
                            1, 'REP/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262901, 6685608, 'REPETH', 'REP/ETH', 'REP/ETH', 
                            1, 'REP/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262902, 6685608, 'REQBTC', 'REQ/BTC', 'REQ/BTC', 
                            1, 'REQ/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262903, 6685608, 'REQETH', 'REQ/ETH', 'REQ/ETH', 
                            1, 'REQ/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262904, 6685608, 'SLRBTC', 'SLR/BTC', 'SLR/BTC', 
                            1, 'SLR/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262905, 6685608, 'SLRCHF', 'SLR/CHF', 'SLR/CHF', 
                            1, 'SLR/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262906, 6685608, 'SLREUR', 'SLR/EUR', 'SLR/EUR', 
                            1, 'SLR/EUR', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 889, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262907, 6685608, 'SLRGBP', 'SLR/GBP', 'SLR/GBP', 
                            1, 'SLR/GBP', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 897, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262908, 6685608, 'SLRJPY', 'SLR/JPY', 'SLR/JPY', 
                            1, 'SLR/JPY', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262909, 6685608, 'SLRUSD', 'SLR/USD', 'SLR/USD', 
                            1, 'SLR/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262910, 6685608, 'SNMBTC', 'SNM/BTC', 'SNM/BTC', 
                            1, 'SNM/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262911, 6685608, 'SNMETH', 'SNM/ETH', 'SNM/ETH', 
                            1, 'SNM/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262912, 6685608, 'STORJBTC', 'STORJ/BTC', 'STORJ/BTC', 
                            1, 'STORJ/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262913, 6685608, 'STORJETH', 'STORJ/ETH', 'STORJ/ETH', 
                            1, 'STORJ/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262914, 6685608, 'SUBBTC', 'SUB/BTC', 'SUB/BTC', 
                            1, 'SUB/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262915, 6685608, 'SUBETH', 'SUB/ETH', 'SUB/ETH', 
                            1, 'SUB/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262916, 6685608, 'TIMEBTC', 'TIME/BTC', 'TIME/BTC', 
                            1, 'TIME/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262917, 6685608, 'TIMECHF', 'TIME/CHF', 'TIME/CHF', 
                            1, 'TIME/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262918, 6685608, 'TIMEETH', 'TIME/ETH', 'TIME/ETH', 
                            1, 'TIME/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262919, 6685608, 'TIMEEUR', 'TIME/EUR', 'TIME/EUR', 
                            1, 'TIME/EUR', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 889, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262920, 6685608, 'TIMEGBP', 'TIME/GBP', 'TIME/GBP', 
                            1, 'TIME/GBP', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 897, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262921, 6685608, 'TIMEJPY', 'TIME/JPY', 'TIME/JPY', 
                            1, 'TIME/JPY', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262922, 6685608, 'TIMEUSD', 'TIME/USD', 'TIME/USD', 
                            1, 'TIME/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262923, 6685608, 'TLCI/USD', 'TLCI/USD', 'TLCI/USD', 
                            1, 'TLCItest/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262924, 6685608, 'USDCAD', 'USD/CAD', 'USD/CAD', 
                            1, 'USD/CAD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 911, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262925, 6685608, 'USDCHF', 'USD/CHF', 'USD/CHF', 
                            1, 'USD/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262926, 6685608, 'USDCZK', 'USD/CZK', 'USD/CZK', 
                            1, 'USD/CZK', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 901, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262927, 6685608, 'USDDKK', 'USD/DKK', 'USD/DKK', 
                            1, 'USD/DKK', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 907, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262881, 6685608, 'MTLETH', 'MTL/ETH', 'MTL/ETH', 
                            1, 'MTL/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262882, 6685608, 'MWATBTC', 'MWAT/BTC', 'MWAT/BTC', 
                            1, 'MWAT/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262883, 6685608, 'MWATETH', 'MWAT/ETH', 'MWAT/ETH', 
                            1, 'MWAT/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262928, 6685608, 'USDHKD', 'USD/HKD', 'USD/HKD', 
                            1, 'USD/HKD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 908, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262929, 6685608, 'USDHUF', 'USD/HUF', 'USD/HUF', 
                            1, 'USD/HUF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 902, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262930, 6685608, 'USDILS', 'USD/ILS', 'USD/ILS', 
                            1, 'USD/ILS', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 903, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262931, 6685608, 'USDJPY', 'USD/JPY', 'USD/JPY', 
                            1, 'USD/JPY', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262932, 6685608, 'USDMXN', 'USD/MXN', 'USD/MXN', 
                            1, 'USD/MXN', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 912, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262933, 6685608, 'USDNOK', 'USD/NOK', 'USD/NOK', 
                            1, 'USD/NOK', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 904, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262934, 6685608, 'USDNZD', 'USD/NZD', 'USD/NZD', 
                            1, 'USD/NZD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 895, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262935, 6685608, 'USDPLN', 'USD/PLN', 'USD/PLN', 
                            1, 'USD/PLN', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 892, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262936, 6685608, 'USDRUB', 'USD/RUB', 'USD/RUB', 
                            1, 'USD/RUB', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 893, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262937, 6685608, 'USDSEK', 'USD/SEK', 'USD/SEK', 
                            1, 'USD/SEK', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 896, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262938, 6685608, 'USDSGD', 'USD/SGD', 'USD/SGD', 
                            1, 'USD/SGD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 905, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262939, 6685608, 'USDTRY', 'USD/TRY', 'USD/TRY', 
                            1, 'USD/TRY', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 894, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262940, 6685608, 'USDZAR', 'USD/ZAR', 'USD/ZAR', 
                            1, 'USD/ZAR', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 891, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262941, 6685608, 'VEEBTC', 'VEE/BTC', 'VEE/BTC', 
                            1, 'VEE/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262942, 6685608, 'VEEETH', 'VEE/ETH', 'VEE/ETH', 
                            1, 'VEE/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262943, 6685608, 'VETcoinBTC', 'VET/BTC', 'VET/BTC', 
                            1, 'VET/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262944, 6685608, 'VETcoinETH', 'VET/ETH', 'VET/ETH', 
                            1, 'VET/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262945, 6685608, 'VIBBTC', 'VIB/BTC', 'VIB/BTC', 
                            1, 'VIB/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262946, 6685608, 'VIBETH', 'VIB/ETH', 'VIB/ETH', 
                            1, 'VIB/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262884, 6685608, 'MYSTBTC', 'MYST/BTC', 'MYST/BTC', 
                            1, 'MYST/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262947, 6685608, 'VLDBTC', 'VLD/BTC', 'VLD/BTC', 
                            1, 'VLD/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262948, 6685608, 'VLDETH', 'VLD/ETH', 'VLD/ETH', 
                            1, 'VLD/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262949, 6685608, 'WAXBTC', 'WAX/BTC', 'WAX/BTC', 
                            1, 'WAX/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262950, 6685608, 'WAXETH', 'WAX/ETH', 'WAX/ETH', 
                            1, 'WAX/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262979, 6685608, 'WAX', 'WAX', 'WAX', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262980, 6685608, 'REP', 'REP', 'REP', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262981, 6685608, 'ZEC', 'ZEC', 'ZEC', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262982, 6685608, 'AMLT', 'AMLT', 'AMLT', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262983, 6685608, 'GNT', 'GNT', 'GNT', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262984, 6685608, 'STORJ', 'STORJ', 'STORJ', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262985, 6685608, 'MWAT', 'MWAT', 'MWAT', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262986, 6685608, 'GNO', 'GNO', 'GNO', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262987, 6685608, 'IOST', 'IOST', 'IOST', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262988, 6685608, 'Eos', 'Eos', 'Eos', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262989, 6685608, 'ZRX', 'ZRX', 'ZRX', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262990, 6685608, 'AE', 'AE', 'AE', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262991, 6685608, 'SLR', 'SLR', 'SLR', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262992, 6685608, 'TLCI', 'TLCI', 'TLCI', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262993, 6685608, 'DASH', 'DASH', 'DASH', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262994, 6685608, 'VLD', 'VLD', 'VLD', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262995, 6685608, 'OMG', 'OMG', 'OMG', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262996, 6685608, 'TIME', 'TIME', 'TIME', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262997, 6685608, 'TRY', 'TRY', 'TRY', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262998, 6685608, 'LCD', 'LCD', 'LCD', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262999, 6685608, 'POWR', 'POWR', 'POWR', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263000, 6685608, 'PLN', 'PLN', 'PLN', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263001, 6685608, 'RUB', 'RUB', 'RUB', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263002, 6685608, 'LiteCoin', 'LiteCoin', 'LiteCoin', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262951, 6685608, 'WPRBTC', 'WPR/BTC', 'WPR/BTC', 
                            1, 'WPR/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262952, 6685608, 'WPRETH', 'WPR/ETH', 'WPR/ETH', 
                            1, 'WPR/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262953, 6685608, 'WTCBTC', 'WTC/BTC', 'WTC/BTC', 
                            1, 'WTC/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262954, 6685608, 'WTCETH', 'WTC/ETH', 'WTC/ETH', 
                            1, 'WTC/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262955, 6685608, 'XAGUSD', 'XAG/USD', 'XAG/USD', 
                            1, 'XAG/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262956, 6685608, 'XAUUSD', 'XAU/USD', 'XAU/USD', 
                            1, 'XAU/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262957, 6685608, 'XLMBTC', 'XLM/BTC', 'XLM/BTC', 
                            1, 'XLM/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262958, 6685608, 'XLMUSD', 'XLM/USD', 'XLM/USD', 
                            1, 'XLM/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262959, 6685608, 'XPDUSD', 'XPD/USD', 'XPD/USD', 
                            1, 'XPD/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262960, 6685608, 'XPTUSD', 'XPT/USD', 'XPT/USD', 
                            1, 'XPT/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262961, 6685608, 'XRPBTC', 'XRP/BTC', 'XRP/BTC', 
                            1, 'XRP/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262962, 6685608, 'XRPCHF', 'XRP/CHF', 'XRP/CHF', 
                            1, 'XRP/CHF', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262963, 6685608, 'XRPETH', 'XRP/ETH', 'XRP/ETH', 
                            1, 'XRP/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262964, 6685608, 'XRPEUR', 'XRP/EUR', 'XRP/EUR', 
                            1, 'XRP/EUR', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 889, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262965, 6685608, 'XRPUSD', 'XRP/USD', 'XRP/USD', 
                            1, 'XRP/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262966, 6685608, 'ZECBTC', 'ZEC/BTC', 'ZEC/BTC', 
                            1, 'ZEC/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262967, 6685608, 'ZECUSD', 'ZEC/USD', 'ZEC/USD', 
                            1, 'ZEC/USD', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262968, 6685608, 'ZILBTC', 'ZIL/BTC', 'ZIL/BTC', 
                            1, 'ZIL/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262969, 6685608, 'ZILETH', 'ZIL/ETH', 'ZIL/ETH', 
                            1, 'ZIL/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262970, 6685608, 'ZRXBTC', 'ZRX/BTC', 'ZRX/BTC', 
                            1, 'ZRX/BTC', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17262971, 6685608, 'ZRXETH', 'ZRX/ETH', 'ZRX/ETH', 
                            1, 'ZRX/ETH', TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            1, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('01/15/2019 10:29:28', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263003, 6685608, 'Bitshares', 'Bitshares', 'Bitshares', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263004, 6685608, 'BitcoinGold', 'BitcoinGold', 'BitcoinGold', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263005, 6685608, 'ETC', 'ETC', 'ETC', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263006, 6685608, 'AppCoins', 'AppCoins', 'AppCoins', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263007, 6685608, 'BSV', 'BSV', 'BSV', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263008, 6685608, 'SNM', 'SNM', 'SNM', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263009, 6685608, 'DAT', 'DAT', 'DAT', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263010, 6685608, 'EVX', 'EVX', 'EVX', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263011, 6685608, 'SEK', 'SEK', 'SEK', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263012, 6685608, 'WPR', 'WPR', 'WPR', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263013, 6685608, 'BCH', 'BCH', 'BCH', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263014, 6685608, 'GBP', 'GBP', 'GBP', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263015, 6685608, 'AGI', 'AGI', 'AGI', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263016, 6685608, 'JPY', 'JPY', 'JPY', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263017, 6685608, 'XPT', 'XPT', 'XPT', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263018, 6685608, 'DEB', 'DEB', 'DEB', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263019, 6685608, 'AIR', 'AIR', 'AIR', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263020, 6685608, 'HVN', 'HVN', 'HVN', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263021, 6685608, 'SUB', 'SUB', 'SUB', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263022, 6685608, 'XPD', 'XPD', 'XPD', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263023, 6685608, 'GAT', 'GAT', 'GAT', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263024, 6685608, 'LKK', 'LKK', 'LKK', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263025, 6685608, 'XAU', 'XAU', 'XAU', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263026, 6685608, 'ILS', 'ILS', 'ILS', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263027, 6685608, 'SGD', 'SGD', 'SGD', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263028, 6685608, 'XAG', 'XAG', 'XAG', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263029, 6685608, 'LKK2Y', 'LKK2Y', 'LKK2Y', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263030, 6685608, 'DENT', 'DENT', 'DENT', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263031, 6685608, 'CZK', 'CZK', 'CZK', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263032, 6685608, 'PKT', 'PKT', 'PKT', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263033, 6685608, 'VIB', 'VIB', 'VIB', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263034, 6685608, 'PPT', 'PPT', 'PPT', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263035, 6685608, 'XLM', 'XLM', 'XLM', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263036, 6685608, 'HCP', 'HCP', 'HCP', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263037, 6685608, 'BNT', 'BNT', 'BNT', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263038, 6685608, 'HKD', 'HKD', 'HKD', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263039, 6685608, 'ETHOS', 'ETHOS', 'ETHOS', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263040, 6685608, 'KEY', 'KEY', 'KEY', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263041, 6685608, 'CLN', 'CLN', 'CLN', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263042, 6685608, 'ICX', 'ICX', 'ICX', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263043, 6685608, 'XRP', 'XRP', 'XRP', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263044, 6685608, 'EOS', 'EOS', 'EOS', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263045, 6685608, 'AION', 'AION', 'AION', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263046, 6685608, 'AUD', 'AUD', 'AUD', 
                            NULL, NULL, NULL, TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('02/02/2019 07:42:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263106, 1, 'EUR/USD Benchmark', 'EUR/USD Benchmark', 'EUR/USD Benchmark Indexes', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 23:15:05', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 23:15:05', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263107, 1, 'CHF/USD Benchmark', 'CHF/USD Benchmark', 'CHF/USD Benchmark Indexes', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 23:15:06', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 23:15:06', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263108, 1, 'GBP/USD Benchmark', 'GBP/USD Benchmark', 'GBP/USD Benchmark Indexes', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 23:15:06', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 23:15:06', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263109, 1, 'USD/JPY Benchmark', 'USD/JPY Benchmark', 'USD/JPY Benchmark Indexes', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 23:15:06', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 23:15:06', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263060, 6685608, 'LYCI/USD', 'LYCI/USD', 'LYCI/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:52', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:52', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263061, 6685608, 'PLYCI/USD', 'PLYCI/USD', 'PLYCI/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:52', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:52', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263062, 6685608, 'SLYCI/USD', 'SLYCI/USD', 'SLYCI/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:52', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:52', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263063, 6685608, 'DCR/USD', 'DCR/USD', 'DCR/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263064, 6685608, 'DCR/BTC', 'DCR/BTC', 'DCR/BTC', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263065, 6685608, 'GLX/USD', 'GLX/USD', 'GLX/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263066, 6685608, 'GLX/ETH', 'GLX/ETH', 'GLX/ETH', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263067, 6685608, 'GLX/EUR', 'GLX/EUR', 'GLX/EUR', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 889, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263068, 6685608, 'GLX/BTC', 'GLX/BTC', 'GLX/BTC', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263069, 6685608, 'KIN/BTC', 'KIN/BTC', 'KIN/BTC', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:53', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263070, 6685608, 'KIN/ETH', 'KIN/ETH', 'KIN/ETH', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:54', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:54', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263071, 6685608, 'KIN/USD', 'KIN/USD', 'KIN/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:54', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:54', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263073, 6685608, 'NEO/BTC', 'NEO/BTC', 'NEO/BTC', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:54', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:54', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263074, 6685608, 'NEO/USD', 'NEO/USD', 'NEO/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:54', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:54', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263075, 6685608, 'HCP/BTC', 'HCP/BTC', 'HCP/BTC', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:55', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:55', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263076, 6685608, 'HCP/USD', 'HCP/USD', 'HCP/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:55', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:55', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263077, 6685608, 'HCP/EUR', 'HCP/EUR', 'HCP/EUR', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:55', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 889, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:55', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263078, 6685608, 'HCP/GBP', 'HCP/GBP', 'HCP/GBP', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:55', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 897, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:55', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263079, 6685608, 'HCP/CHF', 'HCP/CHF', 'HCP/CHF', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:55', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:55', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263080, 6685608, 'testP/USD', 'testP/USD', 'testP/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:56', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:56', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263081, 6685608, 'testSC/USD', 'testSC/USD', 'testSC/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:56', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:56', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263082, 6685608, 'new_PCL/ETH', 'new_PCL/ETH', 'new_PCL/ETH', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:59:56', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:59:56', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263083, 6685608, 'NEO', 'NEO', 'NEO', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 23:25:42', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 23:25:42', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263084, 6685608, 'LYCI', 'LYCI', 'LYCI', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 23:25:42', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 23:25:42', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263085, 6685608, 'SLYCI', 'SLYCI', 'SLYCI', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 23:25:42', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 23:25:42', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263086, 6685608, 'PLYCI', 'PLYCI', 'PLYCI', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 23:25:43', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 23:25:43', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263088, 6685608, 'DCR', 'DCR', 'DCR', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 23:25:58', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 23:25:58', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263089, 6685608, 'GLX', 'GLX', 'GLX', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 23:25:58', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 23:25:58', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263090, 6685608, 'STEEM', 'STEEM', 'STEEM', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 23:25:58', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 23:25:58', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263091, 6685608, 'KIN', 'KIN', 'KIN', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 23:25:58', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 23:25:58', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263053, 6685608, 'LKK/JPY', 'LKK/JPY', 'LKK/JPY', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:17:02', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:17:02', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263054, 6685608, 'LKK/CHF', 'LKK/CHF', 'LKK/CHF', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:17:06', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 906, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:17:06', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263055, 6685608, 'LKK/EUR', 'LKK/EUR', 'LKK/EUR', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:17:10', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 889, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:17:10', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263056, 6685608, 'LKK/USD', 'LKK/USD', 'LKK/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:17:14', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:17:14', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263057, 6685608, 'LKK/GBP', 'LKK/GBP', 'LKK/GBP', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:17:17', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 897, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:17:17', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263058, 6685608, 'STEEM/BTC', 'STEEM/BTC', 'STEEM/BTC', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:20:17', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 899, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:20:17', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263059, 6685608, 'STEEM/USD', 'STEEM/USD', 'STEEM/USD', 
                            NULL, NULL, NULL, TO_DATE('04/28/2019 22:20:23', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/28/2019 22:20:23', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263093, 6685608, 'BTC/LKK', 'BTC/LKK', 'BTC/LKK', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 13:38:10', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 900, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 13:38:10', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263098, 6685608, 'AIR/ETH', 'AIR/ETH', 'AIR/ETH', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 13:59:10', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 909, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 13:59:10', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263099, 6685608, 'testP', 'testP', 'testP', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 14:05:12', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 14:05:12', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263100, 6685608, 'testSC', 'testSC', 'testSC', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 14:05:12', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 14:05:12', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263101, 6685608, 'GCP', 'GCP', 'GCP', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 14:05:12', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 14:05:12', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263102, 6685608, 'HGT', 'HGT', 'HGT', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 14:05:12', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 14:05:12', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263103, 6685608, 'new_PCL', 'new_PCL', 'new_PCL', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 14:05:12', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 14:05:12', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263105, 1, 'SLR/USD CMC', 'SLR/USD CoinMarketCap', 'SLR/USD CoinMarketCap Indexes', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 23:00:52', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 23:00:52', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263110, 1, 'USD/CHF Benchmark', 'USD/CHF Benchmark', 'USD/CHF Benchmark Indexes', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 23:39:16', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 898, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 23:39:16', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263094, 6685608, 'BTG', 'BTG', 'BTG', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 13:44:37', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 13:44:37', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263095, 6685608, 'BTS', 'BTS', 'BTS', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 13:44:37', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 13:44:37', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263096, 6685608, 'APPC', 'APPC', 'APPC', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 13:44:37', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 13:44:37', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);
                        Insert into TL_SECURITY
                        (SECURITY_ID, BOARD_ID, TICKER, SHORTNAME, NAME, 
                            FACEVALUE, ISIN, ISSUEDATE, CREATEDATE, CREATOR_ID, 
                            ISSUESIZE, EXCHANGE_ID, SECURITYTYPE_ID, ISSUER_ID, CURRENCY_ID, 
                            REGNO, SEC_GRP_ID, LOTSIZE, DELIVERYDATE, STRIKEPRICE, 
                            OPTIONTYPE_ID, IDENT, SETTLE_CODE, INSTR_ID, MARKETSEGMENTID, 
                            ACTUALDATE, FUT_TYPE, INPUTDATE, MATURITY_DATE)
                        Values
                        (17263097, 6685608, 'LTC', 'LTC', 'LTC', 
                            NULL, NULL, NULL, TO_DATE('04/29/2019 13:44:38', 'MM/DD/YYYY HH24:MI:SS'), 105, 
                            NULL, 1010, 1, NULL, 910, 
                            NULL, NULL, NULL, NULL, NULL, 
                            NULL, NULL, NULL, NULL, NULL, 
                            TO_DATE('04/29/2019 13:44:38', 'MM/DD/YYYY HH24:MI:SS'), NULL, NULL, NULL);

                        '''
    cursor.execute(sql_insert_query)