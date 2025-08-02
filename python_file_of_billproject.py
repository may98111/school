#for addition of data
def data():
    import pickle
    o=open('bill.dat',"ab")
    s= int(input("Enter the number of bills to be made -> "))
    for j in range (s):
        li=[]
        print("<--------------DETAILS FOR BILL-------------->   ")
        d=input("  Enter the bill no -> ")
        e=input("  Enter the name of recipient -> ")
        f=input("  Enter the address -> ")
        g=input("  Enter the mobile no. -> ")
        p=[d,e,f,g]
        print("<--------------DETAILS FOR PRODUCT BOUGHT-------------->   ")
        n=int(input("  Enter the number of products bought -> ")) 
        a=0
        for i in range(n):
            a=a+1
            print("      <----DETAILS FOR",a,"ITEM BOUGHT---->")
            ab=input("   Name of Item bought -> ")
            ac=eval(input("   Quantity of Item bought(peice or kg or litre) -> "))
            ad=float(input("   Price of  per unit or per kilo or per litre of item -> "))                                            
            s=[ab,ac,ad]
            li.append(s)
        p.append(li)
        pickle.dump(p,o)
    o.close()




#FOR DISPLAY OF BILL
def dis():
        from datetime import datetime
        now = datetime.now()
        import pickle
        s=0
        a=[]
        o=open('bill.dat',"rb")
        q=0
        while q==0 :
            try:
                m = pickle.load(o)
                a.append(m)
            except:
                o.close()
                break
        print(a)
        for i in a:
            d=i[0]
            e=i[1]
            f=i[2]
            g=i[3]
            h=now.strftime("%d/%m/%Y(%H:%M:%S)")
            l=i[4]
            print("""
         __________________________________________________________________
        |                           >SUPER MART<                           |
        |                                                                  |  
        |                        >NEW DELHI-110005<                        |
        |                                                                  |
        |------------------------PHONE:01125268494-------------------------|                                     
        |                              >BILL<                              |                                            
        |==================================================================|
                ---->BILL NO :""",d,"""                          
                ---->NAME :""",e,"""                        
                ---->ADDRESS :""",f, """                      
                ---->MOBILE NO :""",g,"""                
                ---->DATE AND TIME :""",h,"""                    
        |__________________________________________________________________|""")
            print("          ","S.NO","   ","ITEMS","         ","QTY/KG/Li","      ","N/RATE","     ","VALUE")
            H=0
            for m in l:
                s=s+1
                t=m[0]
                u=m[1]
                v=m[2]
                H=H+(u*v)
                print("          ",s,"      ",t,"          ",u,"              ",v,"         ",u*v)
            n=s
            s=0
            print("        |___________________________________________________________________|")
            print("                  ITEMS: ",n,"                                 TOTAL: ₹",H)
            print("        |===================================================================|")
            print("               <---------------TOTAL AMOUNT TO BE PAID--------------->",)
            print("                                         ₹",H)
            print("         ___________________________________________________________________")
            print("         ________________THANKS FOR SHOPPING WITH SUPER MART________________")
            print("         -------------------------------------------------------------------")
            print("         *******************************************************************","\n")






