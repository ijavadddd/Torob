import tkinter
from RegexSearch import GiveSearchKeyWord,SearchInCategory 

def SetKeyword(event):
    global searchInput
    searchKeyword=searchInput.get()
    root.destroy()
    GiveSearchKeyWord(searchKeyword)





root=tkinter.Tk()
root.attributes("-fullscreen", True)

screenWidth=root.winfo_screenwidth()
screenHieght=root.winfo_screenheight()
myWidth=(screenWidth/2)-((screenWidth-200)/2)
myheight=(screenHieght/2)-((screenHieght-200)/2)
root.geometry("%dx%d+%d+%d"%(screenWidth-200,screenHieght-200,myWidth,myheight))
# root.resizable(0,0)
root.title('تُرب - جستجوی کالا')
root.iconbitmap('..\\TOROB\\img\\torobLogo.ico')

def GetCategory(keySearch):
    root.destroy()  
    SearchInCategory(keySearch)

###START CATEGORI LABLES
    ###DEFINE CATEORIS , WHEN CLICK ON THIS LINKS GO TO PAGE HABE PRODUCTS WITH SAME CATEGORI
    
    ##MOBILE CATEGORIES
mobileCategori=tkinter.Label(
                            root,
                            text='موبایل',
                            fg='#4a4a4a',
                            cursor='hand2',
                            font=('IRANSans 12')
                            )   
mobileCategori.pack()
mobileCategori.place(x=screenWidth-(screenWidth/6),y=screenHieght-(screenHieght/1.04))                  ##WITH THIS LINE WE CAN DETERMINE WICH ELEMENT WHERE BE 
mobileCategori.bind('<ButtonPress>', lambda event ,keySearch='گوشی های':GetCategory(keySearch))

    ##MOBILE ACCESSORY CATEGORIES
mobileAccessoryCategori=tkinter.Label(
                            root,
                            text='تجهیزات موبایل',
                            fg='#4a4a4a',
                            cursor='hand2',
                            font=('IRANSans 12')
                            )   
mobileAccessoryCategori.pack()
mobileAccessoryCategori.place(x=screenWidth-(screenWidth/3.2),y=screenHieght-(screenHieght/1.04))
mobileAccessoryCategori.bind('<ButtonPress>', lambda event ,keySearch='انواع شارژر ':GetCategory(keySearch))

    ##TABLE CATEGORIES
tabletCategori=tkinter.Label(
                            root,
                            text='تبلت',
                            fg='#4a4a4a',
                            cursor='hand2',
                            font=('IRANSans 12')
                            )   
tabletCategori.pack()
tabletCategori.place(x=screenWidth-(screenWidth/2.5),y=screenHieght-(screenHieght/1.04))
tabletCategori.bind('<ButtonPress>', lambda event ,keySearch='تبلت':GetCategory(keySearch))

    ##LAPTOP CATEGORIES
laptopCategori=tkinter.Label(
                            root,
                            text='لپتاپ',
                            fg='#4a4a4a',
                            cursor='hand2',
                            font=('IRANSans 12')
                            )   
laptopCategori.pack()
laptopCategori.place(x=screenWidth-(screenWidth/2),y=screenHieght-(screenHieght/1.04))
laptopCategori.bind('<ButtonPress>', lambda event ,keySearch='لپتاپ':GetCategory(keySearch))

    ##BAND AND SAMRT WATCH CATEGORIES
smartWatch=tkinter.Label(
                            root,
                            text='مچ بند و ساعت هوشمند',
                            fg='#4a4a4a',
                            cursor='hand2',
                            font=('IRANSans 12')
                            )   
smartWatch.pack()
smartWatch.place(x=screenWidth-(screenWidth/1.5),y=screenHieght-(screenHieght/1.04))
smartWatch.bind('<ButtonPress>', lambda event ,keySearch='مچ بند و ساعت هوشمند':GetCategory(keySearch))

    ##TOP DIVIDER(THIS LINE DIVIDE CATEGORIES FROM BODY)
topDivider=tkinter.Label(
                            root,
                            text=1000*"_",
                            fg='#a6a6a6',
                            
)
topDivider.pack()
topDivider.place(x=0,y=screenHieght-(screenHieght/1.08))

###FINISH CATEGORIES LABEL




torobImageAddress=tkinter.PhotoImage(file='..\\TOROB\\img\\torob_logo.png')                                         ##DEFINE A IMAGE
# torobImageSize=torobImageAddress.subsample(7,7)                                                                   ##RESIZE IMAGE SIZE
torobImage=tkinter.Label(root,image=torobImageAddress)                                                              ##TOROB IMAGE LOGO IN MIDDEL OF THE PAGE
# torobImage.grid(row=1,rowspan=2,column=0,columnspan=3,padx=(1000,0),pady=(180,0))
torobImage.pack()
torobImage.place(x=screenWidth-(screenWidth/2.81),y=screenHieght-(screenHieght/1.23))

