# This Python file uses the following encoding: utf-8
from mysql.connector import connect,Error
import importlib                                                                                           ##THIS MODULE CONVERT AND RUN STRING TO MODULE 






try:
    with connect(host='localhost',user='root',password='58858810',database='db_torob') as Torob:
        productsList=[]
        myCursor=Torob.cursor()                                                                             ##GET DATABASE DATA
        myCursor.execute('select * from t_verifiedSellers')                                                 ##GET ALL SELLERS FIELD
        sellersList=myCursor.fetchall()                                                                     ##CONVERT ALL OF THEM TO LIST LIKE→[(),(),...]
        sellerProduct=[]                                                                                    ##THIS LIST TAKE LIST OF EACH SELLER PRODUCT
        myCursor.execute('delete from t_torobProducts ')
        Torob.commit()
        for sellerDetail in sellersList:    
            if sellerDetail[6]==1:                                                                          ##IF THEIR STATUS CODE=1 (ACTIVE) → GET THEIR PRODUCTS
                moduleName=importlib.import_module(sellerDetail[7])                                         ##sellerDetail[7] IS MODULE NAME , IN LAST FIELD (sellerDetail[7]) WE SAVE MODULE NAME FOR RUN AND GET PRODUCT LIST                         
                if not moduleName==None:
                    sellerProduct=moduleName.GetAllProduct()                                                ##APPEND MANUALLY OUR SELLERS PRODUCT TO LIST
                    for product in sellerProduct:
                        productsList.append(product)                                                        ##APPEND ALL PRODUCTS DICTIONARY
            elif sellerDetail[6]==0:
                print(f"{sellerDetail[1]} is Suspension.")
            elif sellerDetail[6]==-1:
                print(f"{sellerDetail[1]} is Deactivate.")
            else:
                print(f"{sellerDetail[1]} have invalid value.")
                
        for product in productsList:
                ##SAVE ALL DATA TO PRODUCT TABLE
                        
                            ##UPDATE  PRODUCT PRICE     WICH LINKS MATCH    (USE LINKS FOR CONDITION BECAUSE EACH PRODUCT LINKS IS UNIQUE)
                            ##UPDATE PRODUCT IN MAIN TABLE
            myCursor.execute('select * from t_torobProducts')
            availibleProductInDatabase=myCursor.fetchall()
                        ##INSERT ALL PRODUCT IN OUR TEMPORARY TABLE
                        
            myCursor.execute(f'''
                                insert IGNORE  into t_torobProducts(sellerCode,sellerName,productCategori,productName,productLinkURL,productImageURL,productPrice)         
                                value(
                                        '{product["SellerCode"]}',
                                        '{product["SellerName"]}',
                                        '{product["ProductCategori"]}',
                                        '{product["ProductName"]}',
                                        '{product["ProductLink"]}',
                                        '{product["ProductImage"]}',
                                        '{product["ProductPrice"]}'
                                    )
                                
                            ''')
            Torob.commit()
except Error as errorr:
    print(errorr)













