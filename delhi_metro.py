from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle
class Graph(object):
    def __init__(self):
        fmap=open("map","rb")
        self.a=pickle.load(fmap)
        self.b=pickle.load(fmap)
        self.graph=self.a
        self.station=[]
        self.distance=0
    def BFS(self,s,fmap):
        visited=[False]*(len(self.graph))
        queue=[]
        dist=[None]*(len(self.graph))
        predecessor=[None]*(len(self.graph))
        queue.append(s)
        visited[s]=True
        dist[s]=0
        s1=s
        while queue:
            s=queue.pop(0)
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
                    dist[i]=dist[s]+1
                    predecessor[i]=s
                    if (i==fmap):
                        p=predecessor[i]
                        self.distance=dist[i]
                        self.station.append(self.b[fmap])
                        while (p!=s1):
                            self.station.append(self.b[p])
                            p=predecessor[p]
                        else:
                            self.station.append(self.b[s1])

                        break

#HEADING AND CREATING BUTTONS TO ROUTE
main_window=Tk()
main_window.title("DELHI METRO RAIL CORPORATION")
main_window.state("zoomed")
main_window.configure(background="white")

topside = LabelFrame(main_window , bd = 2,bg="white")
topside.pack(side=TOP,fill=X,pady=10,padx=5)

img = PhotoImage(file=r"dmlogo.png")
p_lable=Label(topside,image=img,bg="white")
p_lable.pack(side=LEFT)

img2 = PhotoImage(file=r"dmlogo.png")
p_lable2=Label(topside,image=img2,bg="white")
p_lable2.pack(side=RIGHT)

text_label=Label(topside,text="DELHI METRO RAIL CORPORATION",font=("Times",30,"bold"),fg="Black",bg="white")
text_label.pack(side=TOP,padx=30,pady=20)

LS=LabelFrame(main_window,bd = 0,bg="white")
LS.place(x=100,y=200,height=200,width=300)

start_time=Label(LS,text="SOURCE",font=("Times",18,"bold"),fg="black",bg="white")
start_time.pack(side = TOP,padx=10,pady=30)
dest_time=Label(LS,text="DESTINATION",font=("Times",18,"bold"),fg="black",bg="white")
dest_time.pack(side = TOP,padx=10,pady=27)

centerside = LabelFrame(main_window , bd = 0,bg="white")
centerside.place(x = 380 , y = 200, height=200, width = 300)
value1 = StringVar()
combo1 = ttk.Combobox(centerside,width=25,font=("Times",16,"bold"),height=10,textvariable=value1,state='readonly',justify = 'center')
combo1['values']=['Select Station','AIIMS Yellow Line', 'ANVT Pink Line', 'Adarsh Nagar Yellow Line', 'Arjan Garh Yellow Line', 'Arthala Red Line', 'Ashram Pink Line', 'Azadpur', 'Badarpur Violet Line', 'Badkal Mor Violet Line', 'Bata Chownk Violet Line', 'Bhikaji Cama Place Pink Line', 'Central Secretariat', 'Chandhni Chowk Yellow Line', 'Chawri Bazar Yellow Line', 'Chhattarpur Yellow Line', 'Civil Lines Yellow Line', 'Delhi Cantt Pink Line', 'Delhi Gate Violet Line', 'Dilshad Garden Red Line', 'Durgabai Deshmukh South Campus Pink Line', 'ESI Hospital Pink Line', 'East Azad Nagar Pink Line', 'Escorts Mujesar Violet Line', 'Faridabad Old Violet Line', 'GTB Nagar Yellow Line', 'Ghotorni Yellow Line', 'Gokulpuri Pink Line', 'Govindpuri Violet Line', 'Green Park Yellow Line', 'Gurudronacharya Yellow Line', 'Haiderpur Badli Mor Yellow Line', 'Hauz Khas Yellow Line', 'Hazrat Nizamuddin Pink Line', 'Hindon Red Line', 'Huda City Centre Yellow Line', 'IFFCO Chowk Yellow Line', 'INA', 'IP Extension Pink Line', 'ITO Violet Line', 'Inder Lok Red Line', 'JLN Violet Line', 'Jaffrabad Pink Line', 'Jahangirpuri Yellow Line', 'Jama Masjid Violet Line', 'Jangpura Violet Line', 'Janpath Violet Line', 'Jasola-Apollo Violet Line', 'Jhil Mil Red Line', 'Johri Enclave Pink Line', 'Jorbagh Yellow Line', 'Kailash Colony Violet Line', 'Kalkaji Mandir Violet Line', 'Kanhaiya Nagar Red Line', 'Karkarduma Court Pink Line', 'Karkarduma Pink Line', 'Kashmere Gate', 'Keshav Puram Red Line', 'Khan Market Violet Line', 'Kohat Enclave Red Line', 'Krishna Nagar Pink Line', 'Lajpat Nagar', 'Lal Quila Violet Line', 'Lok Kalyan Marg Yellow Line', 'MG Road Yellow Line', 'Majlis Park Pink Line', 'Major Mohit Sharma Red Line', 'Malvia Nagar Yellow Line', 'Mandawali - West Vinod Nagar Pink Line', 'Mandi House Violet Line', 'Mansarovar Park Red Line', 'Maujpur Pink Line', 'Maya Puri Pink Line', 'Mayur Vihar 1 Pink Line', 'Mayur Vihar Pocket 1 Pink Line', 'Mewla Maharajpur Violet Line', 'Model Town Yellow Line', 'Mohan Estate Violet Line', 'Mohan Nagar Red Line', 'Moolchand Violet Line', 'NHPC Chownk Violet Line', 'Naraina Vihar Pink Line', 'Neelam Chownk Ajronda Violet Line', 'Nehru Place Violet Line', 'Netaji Subhash Place', 'New Delhi Yellow Line', 'Okhla Violet Line', 'Patel Chowk Yellow Line', 'Pitam Pura Red Line', 'Pratap Nagar Red Line', 'Pul Bangash Red Line', 'Punjabi Bagh West Pink Line', 'Qutab Minar Yellow Line', 'Raj Bagh Red Line', 'Raja Nahar singh marg Violet Line', 'Rajiv Chowk Yellow Line', 'Rajouri Garden Pink Line', 'Rithala Red Line', 'Rohini East Red Line', 'Rohini Sector 18, 19 Yellow Line', 'Rohini West Red Line', 'Saket Yellow Line', 'Samaypur Badli Yellow Line', 'Sant Surdas Violet Line', 'Sarai Violet Line', 'Sarita Vihar Violet Line', 'Sarojini Nagar Pink Line', 'Sector 28 Violet Line', 'Seelampur Red Line', 'Shahdara Red Line', 'Shaheed Nagar Red Line', 'Shaheed Sthal(New Bus Adda) Red Line', 'Shakurpur Pink Line', 'Shalimar Bagh Pink Line', 'Shastri Nagar Red Line', 'Shastri Park Red Line', 'Shiv Vihar Pink Line', 'Shyam park Red Line', 'Sikandarpur. Yellow Line', 'Sir Vishweshwaraiah Moti Bagh Pink Line', 'South Extension Pink Line', 'Sultanpur Yellow Line', 'Tis Hazari Red Line', 'Trilokpuri Sanjay Lake Pink Line', 'Tuglakabad Violet Line', 'Udyog Bhawan Yellow Line', 'Vidhan Sabha Yellow Line', 'Vinobapuri Pink Line', 'Vinod Nagar East Pink Line', 'Viswavidyalaya Yellow Line', 'Welcome']
combo1.current(0)
combo1.pack(side=TOP,pady=30)