#FOR SEARCH
def search():
    s=0
    from datetime import datetime
    now = datetime.now()
    import pickle
    a=[]
    o=open('bill.dat',"rb")
    q=0
    while q==0 :
        try:
            m = pickle.load(o)
            a.append(m)
        except:
            o.close()
            break     
    print("""
     ______________________________________
    |                                      |
    |     > SEARCH MANAGEMENT SYSTEM <     |
    |                                      |
    |--------------------------------------|
    |                                      |
    |        [1] Bill No.                  |
    |        [2] Name of recipient         |
    |        [3] Address                   |
    |        [4] Moile No.                 |
    |                                      |
     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

    ↓ Enter The choice for search of Bill""")
    c=int(input(""))
    if c==1:
        Bl=input("Enter the Bill No. -> ")
        sts=0
        for i in a:
            if i[0]==Bl:
                print("There is a Bill of Bill No.",Bl)
                e=input("Do you want to print that Bill(yes/no) -> ")
                sts=0
                if e=="yes":
                    d=i[0]
                    e=i[1]
                    f=i[2]
                    g=i[3]
                    h=now.strftime("%d/%m/%Y(%H:%M:%S)")
                    l=i[4]
                    print("""
                 __________________________________________________________________
                |                           >SUPER MART<                           |
                |                                                                  |  
                |                        >NEW DELHI-110005<                        |
                |                                                                  |
                |------------------------PHONE:01125268494-------------------------|                                     
                |                              >BILL<                              |                                            
                |==================================================================|
                        ---->BILL NO :""",d,"""                          
                        ---->NAME :""",e,"""                        
                        ---->ADDRESS :""",f, """                      
                        ---->MOBILE NO :""",g,"""                
                        ---->DATE AND TIME :""",h,"""                    
                |__________________________________________________________________|""")
                    print("          ","S.NO","   ","ITEMS","         ","QTY/KG/Li","      ","N/RATE","     ","VALUE")
                    H=0
                    for m in l:
                        s=s+1
                        t=m[0]
                        u=m[1]
                        v=m[2]
                        H=H+(u*v)
                        print("          ",s,"      ",t,"          ",u,"              ",v,"         ",u*v)
                    n=s    
                    s=0
                    print("        |___________________________________________________________________|")
                    print("                  ITEMS: ",n,"                                 TOTAL: ₹",H)
                    print("        |===================================================================|")
                    print("               <---------------TOTAL AMOUNT TO BE PAID--------------->",)
                    print("                                         ₹",H)
                    print("         ___________________________________________________________________")
                    print("         ________________THANKS FOR SHOPPING WITH SUPER MART________________")
                    print("         -------------------------------------------------------------------")
                    print("         *******************************************************************","\n")
                else:
                    pass
                break      
            else:
                sts=1
        if sts==1:
            print("There is No Bill of Bill No.",Bl)


            
    elif c==2:
        Bl=input("Enter the Name of Recipient -> ")
        sts=0
        for i in a:
            if i[1]==Bl:
                sts=0
                print("There is a Bill with Name",Bl)
                e=input("Do you want to print that Bill(yes/no) -> ")
                if e=="yes":
                    d=i[0]
                    e=i[1]
                    f=i[2]
                    g=i[3]
                    h=now.strftime("%d/%m/%Y(%H:%M:%S)")
                    l=i[4]
                    print("""
                __________________________________________________________________
                |                           >SUPER MART<                           |
                |                                                                  |  
                |                        >NEW DELHI-110005<                        |
                |                                                                  |
                |------------------------PHONE:01125268494-------------------------|                                     
                |                              >BILL<                              |                                            
                |==================================================================|
                        ---->BILL NO :""",d,"""                          
                        ---->NAME :""",e,"""                        
                        ---->ADDRESS :""",f, """                      
                        ---->MOBILE NO :""",g,"""                
                        ---->DATE AND TIME :""",h,"""                    
                |__________________________________________________________________|""")
                    print("          ","S.NO","   ","ITEMS","         ","QTY/KG/Li","      ","N/RATE","     ","VALUE")
                    H=0
                    for m in l:
                        s=s+1
                        t=m[0]
                        u=m[1]
                        v=m[2]
                        H=H+(u*v)
                        print("          ",s,"      ",t,"          ",u,"              ",v,"         ",u*v)
                    n=s    

                    print("        |___________________________________________________________________|")
                    print("                  ITEMS: ",n,"                                 TOTAL: ₹",H)
                    print("        |===================================================================|")
                    print("               <---------------TOTAL AMOUNT TO BE PAID--------------->",)
                    print("                                         ₹",H)
                    print("         ___________________________________________________________________")
                    print("         ________________THANKS FOR SHOPPING WITH SUPER MART________________")
                    print("         -------------------------------------------------------------------")
                    print("         *******************************************************************","\n")
                else:
                    pass    
                break
            else:
                sts=1
        if sts==1:
            print("There is No Bill of Bill No.",Bl)

    elif c==3:
        sts=0
        Bl=input("Enter the Address -> ")
        for i in a:
            if i[2]==Bl:
                sts=0
                print("There is a Bill with Address",Bl)
                e=input("Do you want to print that Bill(yes/no) -> ")
                if e=="yes":
                    d=i[0]
                    e=i[1]
                    f=i[2]
                    g=i[3]
                    h=now.strftime("%d/%m/%Y(%H:%M:%S)")
                    l=i[4]
                    print("""
                __________________________________________________________________
                |                           >SUPER MART<                           |
                |                                                                  |  
                |                        >NEW DELHI-110005<                        |
                |                                                                  |
                |------------------------PHONE:01125268494-------------------------|                                     
                |                              >BILL<                              |                                            
                |==================================================================|
                        ---->BILL NO :""",d,"""                          
                        ---->NAME :""",e,"""                        
                        ---->ADDRESS :""",f, """                      
                        ---->MOBILE NO :""",g,"""                
                        ---->DATE AND TIME :""",h,"""                    
                |__________________________________________________________________|""")
                    print("          ","S.NO","   ","ITEMS","         ","QTY/KG/Li","      ","N/RATE","     ","VALUE")
                    H=0
                    for m in l:
                        s=s+1
                        t=m[0]
                        u=m[1]
                        v=m[2]
                        H=H+(u*v)
                        print("          ",s,"      ",t,"          ",u,"              ",v,"         ",u*v)
                    n=s   
                    s=0
                    print("        |___________________________________________________________________|")
                    print("                  ITEMS: ",s,"                                 TOTAL: ₹",H)
                    print("        |===================================================================|")
                    print("               <---------------TOTAL AMOUNT TO BE PAID--------------->",)
                    print("                                         ₹",H)
                    print("         ___________________________________________________________________")
                    print("         ________________THANKS FOR SHOPPING WITH SUPER MART________________")
                    print("         -------------------------------------------------------------------")
                    print("         *******************************************************************","\n")
                else:
                    pass    
                break
            else:
                sts=1
        if sts==1:
            print("There is No Bill of Bill No.",Bl)

    elif c==4:
        sts=0
        Bl=input("Enter the Mobile no. -> ")
        for i in a:
            if i[3]==Bl:
                sts=0
                print("There is a Bill with Mobile no.",Bl)
                e=input("Do you want to Print that Bill(yes/no) -> ")
                if e=="yes":
                    d=i[0]
                    e=i[1]
                    f=i[2]
                    g=i[3]
                    h=now.strftime("%d/%m/%Y(%H:%M:%S)")
                    l=i[4]
                    print("""
                __________________________________________________________________
                |                           >SUPER MART<                           |
                |                                                                  |  
                |                        >NEW DELHI-110005<                        |
                |                                                                  |
                |------------------------PHONE:01125268494-------------------------|                                     
                |                              >BILL<                              |                                            
                |==================================================================|
                        ---->BILL NO :""",d,"""                          
                        ---->NAME :""",e,"""                        
                        ---->ADDRESS :""",f, """                      
                        ---->MOBLIE NO :""",g,"""                
                        ---->DATE AND TIME :""",h,"""                    
                |__________________________________________________________________|""")
                    print("          ","S.NO","   ","ITEMS","         ","QTY/KG/Li","      ","N/RATE","     ","VALUE")
                    H=0
                    for m in l:
                        s=s+1
                        t=m[0]
                        u=m[1]
                        v=m[2]
                        H=H+(u*v)
                        print("          ",s,"      ",t,"          ",u,"              ",v,"         ",u*v)
                    n=s   
                    s=0
                    print("        |___________________________________________________________________|")
                    print("                  ITEMS: ",n,"                                 TOTAL: ₹",H)
                    print("        |===================================================================|")
                    print("               <---------------TOTAL AMOUNT TO BE PAID--------------->",)
                    print("                                         ₹",H)
                    print("         ___________________________________________________________________")
                    print("         ________________THANKS FOR SHOPPING WITH SUPER MART________________")
                    print("         -------------------------------------------------------------------")
                    print("         *******************************************************************","\n")
                else:
                    pass    
                break
            else:
                sts=1
        if sts==1:
            print("There is No Bill of Bill No.",Bl)

    else:
        print("INVAILD CHOICE")
            
        
