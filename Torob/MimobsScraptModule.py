# This Python file uses the following encoding: utf-8
import requests
from bs4 import BeautifulSoup
from ScraptingModule import Seller





class Mimobs(Seller):
    def __init__(self,sellerName,sellerLinkURL,sellerEnamadURL,sellerLogoURL,sellerContactInfo,sellerStatus,sellerModuleName):
        self.sellerName         = sellerName
        self.sellerLinkURL      = sellerLinkURL
        self.sellerEnamadURL    = sellerEnamadURL
        self.sellerLogoURL      = sellerLogoURL
        self.sellerContactInfo  = sellerContactInfo
        self.sellerStatus       = sellerStatus
        self.sellerModuleName   = sellerModuleName
        
        Seller.__init__(self,self.sellerName,self.sellerLinkURL,self.sellerEnamadURL,self.sellerLogoURL,self.sellerContactInfo,self.sellerStatus,self.sellerModuleName)


    def GetCategories(self):
        HomePageDataContent=BeautifulSoup(requests.get('https://mimobs.com/').content,'html.parser')                 ##GET SITE DATA AND DEFINE SITE CONTENT AS HTML WITH BEAUTIFUL SOUP FOR MAKING SITE SCRIPT EASIER
        siteMenu=HomePageDataContent.select('li.nav-item')                       ##GET ALL li  FOR FIND PRODUCT links PAGES
        del siteMenu[0]                                                                      ##DELETE ABOUT US PAGE LINK (...)
        del siteMenu[-1]                                                                      ##DELETE ABOUT US PAGE LINK (...)
        del siteMenu[-1]                                                                      ##DELETE CONTACT US PAGE LINK (...)
        del siteMenu[-1]                                                                      ##DELETE HELP PAGE LINK (BEACUSE HAVE NOT ANY PRODUCT)
                        ## SOME DETAIL ABOUT OTHER BLOCK →  CATEGORIES  ► [0]:MOBILE  , [1]:MOBILEACCESSORY , [2]:TABLET , [3]:LAPTOP , [4]:SMARTWACH
        siteMenuLinks=[]
        for links in siteMenu:
            siteMenuLinks.append(links.find('a',class_='nav-link'))

        MenuLinksURL=[{f'{(list(aTagLink.stripped_strings))[0]}':f"https://mimobs.com/{aTagLink['href']}"} for aTagLink in siteMenuLinks]   ##MAKE CURRECT FORMAT FOR CATEGORY LINKS (ADD SITE URL TO FIRST PART OF PAGES URL) AND ADD CATEGORY TITLE 

        i=0
        categoryBrands=[]
        for categoryLinks in siteMenu:
            productCompany=categoryLinks.select('ul.nav-subset li.nav-subset-item a.nav-subset-link')               ##SELECT CATEGORIES BRAND 
            if not productCompany==[]:                                                                              ##IF FIND BRANDS DELETE CATEGORY AND GET PRODUCTS WITH BRANDS NAME
                del MenuLinksURL[i]
                categoryBrands.append([{f'{(list(aTagLink.stripped_strings))[0]}':f"https://mimobs.com/{aTagLink['href']}"} for aTagLink in productCompany])
                i-=1
            i+=1
        categoryBrands=[category for lists in categoryBrands for category in lists]                             ##COMBIN DIFFRENT PRODUCT CATEGORY LIST IN A LIST
        MenuLinksURL=[brand for categories in (MenuLinksURL,categoryBrands) for brand in categories]            ##COMBIN BRANDS WITH ALL CATEGORIES
            
        return MenuLinksURL

    
    def GetEachProductData(self):
        allProductCategori=Mimobs.GetCategories(self)
        
        allProduct=[]
        for productPages in allProductCategori:
            for pageTitle,pageLink in productPages.items():
                pageDataContent=BeautifulSoup(requests.get(pageLink).content,'html.parser')                             ##GET EACH PRODUCT CONTENT
                getAllProductContainer=pageDataContent.select('div.col-6.col-sm-4.col-xl-3.mb-15 article.store-product.store-compact-product')       ##GET CONTAINER OF PRODUCTS IN PAGES 
                
                availible=True
                for container in getAllProductContainer:                                ##IN EACH PRODUCT PACK(CONTAINER)    
                    try:
                        product={'SellerCode':1,'SellerName':f'{self.sellerName}','ProductCategori':f'{pageTitle}','ProductName':None,'ProductLink':None,'ProductImage':None,'ProductPrice':None}   ##DEFINE A DICTIONARY FOR HOLD PRODUCTS DETAIL
                        
                        
                        productPrice=container.find('span',attrs={"itemprop":"offers"}).find('span')
                        # productPrice=productPrice.find('span')
                        product['ProductPrice']=productPrice.text   

                            ##GET PRODUCT URL
                        productURL=container.find('div',class_='store-product-image').find('a')
                        product['ProductLink']=f"{self.sellerLinkURL}{productURL['href']}"

                            #GET PRODUCT IMAGE
                        productImage=productURL.find('img')
                        product['ProductImage']=f"{self.sellerLinkURL}{productImage['src']}"

                            ##GET PRODUCT TITLE(NAME)
                        productTitle=container.select_one('h3 a')
                        product['ProductName']=list(productTitle.stripped_strings)
                        product['ProductName']=product['ProductName'][0]
                            ##GET PRODUCT PRICE


                        allProduct.append(product)
                    except:
                        availible=False
                        break
                    
                if availible==True:

                    resultPageCounter=pageDataContent.select('ul.pagination.mb-0 li a.page-link')
                    if not  resultPageCounter==[]:                              ##IF <ul class='pagination.mb-0'>   EXIST ► WE HAVE MORE RESULT PAGE
                        otherPageLinks=len(resultPageCounter)                ##IF WE HAVE TOP CONDITION APPEND IT TO OTHER RESULT PAGE


                    
                    for i in range(2,otherPageLinks):                                     
                        otherPage=f"{pageLink}?page={i}"                                                                   ##GO TO NEXT RESULT PAGE WITH MEDIA QUERY
                        pageDataContent=BeautifulSoup(requests.get(otherPage).content,'html.parser')                                ##GET OTHER RESULT PAGE CONTENT
                        getAllProductContainer=pageDataContent.select('div.col-6.col-sm-4.col-xl-3.mb-15 article.store-product.store-compact-product')           ##GET PRODUCTS BOX(CONTAINER) FROM OTHER SITE 
                        if not getAllProductContainer==[]:                                                  ##IF FIND PRODUCT BOX
                            ##print("*********************",otherPage)
                            for productBox in getAllProductContainer:                                ##IN EACH PRODUCT PACK(CONTAINER)    
                                try:
                                    product={'SellerCode':1,'SellerName':f'{self.sellerName}','ProductCategori':f'{pageTitle}','ProductName':None,'ProductLink':None,'ProductImage':None,'ProductPrice':None}   ##DEFINE A DICTIONARY FOR HOLD PRODUCTS DETAIL

                                    productPrice=productBox.find('span',attrs={"itemprop":"offers"}).find('span')
                                    # productPrice=productPrice.find('span')
                                    product['ProductPrice']=productPrice.text   

                                        ##GET PRODUCT URL
                                    productURL=productBox.find('div',class_='store-product-image').find('a')
                                    product['ProductLink']=f"{self.sellerLinkURL}{productURL['href']}"

                                        #GET PRODUCT IMAGE
                                    productImage=productURL.find('img')
                                    product['ProductImage']=f"{self.sellerLinkURL}{productImage['src']}"

                                        ##GET PRODUCT TITLE(NAME)
                                    productTitle=productBox.select_one('h3 a')
                                    product['ProductName']=list(productTitle.stripped_strings)
                                    product['ProductName']=product['ProductName'][0]
                                        ##GET PRODUCT PRICE


                                    allProduct.append(product)
                                except:
                                    availible=False
                                    break
                        else:
                            break
                    break        

        return allProduct
    
        
        
        
def GetAllProduct():
    sellerObject=Mimobs('Momobs',
        'https://mimobs.com/',
        'https://trustseal.enamad.ir/?id=201316&Code=e8Eh6eFgEluH2oNvEsrN',
        'https://mimobs.com/uploads/logo/01a317.jpg',
        'Qazvin',
        '1',
        'MimobsScraotModue'
        )
    return sellerObject.GetEachProductData()