value2 = StringVar()
combo2 = ttk.Combobox(centerside,width=25,font=("Times",16,"bold"),height=10,textvariable=value2,state='readonly',justify = 'center')

combo2['values']=['Select Station','AIIMS Yellow Line', 'ANVT Pink Line', 'Adarsh Nagar Yellow Line', 'Arjan Garh Yellow Line', 'Arthala Red Line', 'Ashram Pink Line', 'Azadpur', 'Badarpur Violet Line', 'Badkal Mor Violet Line', 'Bata Chownk Violet Line', 'Bhikaji Cama Place Pink Line', 'Central Secretariat', 'Chandhni Chowk Yellow Line', 'Chawri Bazar Yellow Line', 'Chhattarpur Yellow Line', 'Civil Lines Yellow Line', 'Delhi Cantt Pink Line', 'Delhi Gate Violet Line', 'Dilshad Garden Red Line', 'Durgabai Deshmukh South Campus Pink Line', 'ESI Hospital Pink Line', 'East Azad Nagar Pink Line', 'Escorts Mujesar Violet Line', 'Faridabad Old Violet Line', 'GTB Nagar Yellow Line', 'Ghotorni Yellow Line', 'Gokulpuri Pink Line', 'Govindpuri Violet Line', 'Green Park Yellow Line', 'Gurudronacharya Yellow Line', 'Haiderpur Badli Mor Yellow Line', 'Hauz Khas Yellow Line', 'Hazrat Nizamuddin Pink Line', 'Hindon Red Line', 'Huda City Centre Yellow Line', 'IFFCO Chowk Yellow Line', 'INA', 'IP Extension Pink Line', 'ITO Violet Line', 'Inder Lok Red Line', 'JLN Violet Line', 'Jaffrabad Pink Line', 'Jahangirpuri Yellow Line', 'Jama Masjid Violet Line', 'Jangpura Violet Line', 'Janpath Violet Line', 'Jasola-Apollo Violet Line', 'Jhil Mil Red Line', 'Johri Enclave Pink Line', 'Jorbagh Yellow Line', 'Kailash Colony Violet Line', 'Kalkaji Mandir Violet Line', 'Kanhaiya Nagar Red Line', 'Karkarduma Court Pink Line', 'Karkarduma Pink Line', 'Kashmere Gate', 'Keshav Puram Red Line', 'Khan Market Violet Line', 'Kohat Enclave Red Line', 'Krishna Nagar Pink Line', 'Lajpat Nagar', 'Lal Quila Violet Line', 'Lok Kalyan Marg Yellow Line', 'MG Road Yellow Line', 'Majlis Park Pink Line', 'Major Mohit Sharma Red Line', 'Malvia Nagar Yellow Line', 'Mandawali - West Vinod Nagar Pink Line', 'Mandi House Violet Line', 'Mansarovar Park Red Line', 'Maujpur Pink Line', 'Maya Puri Pink Line', 'Mayur Vihar 1 Pink Line', 'Mayur Vihar Pocket 1 Pink Line', 'Mewla Maharajpur Violet Line', 'Model Town Yellow Line', 'Mohan Estate Violet Line', 'Mohan Nagar Red Line', 'Moolchand Violet Line', 'NHPC Chownk Violet Line', 'Naraina Vihar Pink Line', 'Neelam Chownk Ajronda Violet Line', 'Nehru Place Violet Line', 'Netaji Subhash Place', 'New Delhi Yellow Line', 'Okhla Violet Line', 'Patel Chowk Yellow Line', 'Pitam Pura Red Line', 'Pratap Nagar Red Line', 'Pul Bangash Red Line', 'Punjabi Bagh West Pink Line', 'Qutab Minar Yellow Line', 'Raj Bagh Red Line', 'Raja Nahar singh marg Violet Line', 'Rajiv Chowk Yellow Line', 'Rajouri Garden Pink Line', 'Rithala Red Line', 'Rohini East Red Line', 'Rohini Sector 18, 19 Yellow Line', 'Rohini West Red Line', 'Saket Yellow Line', 'Samaypur Badli Yellow Line', 'Sant Surdas Violet Line', 'Sarai Violet Line', 'Sarita Vihar Violet Line', 'Sarojini Nagar Pink Line', 'Sector 28 Violet Line', 'Seelampur Red Line', 'Shahdara Red Line', 'Shaheed Nagar Red Line', 'Shaheed Sthal(New Bus Adda) Red Line', 'Shakurpur Pink Line', 'Shalimar Bagh Pink Line', 'Shastri Nagar Red Line', 'Shastri Park Red Line', 'Shiv Vihar Pink Line', 'Shyam park Red Line', 'Sikandarpur. Yellow Line', 'Sir Vishweshwaraiah Moti Bagh Pink Line', 'South Extension Pink Line', 'Sultanpur Yellow Line', 'Tis Hazari Red Line', 'Trilokpuri Sanjay Lake Pink Line', 'Tuglakabad Violet Line', 'Udyog Bhawan Yellow Line', 'Vidhan Sabha Yellow Line', 'Vinobapuri Pink Line', 'Vinod Nagar East Pink Line', 'Viswavidyalaya Yellow Line', 'Welcome']
combo2.current(0)
combo2.pack(side=TOP,pady=30)