##TOROB NAME TITLE
torobTitle=tkinter.Label(
                            root,
                            text="تُرب",
                            fg='#d73948',
                            font=('IRANSans 25')
)
torobTitle.pack()
torobTitle.place(x=screenWidth-(screenWidth/2.48),y=screenHieght-(screenHieght/1.2))

##SEARCH TITLE
searchTitle=tkinter.Label(
                            root,
                            text="موتور جستجوی هوشمند خرید",
                            fg='#000',
                            font=('IRANSans 25')
                            )
searchTitle.pack()
searchTitle.place(width=screenWidth/3,x=screenWidth-(screenWidth/1.45),y=screenHieght-(screenHieght/1.3))


##SEARCH INPUT(BOX FOR ENTER SEARCH WORDS)
searchInput=tkinter.Entry(
                            master=root,
                            
                            font=('Georgia 25')
                            )
# searchInput.bind('<ButtonPress>',SendSearchKeyword)                                 ##WHEN BUTTON CLICKED SEND SEARCH KEYWORD TO NEW PAGE FOR GET PRODUCTS
searchInput.pack()
searchInput.place(width=screenWidth/3,x=screenWidth-(screenWidth/1.6),y=screenHieght-(screenHieght/1.5))

##SEARCH BUTTON
searchButton=tkinter.Button(
                            master=root,
                            text='جستجوی کالا',
                            width=20,
                            bg='#d73948',
                            fg='#fff',
                            cursor='hand2',
                            font=('IRANSans 12')
                            
                            )
searchButton.bind('<ButtonPress>',SetKeyword)                    ##WHEN BUTTON CLICKED GO TO SearchRsult.py
# searchButton.bind('<ButtonPress>',SearchProduct)                    ##WHEN BUTTON CLICKED GO TO SearchRsult.py


searchButton.pack()
searchButton.place(width=screenWidth/12,x=screenWidth-(screenWidth/1.4),y=screenHieght-(screenHieght/1.5))

##OUR REGISTERD SELLER PAGE
sellersLinkButton=tkinter.Label(
                            master=root,
                            text='لیست فروشگاه‌ها ',
                            width=20,
                            height=2,
                            fg='#4f4f4f',
                            cursor='hand2',
                            font=('IRANSans 10')
                            )
# closeButton.bind('<Button>',root.)
sellersLinkButton.pack()
sellersLinkButton.place(width=160,x=screenWidth-(screenWidth/1.51),y=screenHieght-(screenHieght/7))

##THE PAGE FOR REGISTER , NEW SELLER COULD REGISTER IN OUR SITE FROM THIS
sellerRegister=tkinter.Label(
                            master=root,
                            text='ثبت‌نام‌ فروشگاه‌ها',
                            width=20,
                            height=2,
                            fg='#4f4f4f',
                            cursor='hand2',
                            font=('IRANSans 10')
                            )
# closeButton.bind('<Button>',root.)
sellerRegister.pack()
sellerRegister.place(width=150,x=screenWidth-(screenWidth/1.3),y=screenHieght-(screenHieght/7))

##CONTACT US LINK BUTTON
contactUs=tkinter.Label(
                            master=root,
                            text='تماس با ما',
                            width=20,
                            height=2,
                            fg='#4f4f4f',
                            cursor='hand2',
                            font=('IRANSans 10')
                            )
# closeButton.bind('<Button>',root.)
contactUs.pack()
contactUs.place(width=100,x=screenWidth-(screenWidth/5),y=screenHieght-(screenHieght/7))

##ABOUT US
aboutUs=tkinter.Label(
                            master=root,
                            text='درباره ما',
                            width=20,
                            height=2,
                            fg='#4f4f4f',
                            cursor='hand2',
                            font=('IRANSans 10')
                            )
# closeButton.bind('<Button>',root.)
aboutUs.pack()
aboutUs.place(width=100,x=screenWidth-(screenWidth/3.5),y=screenHieght-(screenHieght/7))

##BOTTOM DIVIDER LINE
bottomDivider=tkinter.Label(
                            root,
                            text=200*"_",
                            fg='#000',
                            
)
bottomDivider.pack()
bottomDivider.place(x=screenWidth-(screenWidth/1.3),y=screenHieght-(screenHieght/10))

##CLOSE APP BUTTON
closeButton=tkinter.Button(
                            master=root,
                            text='بستن برنامه',
                            height=2,
                            bg='#ab001c',
                            fg='#fff',
                            cursor='hand2',
                            font=('IRANSans 12'),
                            command=root.destroy
                            )
# closeButton.bind('<Button>',)
closeButton.pack()
closeButton.place(width=160,x=screenWidth-(screenWidth/1.02),y=screenHieght-(screenHieght/8))

























root.mainloop()