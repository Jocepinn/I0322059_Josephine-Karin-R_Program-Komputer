#mencari IP mahasiswa

Data =  {
    "Ali" : {
        "fisika" : 80,
        "biologi": 80,
        "matematika" : 85,
    },
    "Budi" : {
        "fisika" : 70,
        "biologi": 60,
        "matematika" : 70,
    },
    "Caca" : {
        "fisika" : 75,
        "biologi": 80,
        "matematika" : 75,
    },
    "Dodo" : {
        "fisika" : 85,
        "biologi": 70,
        "matematika" : 80,
    },
    "Elo" : {
        "fisika" : 90,
        "biologi": 60,
        "matematika" : 80
    }
}

#mencari IP
ip_1 = (Data["Ali"]["fisika"])+(Data["Ali"]["biologi"])+(Data["Ali"]["matematika"]) 
ip_2 = (Data["Budi"]["fisika"])+(Data["Budi"]["biologi"])+(Data["Budi"]["matematika"])
ip_3 = (Data["Caca"]["fisika"])+(Data["Caca"]["biologi"])+(Data["Caca"]["matematika"])
ip_4 = (Data["Dodo"]["fisika"])+(Data["Dodo"]["biologi"])+(Data["Dodo"]["matematika"])
ip_5 = (Data["Elo"]["fisika"])+(Data["Elo"]["biologi"])+(Data["Elo"]["matematika"])


IPK_Ali= ip_1/3 
IPK_Budi = ip_2/3 
IPK_Caca= ip_3/3 
IPK_Dodo= ip_4/3 
IPK_Elo = ip_5/3 


print("Ali", IPK_Ali,"Predikat A")
print("Budi", IPK_Budi,"Predikat C")
print("Caca", IPK_Caca,"Predikat B")
print("Dodo", IPK_Dodo,"Predikat B")
print("Elo", IPK_Elo,"Predikat B")






