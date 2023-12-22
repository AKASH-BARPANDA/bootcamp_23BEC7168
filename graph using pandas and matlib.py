import matplotlib.pyplot as plt
import pandas as pd

#plt. style.use('bmh')
df = pd.read_csv('/Users/akashbarpanda/Desktop/vscode/python/chatbot/US_House_Price.csv')
x = df['DATE']
y = df['house_for_sale_or_sold']

plt.xlabel('DATE',fontsize = 15)
plt.ylabel('house_for_sale_or_sold',fontsize = 15)

plt.bar(x,y)


# Line Graph
plt.xlabel('DATE', fontsize=18)
plt.ylabel( 'house_for_sale_or_sold', fontsize=16)
plt. scatter(x, y)
plt. plot(x,y)



plt.show()