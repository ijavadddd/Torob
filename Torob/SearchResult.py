# This Python file uses the following encoding: utf-8
from tkinter import *
from TkinterModule import PageScrollbar,GetMonitorScreenSize,ProductBox,FixedNavbar,Footer
from mysql.connector import connect

####    @ijavadddd

def searchResults():
    searchResultRoot=Tk()
    Navbar=FixedNavbar(searchResultRoot)
    Navbar.CreateNavbar()
    screenWidth,screenHieght=GetMonitorScreenSize()
    bodyContainer=Frame(searchResultRoot)
    bodyContainer.pack(fill=BOTH, expand=1)
    bodyContainer.place(width=screenWidth,height=screenHieght-(screenHieght/5),x=0,y=screenHieght-(screenHieght/1.24))
    mainScrollable=PageScrollbar(bodyContainer)
    mainScrollable.config(width=screenWidth,height=screenHieght*5)
    with connect(host='localhost',user='root',password='58858810',database='db_torob') as Torob:
        myCursor=Torob.cursor()
        myCursor.execute('select * from t_temporaryResultSearch')                           
        products=myCursor.fetchall()
        products=[list(productTuple) for productTuple in products]
        # resultProducts= products
        productsBoxes=ProductBox(products)
        newHeight=productsBoxes.CreateProductBoxFrame(searchResultRoot,mainScrollable)
        mainScrollable.config(width=screenWidth,height=newHeight)
        pageFooter=Footer(mainScrollable)
        pageFooter.SetFooter(newHeight)


ReturnResult=searchResults()