#UPDATE OF DATA
def update():
    import pickle
    a=[]
    o=open('bill.dat',"rb")
    q=0
    while q==0 :
        try:
            m = pickle.load(o)
            a.append(m)
        except:
            o.close()
            break  
    
    
    o=open('bill.dat',"wb")   
    print("""
 ______________________________________
|                                      |
|     > UPDATE MANAGEMENT SYSTEM <     |
|          (Details on Bill)           |
|--------------------------------------|
|                                      |
|        [1] Name of recipient         |
|        [2] Address of recipent       |
|        [3] Mobile No. of recipent    |
|                                      |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾     
↓ Enter The choice for updation in Bill""")
    c=int(input(""))
    d=input("Enter the Bill No. -> ")
    for i in a:
        if i[0]==d:
            D=i
            if c==1 :
                s=input("Enter the New Name of Recipient -> ")
                D[1]=s
                print("Name of Recipient Updated")
                pickle.dump(D,o)
            elif c==2:
                s=input("Enter the New Address of Recipient -> ")
                D[2]=s
                print("Address of Recipient Updated")
                pickle.dump(D,o)
            elif c==3:
                s=input("Enter the New Mobile No. of Recipient -> ")
                D[3]=s
                print("Mobile No. of Recipient Updated")    
                pickle.dump(D,o)
            else:
                print("INVALID OPTION")
        else:
            pickle.dump(i,o)
            pass                   
    o.close()     
            
        


