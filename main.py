def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# testing for Version 01

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import pandas as pd

pd.set_option('display.max_columns',10)
pd.set_option('display.max_rows',5)
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\user\Desktop\Data Analytics\GBvideos.csv")

x = data["channel_title"].head(5)
y = data["views"].head(5)
y1 = data["likes"].head(5)
plt.plot(x,y, marker = "o", color = "yellow")
plt.plot(x,y1, marker = "o", color = "red")
plt.title("channel title Vs Views and Likes")
plt.ylabel("Views / Likes")
plt.xlabel("Channel Title")
plt.show()


