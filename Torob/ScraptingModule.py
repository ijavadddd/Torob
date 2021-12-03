from abc import ABC,abstractmethod 



class Seller(ABC):
    def __init__(self,sellerName,sellerLinkURL,sellerEnamadURL,sellerLogoURL,sellerContactInfo,sellerStatus,sellerModuleName):
        self.sellerName         = sellerName
        self.sellerLinkURL      = sellerLinkURL
        self.sellerEnamadURL    = sellerEnamadURL
        self.sellerLogoURL      = sellerLogoURL
        self.sellerContactInfo  = sellerContactInfo
        self.sellerStatus       = sellerStatus
        self.sellerModuleName   = sellerModuleName
    
    @abstractmethod
    def GetCategories(self):
        pass
    
    @abstractmethod
    def GetEachProductData(self):
        pass


#-----------------------------------------------------------------------------------------------------------------------------------------
# class ProductsModel:
    # def __init__(self,sellerCode,sellerName,productCategory,productTitle,productImage,productPrice,productURL):
        # self.sellerCode     =   sellerCode
        # self.sellerName     =   sellerName
        # self.productCategory=   productCategory
        # self.productTitle   =   productTitle
        # self.productImage   =   productImage
        # self.productPric    =   productPrice
        # self.productURL     =   productURL
        # 
    # def __hash__(self):
        # productHash=hash(self.productLink)
        # return productHash
    # 
    # def SetProduct(self):
        # self.product={
                # 'SellerCode'        :   f'{self.sellerCode}',
                # 'SellerName'        :   f'{self.sellerName}',
                # 'ProductCategori'   :   f'{self.productCategory}',
                # 'ProductTitle'      :   f'{self.productTitle}',
                # 'ProductImage'      :   f'{self.productImage}',
                # 'ProductPrice'      :   f'{self.productPric}',
                # 'ProductURL'        :   f'{self.productURL}'
                # }
        # 
        # return self.product
    # 
    # def SendDict(self):
        # b=ProductsModel.SetProduct
        # return vars(b)
        # 
    # def __str__(self):
        # productInfo=f'''
                    # Seller Code          :   {self.sellerCode}
                    # Seller Title         :   {self.sellerName}
                    # Product Category     :   {self.productCategory}
                    # Product Title        :   {self.productTitle}
                    # Product Image Link   :   {self.productImage}
                    # Product Price        :   {self.productPric}
                    # Product URL          :   {self.productURL}
                    # '''
        # return productInfo