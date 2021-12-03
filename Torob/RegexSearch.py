from mysql.connector import connect,Error
import re
# from SearchHomeGUI import SetKeyword


def GiveSearchKeyWord(searchKeyword):
    def SearchInData(searchKeyword):
        try:
            with connect(host='localhost',user='root',password='58858810',database='db_torob') as Torob:
                myCursor=Torob.cursor()
                myCursor.execute('select * from t_torobProducts')                           
                products=myCursor.fetchall()
                searchesList=[list(productTuple) for productTuple in products]
                resultList=[]

                for item in searchesList:
                    resultObject=(re.search(r'.*?{0}.*'.format(searchKeyword),item[4]))
                    if not resultObject==None:
                        resultList.append(item)

                myCursor.execute('delete from t_temporaryResultSearch ')
                Torob.commit()
                for product in resultList:
                    myCursor.execute(f'''
                                        insert IGNORE  into t_temporaryResultSearch(sellerCode,sellerName,productCategori,productName,productImageURL,productPrice,productLinkURL)         
                                        value(
                                                '{product[0]}',
                                                '{product[1]}',
                                                '{product[3]}',
                                                '{product[4]}',
                                                '{product[5]}',
                                                '{product[6]}',
                                                '{product[7]}'
                                            )

                                    ''')
                Torob.commit()
                return True
        except Error as error:
            print(error)
    SearchInData(searchKeyword)
    from SearchResult import searchResults
    searchResults()
    
    
    
    
    
    

def SearchInCategory(searchKeyword):
    def SearchInData(searchKeyword):
        try:
            with connect(host='localhost',user='root',password='58858810',database='db_torob') as Torob:
                myCursor=Torob.cursor()
                myCursor.execute('select * from t_torobProducts')                           
                products=myCursor.fetchall()
                searchesList=[list(productTuple) for productTuple in products]
                resultList=[]

                for item in searchesList:
                    resultObject=(re.search(r'.*?{0}.*'.format(searchKeyword),item[3]))
                    if not resultObject==None:
                        resultList.append(item)

                myCursor.execute('delete from t_temporaryResultSearch ')
                Torob.commit()
                for product in resultList:
                    myCursor.execute(f'''
                                        insert IGNORE  into t_temporaryResultSearch(sellerCode,sellerName,productCategori,productName,productImageURL,productPrice,productLinkURL)         
                                        value(
                                                '{product[0]}',
                                                '{product[1]}',
                                                '{product[3]}',
                                                '{product[4]}',
                                                '{product[5]}',
                                                '{product[6]}',
                                                '{product[7]}'
                                            )

                                    ''')
                Torob.commit()
                return True
        except Error as error:
            print(error)
    SearchInData(searchKeyword)
    from SearchResult import searchResults
    searchResults()
    
    
    
    