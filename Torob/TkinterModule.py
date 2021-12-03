import tkinter as TKR                                                               ##IMPORT TKINTER FOR HANDLE GUI
from tkinter import Toplevel, ttk                                                             ##TTK HAVE A CLASS NAME:SCROLLBAR , IT COULD US MAKE SCROLLABLE FRAM
from ttkwidgets.autocomplete import AutocompleteCombobox                            ##IMPORT IT BEACUSE NEED TO USE AUTO COMPLETE FOR SEARCH ENTRY (SUGESTION WHILE U SEARCH)
from RegexSearch import GiveSearchKeyWord,SearchInCategory                                           ##WHEN CALL THIS FUNCTION OUR SEARCH KEYWORD WILL SEND TO DATABASE AND SEARCH TABLE WILL FILL WITH NEW RESULT
                                                                            ##########
import urllib.request                                                              ###
import io                                                                          ###  THIS THREE LIBRARY HELP US TO SHOW ONLINE IMAGES IN TKINTER.
from PIL import ImageTk, Image                                                     ###
                                                                            ##########
import webbrowser


### -----------------------------------------------------------------------------------------------------------------------------
    #WITH THIS FUNTION WE COULD GET MONITOR SIZE WITH TKINTER WINFO...
def GetMonitorScreenSize():
    screenSize = TKR.Tk()                                       ##FOR USING WINFO WE MOST DEFINE A MASTER.
    screenWidth = screenSize.winfo_screenwidth()                ##GET MONITOR WITH.
    screenHieght = screenSize.winfo_screenheight()              ##GET MONITOR HEIGHT.
    screenSize.destroy()                                        ##AFTER GET MONITOR SIZE DESTROY MASTER , BEACUSE EXIST MULTIPLE WINDOWS COULD MAKE INTERFERNCE AND MAKE BUG IN PROGRAM.
    return screenWidth, screenHieght

screenWidth, screenHieght = GetMonitorScreenSize()              ##DEFINE WIDTH AND HEIGHT AS GLOBAL VARIABLE FOR USE IN WHOLE PROGRAM.



### -----------------------------------------------------------------------------------------------------------------------------
    # FUNCTION TO MAKE FRAMES SCROLLABLE
    ##THIS FUNCTION MAKE A SCROLLABLE FRAME FOR US
