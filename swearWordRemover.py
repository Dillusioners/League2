#Inputting the sentence
a = str.lower(input("Enter your nab paragraph: "))
#splitting the paragraph into word elements
para = a.split()
i = 0
z = 0
#Creating an array of swear words
swear = ['fuck', 'dick','pussy','nigga','boobs','tit','bitch','ass','whore','porn','johnny sins','cunt','wanker','gandu','asshole','tittyfuck','anal','bukkake','creampie','stepsis','slut','urmum','cocksucker']
print('All Swear words found: ')
#checking if z index of para is a swear word from swear array and gets removed
while i != len(para):
    while z != len(swear):
        if swear[z] in para[i]:
            print(para[i])
        z += 1
    z = 0
    i += 1