import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MaxNLocator, FuncFormatter
import tkinter as tk
from tkinter import filedialog

def plot_trace(file_path):
    # 读取CSV文件
    data = pd.read_csv(file_path, header=None, names=['Operation', 'Address', 'Size'])

    # 将地址列转换为十六进制
    data['Address'] = data['Address'].apply(lambda x: int(x, 16))

    # 提取访问地址和时间（行索引作为时间）
    addresses = data['Address']
    times = data.index

    # 绘制散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(times, addresses, s=10, alpha=0.6)

    # 设置纵轴刻度
    plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=10))  # 设置主刻度数量
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())  # 增加次刻度线

    # 自定义纵轴刻度格式为十六进制
    def hex_formatter(x, pos):
        return f'0x{int(x):X}'

    plt.gca().yaxis.set_major_formatter(FuncFormatter(hex_formatter))

    # 设置标签和标题
    plt.xlabel('Time')
    plt.ylabel('Address (Hex)')
    plt.title('Memory Access Addresses Over Time')
    plt.grid(True)

    # 旋转纵轴标签以提高可读性
    plt.yticks(rotation=45)

    plt.tight_layout()  # 自动调整子图参数，使其填充整个图像区域
    plt.show()

def select_file():
    # 打开文件选择对话框
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        plot_trace(file_path)

# 创建主窗口
root = tk.Tk()
root.title("Select Trace File")

# 创建按钮
select_button = tk.Button(root, text="Select Trace File", command=select_file)
select_button.pack(pady=20)

# 运行主循环
root.mainloop()