def print_route(arr_sta,dis):
    RS=LabelFrame(main_window ,bg="white",bd=0)
    RS.place(x=900,y=150,height=600,width=400)
    scrollb=Scrollbar(RS)
    scrollb.pack(side=RIGHT,fill=Y)
    scrollb2=Scrollbar(RS,orient="horizontal")
    scrollb2.pack(fill=X,side=BOTTOM)
    listbox=Listbox(RS,bd=2,bg="White",fg="Black",font=("Times New Roman",14,"bold"),yscrollcommand = scrollb.set,xscrollcommand = scrollb2.set)
    scrollb.config(command=listbox.yview)
    scrollb2.config(command=listbox.xview)
    listbox.insert(END, "            STATIONS TO CROSS : "+str(dis))
    listbox.selection_clear(0, 'end')
    for i in range(len(arr_sta)-1,-1,-1):
        listbox.insert(END, "   ")
        listbox.insert(END, "   "+str(len(arr_sta)-i)+"."+" "+arr_sta[i])
        #listbox.insert(END," "+str(len(arr_sta)+"."+
    listbox.pack(fill=BOTH,expand=TRUE)


#FINDING SHORTEST ROUTE BW TWO STATIONS
def find_route(s,d):
    g=Graph()
    dict_station=g.b
    try:
        for i in range(len(dict_station)):
            if dict_station[i]==s:
                s_index=i
            elif dict_station[i]==d:
                d_index=i
            else:
                continue
        g.BFS(s_index,d_index)
        print_route(g.station,g.distance)
    except:
        messagebox.showinfo("Select Station", "Enter Valid Station" , icon = "warning")

def click_me():
    try:
        ##########################################################3
        RS = LabelFrame(main_window ,bg="Black",bd=0)
        RS.place(x = 900 , y = 150, height=600, width = 400)
        RS.destroy()
    except:
        a=5
    source=value1.get()
    destination=value2.get()
    find_route(source,destination)


click_button = Button(main_window, text="Find Shortest Route", width=20, font=("Times", 14, "bold"), command=click_me, relief="groove", cursor="hand2")
click_button.place(x=323,y=425)

main_window.mainloop()
