import matplotlib.pyplot as plt
plt.rc("font",family="Microsoft JhengHei")
plt.plot([1,4,6],[[2,4,6],[3,7,10],[6,13,21]],label=["第一組","第二組","第三組"])
plt.legend()
plt.xlabel("X軸")
plt.ylabel("y軸")
plt.show()