def PageScrollbar(frameName):
    scrollCanvas = TKR.Canvas(master=frameName)
    scrollCanvas.pack(side=TKR.LEFT, fill=TKR.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(frameName, orient=TKR.VERTICAL, command=scrollCanvas.yview)
    my_scrollbar.pack(side=TKR.RIGHT, fill=TKR.Y)

    scrollCanvas.configure(yscrollcommand=my_scrollbar.set)
    scrollCanvas.bind('<Configure>', lambda e: scrollCanvas.configure(scrollregion=scrollCanvas.bbox("all")))

    second_frame = TKR.Frame(scrollCanvas)                                      ## CREAT ANOTHER FRAME INSIDE CANVAS
    second_frame.pack()

    scrollCanvas.create_window((0, 0), window=second_frame, anchor="nw")        ##ADD THAT NEW FRAME TO A WINDOW IN THE CANVAS
    scrollCanvas.pack()
    
    return second_frame





### -----------------------------------------------------------------------------------------------------------------------------
    ##MAKE A AUTO COMPLETE, IT USES IN SEARCH ENTRY FOR SUGGESTION
    ##IN THIS FUNCTION WE JUST DEFINE A LIST OF WORDS(SUGGESTION) AND AFTER USE IT IN COMPLETE VALUE FILED IN AUTOCOMPLETECOMBOBOX OBJECT
def AutoCompleteComboBoxValues():
    searchValues = [
        ' سامسونگ', 'اپل', 'شیائومی', 'نوکیا', 'ال جی', 'هوآوی',
        'مچ بند','شارژر','هدفون','اسپیکر ','هارد'
    ]
    return searchValues
    


###---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ## IN THIS CLASS WE GONNA MAKE A FIXED NAVBAR AND USE SCROLLABLE FRAME IN THIS CLASS FOR MAKE PAGE BODY SCROLLABLE
class FixedNavbar(TKR.Toplevel):
    masterName=None                                                     ##DEFINE THIS BECAUSE CANT USE SELF IN BackToHome FUNCTION
    def __init__(self, masterName):
        self.masterName = masterName                                    ## GET MASTER NAME OF TKINTER PAGE
        FixedNavbar.masterName=self.masterName                          ## SET MASTER NAME FOR USE IN BackToHome FUNCTION

    

    def CreateNavbar(self):                                             ## THIS FUNCTION CREATE FIXED NAVBAR

        def BackToHome(event):                                              ## BACK HOME BUTTON , WHEN CLICKED GO TO HOME PAGE
            self.masterName.destroy()                                       ## CLOSE THIS FRAME AND DELETE DATA
            import SearchHomeGUI                                            ## OPEN HOME PAGE,(WHEN WE IMPORT A TKINTER FILE IT WILL OPEN AND NO ACTION NEEDED , THAT'S WHY E IMPORT IT IN FUNCTION)
    
        def SetKeyword(event):                                          ## THIS FUNCTION CALL WHENE PRESS SEARCH BUTTON
            searchKeyword = self.searchInput.get()                      ## GET SEARCH KEYWORD THAT TYPED IN ENTRY BOX
            self.masterName.destroy()                                   ## DESTROY THIS FRAM
            GiveSearchKeyWord(searchKeyword)                            ##SEND SEARCH KEYWORD TO OTHER MODULE FOR SAVED RESULTS IN SEARCH RESULT TABLE IN DATABASE
        
        def GetCategory(keySearch):
            self.masterName.destroy()                                   ## DESTROY THIS FRAM
            SearchInCategory(keySearch)                            ##SEND SEARCH KEYWORD TO OTHER MODULE FOR SAVED RESULTS IN SEARCH RESULT TABLE IN DATABASE
        
        self.masterName.attributes("-fullscreen", True)                 ## DEFINE OUR PROGRAM WONDOW AS FULL SCREENAND NOT RESIZIBLE 
        self.masterName.iconbitmap('..\\TOROB\\img\\torobLogo.ico')     ## DEFINE PROGRAM WONDOW FAVICON
        self.masterName.title('تُرب - جستجوی کالا')                      ## DEFINE PROGRAM WONDOW TITLE
        
    ## START CATEGORI LABLES
        ## DEFINE CATEORIS , WHEN CLICK ON THIS LINKS GO TO PAGE HAVE PRODUCTS WITH SAME CATEGORI
            ## MOBILE CATEGORI
        self.mobileCategori = TKR.Label(
                                        self.masterName,
                                        text='موبایل',
                                        fg='#4a4a4a',
                                        cursor='hand2',
                                        font=('IRANYekanWeb 14')
                                        )
        self.mobileCategori.pack()
        ## WITH THIS LINE WE CAN DETERMINE SIZE AND POSITION
        self.mobileCategori.place(x=screenWidth-(screenWidth/15), y=screenHieght-(screenHieght/1.14))
        self.mobileCategori.bind('<ButtonPress>', lambda event ,keySearch='گوشی های':GetCategory(keySearch))

            ## MOBILE ACCESSORY CATEGORIES
        self.mobileAccessoryCategori = TKR.Label(
                                                self.masterName,
                                                text='تجهیزات موبایل',
                                                fg='#4a4a4a',
                                                cursor='hand2',
                                                font=('IRANYekanWeb 14')
                                                )
        self.mobileAccessoryCategori.pack()
        self.mobileAccessoryCategori.place(x=screenWidth-(screenWidth/5.5), y=screenHieght-(screenHieght/1.14))
        self.mobileAccessoryCategori.bind('<ButtonPress>', lambda event ,keySearch='انواع شارژر ':GetCategory(keySearch))

            ## TABLET CATEGORIES
        self.tabletCategori = TKR.Label(
                                        self.masterName,
                                        text='تبلت',
                                        fg='#4a4a4a',
                                        cursor='hand2',
                                        font=('IRANYekanWeb 14')
                                        )
        self.tabletCategori.pack()
        self.tabletCategori.place(x=screenWidth-(screenWidth/4.2), y=screenHieght-(screenHieght/1.14))
        self.tabletCategori.bind('<ButtonPress>', lambda event ,keySearch='تبلت':GetCategory(keySearch))

            ## LAPTOP CATEGORIES
        self.laptopCategori = TKR.Label(
                                        self.masterName,
                                        text='لپتاپ',
                                        fg='#4a4a4a',
                                        cursor='hand2',
                                        font=('IRANYekanWeb 14')
                                        )
        self.laptopCategori.pack()
        self.laptopCategori.place(x=screenWidth-(screenWidth/3.3), y=screenHieght-(screenHieght/1.14))
        self.laptopCategori.bind('<ButtonPress>', lambda event ,keySearch='لپتاپ':GetCategory(keySearch))

            ## BAND AND SAMRT WATCH CATEGORIES
        self.smartWatch = TKR.Label(
                                    self.masterName,
                                    text='مچ بند و ساعت هوشمند',
                                    fg='#4a4a4a',
                                    cursor='hand2',
                                    font=('IRANYekanWeb 14')
                                    )
        self.smartWatch.pack()
        self.smartWatch.place(x=screenWidth-(screenWidth/2.2),y=screenHieght-(screenHieght/1.14))
        self.smartWatch.bind('<ButtonPress>', lambda event ,keySearch='مچ بند و ساعت هوشمند':GetCategory(keySearch))

        torobImageAddress = TKR.PhotoImage(file='..\\TOROB\\img\\torob_logo.png')                             ## DEFINE LOGO IMAGE
        # torobImageAddress=torobImageAddress.subsample(2,2)                                                  ##RESIZE IMAGE SIZE
        torobImage = TKR.Label(self.masterName, image=torobImageAddress)                                      ## TOROB IMAGE LOGO IN RIGHT CORNER OF THE PAGE
        torobImage.pack()
        torobImage.place(x=screenWidth-(screenWidth/20),y=screenHieght-(screenHieght/1.035))

            # TOROB NAME TITLE
        self.torobTitle = TKR.Label(
                                    self.masterName,
                                    text="تُرب",
                                    fg='#d73948',
                                    font=('IRANYekanWeb 25')
                                    )
        self.torobTitle.pack()
        self.torobTitle.place(x=screenWidth-(screenWidth/10),y=screenHieght-(screenHieght/1.035))

            # SEARCH INPUT(BOX FOR ENTER SEARCH WORDS)
        self.searchInput = AutocompleteCombobox(
                                                master=self.masterName,
                                                completevalues=AutoCompleteComboBoxValues(),
                                                font=('IRANSans 16')
                                                )
        self.searchInput.pack()
        self.searchInput.place(width=screenWidth/3, height=screenHieght-(screenHieght/1.06),x=screenWidth-(screenWidth/2.23), y=screenHieght-(screenHieght/1.04))

            # SEARCH BUTTON
        self.searchButton = TKR.Button(
                                        master=self.masterName,
                                        text='جستجوی کالا',
                                        width=20,
                                        bg='#d73948',
                                        fg='#fff',
                                        cursor='hand2',
                                        font=('IRANSans 12')
                                        )
        self.searchButton.pack()
        self.searchButton.place(width=screenWidth/12, x=screenWidth -(screenWidth/1.85), y=screenHieght-(screenHieght/1.04))
        self.searchButton.bind('<ButtonPress>', SetKeyword)

            # CLOSE APP BUTTON
        self.closeButton = TKR.Button(
                                    master=self.masterName,
                                    text='بستن برنامه',
                                    height=2,
                                    bg='#ab001c',
                                    fg='#fff',
                                    cursor='hand2',
                                    font=('IRANSans 12'),
                                    command=self.masterName.destroy
                                    )
        self.closeButton.pack()
        self.closeButton.place(width=160, x=screenWidth-(screenWidth/1.02), y=screenHieght-(screenHieght/1.001))

            # Home BUTTON
        self.homeButton = TKR.Button(
                                    master=self.masterName,
                                    text='صفحه اصلی',
                                    height=2,
                                    bg='#3f62e0',
                                    fg='#fff',
                                    cursor='hand2',
                                    font=('IRANSans 12')
                                    )
        self.homeButton.pack()
        self.homeButton.place(width=160, x=screenWidth-(screenWidth/1.02), y=screenHieght-(screenHieght/1.1))
        self.homeButton.bind('<Button>', BackToHome)

        # FINISH CATEGORIES LABEL
        # TOP DIVIDER(THIS LINE DIVIDE CATEGORIES FROM BODY)
        self.topDivider = TKR.Label(
                                    self.masterName,
                                    text=1000*"_",
                                    fg='#a6a6a6',
                                    )
        self.topDivider.pack()
        self.topDivider.place(x=0, y=screenHieght-(screenHieght/1.21))
        ##FINISH NAVBAR SECTION        

            ##DEFINE BODY CONTAINER(FRAME)
        self.bodyContainer = TKR.Frame(self.masterName)
        self.bodyContainer.pack(fill=TKR.BOTH, expand=1)
        self.bodyContainer.place(width=screenWidth, height=screenHieght -(screenHieght/5), x=0, y=screenHieght-(screenHieght/1.24))





### ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ## THIS CLASS MAKE PRODUCTS BOXES AND RETURN BOXES TO THE NUMBER OF PRODUCT LIST LEN GAVE
class ProductBox:
    def __init__(self, productsList):
        self.productsList = productsList

    ### CREAT BOX FOR EACH PRODUCT (THREE BOX IN A ROW→ ONE TRIPLEX LIST = ONE ROW)
    @staticmethod
    def CreateProductList_WithBoxSizes(self):
            ## THIS CONDITION CHECK LEN OF PRODUCT LIST (IF ITS EMPTY ==> THIS FUNCTION COMMAND NOT RUN)
        if len(self.productsList) >= 1:
            self.triplexProductsList = []               ## THIS LIST HOLD LISTS INCLUDES THREE PRODUCT(HOLD triplexList==> MEAN HOLD ALL ROWS , ITS LIKE A CONTAINER)
            self.triplexList = []                       ## THIS LIST HOLD THREE PRODUCT FOR EACH ROW

            i = 1
            for product in self.productsList:
                self.triplexList.append(product)
                if i % 3 == 0:              ## triplexList HOLD JUST THREE PRODUCT IN A ROWS , WHEN THREE PRODUCT COMPLETELY APPEND TO IT , triplexList APPEN TO triplexProductsList AND MAKE SELF EMPTY FOR NEW ROW
                    self.triplexProductsList.append(self.triplexList)       ## APPEND A ROW TO OUR VODY CONTAINER (THREE PRODUCT IS A ROW)
                    self.triplexList = []                                   ## CLEAR FOR ADD NEW THREE PRODUCT , EACH TRIPLEX LIST
                    ## IF OUR PRODUCT WERE'NT DEVISIBLE ON 3 AND BE THE LAST PRODUCT APPEND IT TO CONTAINER LIST TOO
                if len(self.productsList) % 3 != 0 and i == len(self.productsList):
                    self.triplexProductsList.append(self.triplexList)
                    break                                                   ## THIS WAS THE LAST ONE SO GET OUT THE LOOP               
                i += 1

            self.productY = 50                                          ## FIRST HEIGHT FROM TOP
            self.boxWidth = screenWidth/4                               ## EACH PRODUCT BOX WIDTH             
            self.boxHeight = 550                                        ## EACH PRODUCT BOX HEIGHT       
            for row in self.triplexProductsList:                        ## EACH ROW(THREE PRODUCT) IN BODY CONTAINER
                for i in range(0, len(row)):                            ## THIS LOOP WILL HELP FOR MAKE EACH PRODUCT BOX POSITION IN PAGE
                    if i == 0:                                          ## IF IT WAS THE FIRST PRODUCT IN ROW IT'S POSITION IS...
                        row[i].append(self.boxWidth)                    ## WIDTH
                        row[i].append(self.boxHeight)                   ## HEIGHT
                        row[i].append(screenWidth-(screenWidth/3.2))    ## X
                        row[i].append(self.productY)                    ## Y
                    elif i == 1:                                        ## IF IT WAS THE SECOND PRODUCT IN ROW IT'S POSITION IS...
                        row[i].append(self.boxWidth)
                        row[i].append(self.boxHeight)
                        row[i].append(screenWidth-(screenWidth/1.6))
                        row[i].append(self.productY)
                    else:                                               ## IF IT WAS THE THIRD PRODUCT IN ROW IT'S POSITION IS...
                        row[i].append(self.boxWidth)
                        row[i].append(self.boxHeight)
                        row[i].append(screenWidth-(screenWidth/1.06))
                        row[i].append(self.productY)

                self.productY += 650                                    ## SUM PRODUCT BOX HEIGHT AND MARGIN TOP FOR SET NEW HEIGHT FOR NEW ROW

            return self.triplexProductsList                             ##AFTER ALL RETURN CONTAINER INCLUDE PRODUCT BOX IN ROWS


    ## THIS FUNCTION SET ALL PRODUCT DATA IN EACH PRODUCT BOX
    def CreateProductBoxFrame(self,root, masterName):

        products = ProductBox.CreateProductList_WithBoxSizes(self)          ## GET CONTAINER OF ALL ROWS(triplexProductsList)
        if products == None:                                                ## IF NO PRODUCTS RETURNED:
            frameHeightSize = screenHieght-200                              ## HEIGHT OF BODY CONTAINER
            productsFrame = TKR.Frame(masterName)
            productsFrame.pack()
            productsFrame.place(width=screenWidth, height=frameHeightSize, x=0, y=screenHieght-(screenHieght/1))

                ##THIS CONDITION WHENE NO PRODUCT FOUND , THIS LABLE SHOW TO CLINET NO PRODUCTS FOUNDED
            notFound = TKR.Label(
                                master=masterName,
                                text="محصول مورد نظر یافت نشد",
                                font=('IRANYekanWeb 30')
                                )
            notFound.pack()
            notFound.place(x=(screenWidth)/2, y=100)
            return frameHeightSize
        
        else:
            frameHeightSize = len(products)*650                         ##BODY CONTANER HEIGH = NUMBER OF PRODUCT * 650
            productsFrame = TKR.Frame(masterName)
            productsFrame.pack()
            productsFrame.place(width=screenWidth, height=frameHeightSize, x=0, y=screenHieght-(screenHieght/1))


            productTitleLable=[]
            for rowsList in products:                               ## products CONTAINE LISTS THOSE LIST CONTAINE THREE LIST
                for eachRow in rowsList:                            ## EACH LIST IS A PRODUCT
                    
                    def EnterData(productList):
                        productList=productList
                        productRoot=Toplevel()
                        productRoot.attributes("-fullscreen", True)
                        # Navbar=FixedNavbar(productRoot)
                        # Navbar.CreateNavbar()
                        screenWidth,screenHieght=GetMonitorScreenSize()
                        def OpenSite(event):
                            webbrowser.open(f"{productList[7]}")
                        bodyContainer=TKR.Frame(productRoot)
                        # bodyContainer.pack(fill=TKR.BOTH, expand=1)
                        bodyContainer.place(width=screenWidth,height=screenHieght,x=0,y=screenHieght)

                        mainScrollable=PageScrollbar(productRoot)
                        mainScrollable.config(width=screenWidth,height=screenHieght+250,bg='#fff')

                        closeButton = TKR.Button(
                                    master=mainScrollable,
                                    text='بستن برنامه',
                                    height=2,
                                    bg='#ab001c',
                                    fg='#fff',
                                    cursor='hand2',
                                    font=('IRANSans 12'),
                                    command=root.destroy
                                    )
                        closeButton.pack()
                        closeButton.place(width=160, x=screenWidth-(screenWidth/1.02), y=screenHieght-(screenHieght/1.001))
                        
                        imageFrame=TKR.Frame(mainScrollable,bg='#fff')
                        imageFrame.pack()
                        imageFrame.place(width=screenWidth-(screenWidth/1.35),height=screenHieght/1.65,x=screenWidth-(screenWidth/3),y=screenHieght-(screenHieght/1.3))

                        imageWidth = int((productList[-4])/1.1)
                        imageHeight = int((productList[-3]-120)/1.1)
                        ## GET ONLINE IMAGES FOR SHOW IN TKINTER
                        raw_data = urllib.request.urlopen(productList[5]).read()
                        productImage = Image.open(io.BytesIO(raw_data))
                        productImage = productImage.resize((imageWidth, imageHeight))   
                        productImage = ImageTk.PhotoImage(productImage)                 
                        productImageLable=TKR.Label(imageFrame,image=productImage)
                        productImageLable.pack()


                        productSellerLable=TKR.Message(
                                                    master=mainScrollable,
                                                    text=':فروشگاه',
                                                    fg='#000',
                                                    font=('IRANSans 12'),
                                                    width=100,
                                                    bg='#fff'
                                                    
                        )
                        productSellerLable.pack()
                        
                        productSellerLable.place(x=screenWidth-(screenWidth/2.3),y=screenHieght-(screenHieght/1.14))
                        productSeller=TKR.Message(
                                                    master=mainScrollable,
                                                    text=f'{productList[1]}',
                                                    fg='#000',
                                                    font=('IRANSans 12'),
                                                    bg='#fff'
                        )
                        productSeller.pack()
                        productSeller.place(x=screenWidth-(screenWidth/2),y=screenHieght-(screenHieght/1.14))
                        
                        divider=TKR.Label(master=mainScrollable,text=50*'_',bg='#fff')
                        divider.pack()
                        divider.place(x=screenWidth-(screenWidth/1.8),y=screenHieght-(screenHieght/1.2))
                        

                        productTitleFrame=TKR.Frame(mainScrollable,bg='#fff')
                        productTitleFrame.pack()
                        productTitleFrame.place(width=screenWidth-(screenWidth/2.5),height=screenHieght/5,x=screenWidth-(screenWidth/1.05),y=screenHieght-(screenHieght/1.27))

                        productTitle=TKR.Message(
                                                    master=productTitleFrame,
                                                    text=f'{productList[4]} : نام محصول',
                                                    fg='#000',
                                                    font=('IRANSans 12'),
                                                    width=900,
                                                    bg='#fff'

                        )
                        productTitle.pack()

                        productPrice=TKR.Message(
                                                    master=mainScrollable,
                                                    text=f'{productList[6]}',
                                                    fg='#000',
                                                    bg='#32a852',
                                                    font=('IRANSans 16'),
                                                    width=900,


                        )
                        productPrice.pack()
                        productPrice.place(width=screenWidth-(screenWidth/1.34),height=screenHieght/8,x=screenWidth-(screenWidth/1.6),y=screenHieght-(screenHieght/1.9))

                        buyButton=TKR.Button(
                                                mainScrollable,
                                                bg='#D73948',
                                                fg='#000',
                                                font=('IRANSans 16'),
                                                cursor='hand2',
                                                text='خرید محصول'
                                                )
                        buyButton.pack()
                        buyButton.place(width=screenWidth-(screenWidth/1.34),height=screenHieght/8,x=screenWidth-(screenWidth/1.6),y=screenHieght-(screenHieght/2.8))
                        buyButton.bind('<Button>',OpenSite)


                        pageFooter=Footer(mainScrollable)
                        pageFooter.SetFooter(screenHieght+200)



                    ## DEFINE EACH PRODUCT BOX FRAME
                    productBoxFrame = TKR.Frame(productsFrame, bg='#fff', cursor="hand2")
                    productBoxFrame.pack()
                    productBoxFrame.place(width=eachRow[-4], height=eachRow[-3], x=eachRow[-2], y=eachRow[-1])
                    productBoxFrame.bind('<Button>',lambda event,boxNum=eachRow:EnterData(boxNum))
                    

                    ## DEFINE IMAGE BOX FRAME IN PRODUCT BOX FRAME
                    productBoxImageFrame = TKR.Frame(productBoxFrame, cursor="hand2")
                    productBoxImageFrame.pack()
                    productBoxImageFrame.place(width=eachRow[-4], height=eachRow[-3]-120, x=0, y=0)
                    
                    ## DEFINE IMAGES WIDTH AND HEIGHT FOR USE IN IMAGE BOX FRAME
                    imageWidth = int((eachRow[-4])/1.2)
                    imageHeight = int((eachRow[-3]-120)/1.2)
                    ## GET ONLINE IMAGES FOR SHOW IN TKINTER
                    raw_data = urllib.request.urlopen(eachRow[5]).read()
                    productImage = Image.open(io.BytesIO(raw_data))
                    productImage = productImage.resize((imageWidth, imageHeight))       ## RESIZE IMAGE SIZE
                    productImage = ImageTk.PhotoImage(productImage)                     
                        ##SET IMAGE IN IMAGE BOX FRAME
                    productImageLable =TKR.Label(
                                                master=productBoxImageFrame,
                                                image=productImage,
                                                bg="#fff"
                                                )
                    productImageLable.image = productImage  # KEEP A REFRENCE OF IMAGE, WITHOUT THIS LINE IT WILL RETURN US BLANK FRAME
                    productImageLable.pack(side='top', fill='both', expand='yes')
                    productImageLable.bind('<Button>',lambda event,boxNum=eachRow:EnterData(boxNum))

                    
                    ## DEFINE TITLE BOX FRAME IN PRODUCT BOX FRAME
                    productBoxTitleFrame = TKR.Frame(productBoxFrame, bg="#fff", cursor="hand2")
                    productBoxTitleFrame.pack()
                    productBoxTitleFrame.place(width=eachRow[-4], height=80, x=0, y=eachRow[-3]-120)
                    ##SET PRODUCT TITLE IN PRODUCT TITLE BOX 
                    productTitleLable=TKR.Message(
                                                master=productBoxTitleFrame,
                                                text=eachRow[4],
                                                width=300,
                                                bg="#fff",
                                                font=('IRANYekanWeb 12')
                                                )
                    productTitleLable.pack()
                    # productTitleLable[j].bind('<Button>',partial(EnterData,eachRow))
                    productTitleLable.bind('<Button>',lambda event,boxNum=eachRow:EnterData(boxNum))


                    ## DEFINE PRICE BOX FRAME IN PRODUCT BOX FRAME
                    productBoxPriceFrame = TKR.Frame(productBoxFrame, cursor="hand2", bg="#D73948")
                    productBoxPriceFrame.pack()
                    productBoxPriceFrame.place(width=eachRow[-4], height=40, x=0, y=eachRow[-3]-40)
                    ##SET PRODUCT PRICE
                    productPriceLable =TKR.Label(
                                                master=productBoxPriceFrame,
                                                text=eachRow[6],
                                                bg="#D73948",
                                                font=('IRANYekanWeb 15')
                                                )
                    productPriceLable.pack()

            return (frameHeightSize+400)        ##RETURN NEW BODY CONTAINER HEIGHT

    def __str__(self):
        return str(self.triplexProductsList)



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
##THIS FUNCTION WILL CREATE FOOTER FOR PAGES
class Footer:
    def __init__(self, masterName):
        self.masterName = masterName

    ##RETURN FOOTER FRAME
    def SetFooter(self, newHeight):
        self.newHeight = newHeight
        
        ## FOOTER FRAME
        footer = TKR.Frame(
                            master=self.masterName,
                            bg='black'
                            )
        footer.pack()
        footer.place(width=screenWidth, height=260,x=0, y=(self.newHeight)-260)

        ## FOOTER RIGHT SECTION
        footerRightInfo = TKR.Frame(master=footer)
        footerRightInfo.pack()
        footerRightInfo.place(width=(screenWidth)/3,height=250, x=screenWidth-(screenWidth)/3, y=10)

        ContactUsTitle = TKR.Label(
                                    master=footerRightInfo,
                                    text="راه های ارتباطی",
                                    font=('IRANYekanWeb 24')
                                    )
        ContactUsTitle.pack()
        ContactUsTitle.place(x=(screenWidth)/6, y=20)

        phoneNumber = TKR.Label(
                                master=footerRightInfo,
                                text="شماره تماس: 91008676 (با پیش شماره 021)",
                                font=('IRANYekanWeb 12')
                                )
        phoneNumber.pack()
        phoneNumber.place(x=(screenWidth)/11, y=90)

        address = TKR.Label(
                            master=footerRightInfo,
                            text='آدرس: تهران، خیابان آزادی شرق به غرب، بعد از دانشگاه شریف\n کوچه صادقی، پلاک 29،پارک علم و فناوری دانشگاه شریف،\n طبقه دوم، واحد 3',
                            font=('IRANYekanWeb 11')
                            )
        address.pack()
        address.place(x=(screenWidth)/25, y=130)

        postalCode = TKR.Label(
                                master=footerRightInfo,
                                text='کد پستی: 1458883499',
                                font=('IRANYekanWeb 13')
                                )
        postalCode.pack()
        postalCode.place(x=(screenWidth)/5.5, y=200)

        ##FOOTER MIDDLE SECTION
        footerMiddleInfo = TKR.Frame(master=footer)
        footerMiddleInfo.pack()
        footerMiddleInfo.place(width=(screenWidth)/3,height=250, x=screenWidth-(screenWidth/1.5), y=10)

        sellerRegisterTitle = TKR.Label(
                                        master=footerMiddleInfo,
                                        text="ثبت نام فروشندگان",
                                        font=('IRANYekanWeb 24'),
                                        )
        sellerRegisterTitle.pack()
        sellerRegisterTitle.place(x=(screenWidth)/7, y=20)

        registerInfo = TKR.Label(
                                master=footerMiddleInfo,
                                text='به راحتی و با چند کلیک به جمع ما بپیوندید',
                                font=('IRANYekanWeb 11')
                                )
        registerInfo.pack()
        registerInfo.place(x=(screenWidth)/10, y=75)

        registerLink = TKR.Label(
                                master=footerMiddleInfo,
                                text='ثبت نام در تُرب',
                                font=('IRANYekanWeb 16'),
                                cursor="hand2",
                                fg='blue'
                                )
        registerLink.pack()
        registerLink.place(x=(screenWidth)/5.5, y=130)

        ## FOOTER LEFT SECTION
        footerLeftInfo = TKR.Frame(master=footer)
        footerLeftInfo.pack()
        footerLeftInfo.place(width=(screenWidth)/3, height=250, x=0, y=10)

        sellerRegisterTitle = TKR.Label(
                                        master=footerLeftInfo,
                                        text="بهترین ها در تُرب",
                                        font=('IRANYekanWeb 24')
                                        )
        sellerRegisterTitle.pack()
        sellerRegisterTitle.place(x=(screenWidth)/6, y=20)

        registerLink = TKR.Label(
                                master=footerLeftInfo,
                                text='لیست فروشگاه هایی که عضو خانواده تُرب شدند',
                                font=('IRANYekanWeb 11')
                                )
        registerLink.pack()
        registerLink.place(x=(screenWidth)/16, y=90)

        sellersList = TKR.Label(
                                master=footerLeftInfo,
                                text='لیست فروشگاه ها',
                                font=('IRANYekanWeb 16'),
                                cursor="hand2",
                                fg='blue'
                                )
        sellersList.pack()
        sellersList.place(x=(screenWidth)/5, y=150)
        self.masterName.mainloop()
        return footer                               ## RETURN FOOTER FRAME