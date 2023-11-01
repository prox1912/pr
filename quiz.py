from  random import *

import csv
def level1():
    cct=0
    ct=""
    t=[]
    s=[]

    q1={"Taj Mahal":"India","Christ The Redeemer":"Rio de Janeiro","Machu Pichu":"Peru","Colosseum":"Rome"}
    t=list(q1.keys())
    s=list(q1.values())
    a=choice(t)
    ct=q1[a]
    s.remove(ct)
    print("Where is ",a,"?","\n 1-",ct)
    for i in s:
        x=2
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==1:
        cct+=1
        print("Correct")
    else:
        print("Wrong")

    q2={"Mahatma Gandhi":"Porbandar","Gautam Buddha":"Lumbini","Hellen Keller":"Tuscumbia","Adolf Hitler":"Austria"}
    
    t=list(q2.keys())
    s=list(q2.values())
    a=choice(t)
    ct=q2[a]
    s.remove(ct)
    print("Where was",a," born?","\n 1-",ct)
    for i in s:
        x=2
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==1:
        cct+=1
        print("Correct")
    else:
        print("Wrong")

    
    q3={' First Battle of Panipat':'1526','Battle of Waterloo':'1815','Battle of Plassey':'1757','Syrian Civil War':'2011'}
    t=list(q3.keys())
    s=list(q3.values())
    a=choice(t)
    ct=q3[a]
    s.remove(ct)
    print("When was",a," fought?")
    s.insert(2,ct)
    x=1

    for i in s:
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==3:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q4={'Water':"H2O","Methane":"CH4","Ammonia":"NH3","Glucose":"C6H12O6"}
    t=list(q4.keys())
    s=list(q4.values())
    a=choice(t)
    ct=q4[a]
    s.remove(ct)
    print("What is the formula of ",a,"?")
    s.insert(1,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==2:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    q5={"square of 25":"625","simple interest when principal amount is Rs 450 ,rate is 2% and time is 1 year":"9","geatest integer of 8.5 [8.5]":"8","sum of first 100 natural answers":"5050"}
    
    t=list(q5.keys())
    s=list(q5.values())
    a=choice(t)
    ct=q5[a]
    s.remove(ct)
    print("What is the",a,"?")
    s.insert(0,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==1:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q6={"human":"mammal","frog":"amphibian","squirrel":"rodent","snake":"reptile"}
    
    t=list(q6.keys())
    s=list(q6.values())
    a=choice(t)
    ct=q6[a]
    s.remove(ct)
    print("What is the species of ",a,"?")
    s.insert(3,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==4:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    

    q7={"SI unit of current":"ampere","name of scientist who worked on basic principle for generating electrical current":"faraday","unit for power of lens":"Dioptre","name of scientist who gave three laws of motion":"newton"}
    
    t=list(q7.keys())
    s=list(q7.values())
    a=choice(t)
    ct=q7[a]
    s.remove(ct)
    print("What is the  ",a,"?")
    s.insert(2,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==3:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q8={"Literature":"Pulitzer award","Music":"Grammy Award","Acting":"Oscar Award","Sports":"Laureus Award"}
    
    t=list(q8.keys())
    s=list(q8.values())
    a=choice(t)
    ct=q8[a]
    s.remove(ct)
    print("Which of the following awards are given in the field of ",a,"?")
    s.insert(0,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==1:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q9={"most abundant gas in earth's atmosphere":"Nitrogen","gas responsible for global warming":"carbon dioxide","the gas used for hydrogenation of vanaspati ghee":"Hydrogen","gas filled in air balloons":"Helium"}
    
    t=list(q9.keys())
    s=list(q9.values())
    a=choice(t)
    ct=q9[a]
    s.remove(ct)
    print("What is the name of ",a,"?")
    s.insert(1,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==2:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q10={"Iron Man of India":"Sardar Vallabhai Patel","Father of Indian Constitution":"B.R.Ambedkar","writer of national anthem":"Rabindranath Tagore","Father of  the Nation  ":"Mahtma Gandhi"}  
    
    t=list(q10.keys())
    s=list(q10.values())
    a=choice(t)
    ct=q10[a]
    s.remove(ct)
    print("Who is the ",a,"?")
    s.insert(2,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==3:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    return cct
def level2():
    cct=0
    ct=""
    t=[]
    s=[]

    q1={"is used in softening hard water":"sodium carbonate","is used in fire extinguisher":"sodium hydrogen carbonate","is the major constituent of biogas":"methane","element has the lowest freezing point":"Helium"}
    
    t=list(q1.keys())
    s=list(q1.values())
    a=choice(t)
    ct=q1[a]
    s.remove(ct)
    print("What is  ",a,"?")
    s.insert(1,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==2:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q2={"won the Wimbledon Open Men's Singles Crown 2021":"Novak Djokovic","is the new Junior Boys Wimbledon Champion 2021":"Samir Banerjee","first Indian male squash player to enter top 10 in PSA world rankings":"Sourav Ghosai","won BBC's Sports Personality of the Year Prize 2020":"Lewis Hamilton"}
    
    t=list(q2.keys())
    s=list(q2.values())
    a=choice(t)
    ct=q2[a]
    s.remove(ct)
    print("Who ",a,"?")
    s.insert(3,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==4:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q3={"A man weighing 65 kg jumps from a 100 ft high building with a load of 35 kg.What will be the load experienced by him":"0","What is the wavelength of red light in nm":"700","The frequency (in hz)note\n that is  one octave higher than 500Hz is":"1000","100 W electric bulb is used for 10 hours a day.How many units of energy are consumed in 30 days":"30"}
    
    t=list(q3.keys())
    s=list(q3.values())
    a=choice(t)
    ct=q3[a]
    s.remove(ct)
    print(a,"?")
    s.insert(2,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==3:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q4={"father of computing":"Charles Babbage","founder of Facebook":"Mark Zuckerburg","inventor of mouse":"Douglas Engelbart","founder of Google":"Larry Page and Sergey Brin"}
    
    t=list(q4.keys())
    s=list(q4.values())
    a=choice(t)
    ct=q4[a]
    s.remove(ct)
    print("Who is the",a,"?")
    s.insert(3,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==4:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q5={"did  Netaji Subhash Chandra Bose start his Azad Hind Radio":"Berlin","Lothal is located ":"India","the Moplah event in 1921 took place":"Kerala"," didthe Japenese drop the bomb on 7 December 1941 which led to The bombing of Hiroshima Nagasaki by the USA":"Pearl Harbour"}
    
    t=list(q5.keys())
    s=list(q5.values())
    a=choice(t)
    ct=q5[a]
    s.remove(ct)
    print("Where",a,"?")
    s.insert(0,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==1:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q6={"Haflong lake":"Assam","Pangong lake":"Ladakh","Betwa River":"Satpura Hills","Tapi":"Gulf of Khambhat"}
    
    t=list(q6.keys())
    s=list(q6.values())
    a=choice(t)
    ct=q6[a]
    s.remove(ct)
    print("Where is",a,"?")
    s.insert(2,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==3:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q7={"Spill the beans":"Give away a secret","Blow one's own trumpet":"Praise oneself","White object":"An uneconomical possession","In the pipeline":"In the process of being developed"}
    
    t=list(q7.keys())
    s=list(q7.values())
    a=choice(t)
    ct=q7[a]
    s.remove(ct)
    print("What is the meaning of ",a,"?")
    s.insert(1,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==2:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q8={"Presidents Rule":"Article 356","Hindi as official language":"Article 343","Special status to Kashmir":"Article 370","Specify the fundamental rights available":"Article 12-35"}
    
    t=list(q8.keys())
    s=list(q8.values())
    a=choice(t)
    ct=q8[a]
    s.remove(ct)
    print("In which part of the Indian Constitution is ",a," written?")
    s.insert(3,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==4:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q9={"award winning films  that had no dialogues":"Pushpak","first Indian movie nominated for oscar":"Mother India"," book RK Narayan is the author of":"Malgudi Days","first film to win the Filmfare Best Film award":"Do Bigha Zamin"}
    
    t=list(q9.keys())
    s=list(q9.values())
    a=choice(t)
    ct=q9[a]
    s.remove(ct)
    print("Which is the ",a,"?")
    s.insert(1,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==2:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    q10={"Smallpox":"Variola virus","Kwashiorkor":"protein deficiency","osteoporosis":"calcium deficiency","beri beri":"vitamin B1 deficiency"}
   
    t=list(q10.keys())
    s=list(q10.values())
    a=choice(t)
    ct=q10[a]
    s.remove(ct)
    print("What is the cause of",a,"?")
    s.insert(2,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==3:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    return cct
def level3():
    cct=0
    ct=""
    t=[]
    s=[]

    q1={"man to climb Mount Everest without supplemental oxygen":"Reinhold Messner"," Governor General of the UN":"Trygve Lie"," person to sail around the world":"Magellan","man to fly into the space":"Yuri Gagarin"}
    
    
    t=list(q1.keys())
    s=list(q1.values())
    a=choice(t)
    ct=q1[a]
    s.remove(ct)
    print("Who is the first ",a,"?")
    s.insert(1,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==2:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    
    q2={"stars are there on the flag of USA":"50","digits are in pi(in trillion) are calculated":"62.8","bones are there in an elephants trunk":"0","breeds of elephant are there":"3"}
    
    
    t=list(q2.keys())
    s=list(q2.values())
    a=choice(t)
    ct=q2[a]
    s.remove(ct)
    print("How many",a,"?")
    s.insert(3,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==4:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    
    q3={" was once known as Duroliponte":"Cambridge","is the having the oldest tree in the world":"California","was known as St Petersburg city":"Leningrad","is the new name of Oslo city":"Kristania"}
    
    
    t=list(q3.keys())
    s=list(q3.values())
    a=choice(t)
    ct=q3[a]
    s.remove(ct)
    print("Which city",a,"?")
    s.insert(0,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==1:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    
    q4={"in herbivorous animals is the digestion of starch done through bacteria":"caecum","is the bile collected":"gall bladder","is the largest organ":"skin","are calcium crystals a normal part":"ears"}
    
    
    t=list(q4.keys())
    s=list(q4.values())
    a=choice(t)
    ct=q4[a]
    s.remove(ct)
    print(" In which organ  ",a,"?")
    s.insert(0,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==1:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    
    q5={"If the spinning speed of earth is increased then the weight of body at equator":"decreases","The weight of a man in an elevator movin up ":"increases","when light travels from one medium to other the frequency of light":"remains same","In a prism the angle of deviation between incident and emergent ray ______ with angle of incidence":"decrease then increases"}
    
    
    t=list(q5.keys())
    s=list(q5.values())
    a=choice(t)
    ct=q5[a]
    s.remove(ct)
    print(a,"?")
    s.insert(2,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==3:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    
    q6={"high density polythene":'Ziegler Natta catalyst','Haber\'s process':'finely divided iron','Contact process':'vanadium pentoxide','Hydrogenation of vegetable oils':"hydroden over palladium"}    
    
    t=list(q6.keys())
    s=list(q6.values())
    a=choice(t)
    ct=q6[a]
    s.remove(ct)
    print("Which catalyst is used in",a,"?")
    s.insert(1,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==2:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    
    q7={"The difference between compound interest and simple interest at the same rate on Rs 5000 for 2 years is Rs 72.The rate of interest per annum is":"12","A boat can travel 15 km/hr instill water.If the speed of the stream is 3km/hr then what will be the time taken by boat to travel 72km in downstream direction":"4","in how many ways can the letters of the word LEADER be arranged":"360","How many 5 digit answers can be formed from the digits 2,3,5,6,7 and 9 which are divisible by 5 and none of the digits is repeated":"20"}
    
     
    t=list(q7.keys())
    s=list(q7.values())
    a=choice(t)
    ct=q7[a]
    s.remove(ct)
    print("Calculate: ",a,"?")
    s.insert(0,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==1:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    
    q8={"recently amends National anthem to honour indigineous people":"Australia","first one to approve COVID 19 vaccine of Oxford-AstraZeneca":"England","is the host country of the African Union Summit 2022":"Zimbabwe","has announced to provide 144 million $ assistance to people of Afghanistan":"USA"}
    
    
    t=list(q8.keys())
    s=list(q8.values())
    a=choice(t)
    ct=q8[a]
    s.remove(ct)
    print("Which country ",a,"?")
    s.insert(3,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==4:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    
    q9={"\'The greatest glory in living lies not in never falling but in rising every time we fall\' ":"Nelson Mandela","\'Tell me and I forget.Teach me and I remember.Involve me and I learn.\' ":"Benjamin Franklin","\' Whoever is happy makes others happy too.\' ":"Anne Frank","\'You will face many defeats in life but never let yourself be defeated\'":"Maya Angelou"}
    
    
    t=list(q9.keys())
    s=list(q9.values())
    a=choice(t)
    ct=q9[a]
    s.remove(ct)
    print("Who said ",a,"?")
    s.insert(0,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==1:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    
    
    q10={"I speak without a mouth and hear without ears. I have no body but I come alive with the wind":"echo","I have cities but no houses. I have mountains but no trees. I have water but no fish.":"map","I come from a mine and get surrounded by wood always.Everyone uses me.":"pencil lead","I disappear as soon as you say my name":"silence"}
    
    
    t=list(q10.keys())
    s=list(q10.values())
    a=choice(t)
    ct=q10[a]
    s.remove(ct)
    print(a," Who am I?")
    s.insert(2,ct)
    x=1
    for i in s:
        
        print(x,"-",i)
        x=x+1
    ans=int(input("Enter answer"))
    if ans==3:
        cct+=1
        print("Correct")
    else:
        print("Wrong")
    return cct


def main():
    print("Welcome!! My name is Alina. I will be taking your quiz today.\n There are three levels:easy,medium and difficult. You can select whichever level you want to play. \nThere are 10 questions in each level. No two people get the same set of questions.\n At the end of each level your scores are calculated and displayed along with the leaderboard.")
    print("If you give the quiz multiple times i will keep track of all your previous scores")
    while True:
        name=input("Enter your name")
        n=int(input("1-Easy Level , 2-Medium Level , 3-Difficult level.Enter level which you want to play"))
        if n==1:
            c1=level1()
            print(name,", your total score is: ",c1)
            l=[name,c1]
            file='level1.csv'
            with open(file,'a',newline='') as f:
                csv_w=csv.writer(f,delimiter=',')
                csv_w.writerow(l)
            print("Leaderboard of level 1")
            k=[]
            with open(file,"r") as f:
                c=list(csv.reader(f))
                
                w=1
                for i in c:
                    
                    print(w," ",i)
                    w+=1
        elif n==2:
            c2=level2()
            print(name,", your total score is: ",c2)
            
            l=[name,c2]
            file='level2.csv'
            with open(file,'a',newline='') as f:
                csv_w=csv.writer(f,delimiter=',')
                csv_w.writerow(l)
            print("Leaderboard of level 2")
            k=[]
            with open(file,"r") as f:
                c=list(csv.reader(f))
                

                w=1        
                for i in  c:
                    
                    print(w," ",i)
                    w=w+1
                    
            
                
        
        elif n==3:
            c3=level3()
            print(name,", your total score is: ",c3)
            
            l=[name,c3]
            file='level3.csv'
            with open(file,'a',newline='') as f:
                csv_w=csv.writer(f,delimiter=',')
                csv_w.writerow(l)
            print("Leaderboard of level 3")
            k=[]
            with open(file,"r") as f:
                c=list(csv.reader(f))
                
                w=1
                for i in  c:
                    
                    print(w," ",i)
                    w=w+1
                
        
        x=input("Do you want to continue?")
        x.lower()
        if x=="no":
           break 
main()