def dle():
    import pickle
    a=[]
    o=open('bill.dat',"rb")
    q=0
    while q==0 :
        try:
            d = pickle.load(o)
            a.append(d)
        except:
            o.close()
            break
    
    print(a)

    o=open('bill.dat',"wb")
    print("""
 ______________________________________
|                                      |
|    > DELETION MANAGEMENT SYSTEM <    |
|                                      |
|--------------------------------------|
|                                      |
|        [1] Whole Bill                |
|        [2] Items in Bill             |
|                                      |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾     
↓ Enter The choice for updation in Bill""")
    c=int(input(""))
    if c==1:
        d=input("Enter the Bill No. -> ")
        for i in a:
            if i[0]==d:
                a.remove(i)
                print("BILL Has Been Deleted")
            else:
                print("INVALID BILL NO.")
        for i in a:
            pickle.dump(i,o)
    elif c==2:
        d=input("Enter the Bill No. -> ")
        for i in a:
            if i[0]==d:
                D=i[4]
                m=input("Enter the Item Name -> ")
                for k in D:
                    if k[0]==m:
                        D.remove(k)
                        i[4]=D
                        pickle.dump(i,o)
                    else:
                        pass
            else:
                pickle.dump(i,o)
                
    else:
        print("INVALID OPTION")
    o.close()


        
n="o"
while n!=0:
    print("""
 ______________________________________
|                                      |
|       >BILL MANAGEMENT SYSTEM <      |
|                                      |
|--------------------------------------|
|                                      |
|        [1] Insert Data in Bill       |
|        [2] Display of Bill           |
|        [3] Search of Bill            |
|        [4] Update of Bill            |
|        [5] Deletion of Bill          |
|        [0] Exit                      |
|                                      |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

↓ Enter your choice""")
    c=int(input(""))
    if c==0:
        n=0
    elif c==1:
        data()
    elif c==2:
        dis()
    elif c==3:
        search()
    elif c==4:
        update()
    elif c==5:
        dle()
    else:
        print("try again")

   
        
    