import matplotlib.pyplot as plt

Al_27=[64, 80, 62, 58, 56, 58]
MS_27=[55, 125, 118, 42, 115, 67]
MS_40=[26,8,12,14,60]
avg_Al_27=sum(Al_27)/len(Al_27)
avg_MS_27=sum(MS_27)/len(MS_27)
avg_Al_40=sum(MS_40)/len(MS_40)
x=['Aluminium at 27°C','Mild steel at 27°C','Mild steel at -40°C']
y=[avg_Al_27,avg_MS_27,avg_Al_40]

plt.bar(x,y)
plt.title('Impact energy for different materials')
plt.ylabel('Imapact enegy (J) using charpy test')

plt.show()