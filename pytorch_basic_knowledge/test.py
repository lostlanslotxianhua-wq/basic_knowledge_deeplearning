import torch
import numpy as np
from torch.utils.tensorboard import SummaryWriter
import time

# 1. 创建 Writer 实例，日志将保存在 ./runs/fashion_mnist_experiment 目录下
writer = SummaryWriter('runs')

for n_iter in range(100):
    # 模拟 Loss：随步数增加逐渐减小，并加入一些随机噪声
    loss = 1.5 * (0.95 ** n_iter) + np.random.random() * 0.1
    # 模拟 Accuracy：随步数增加逐渐增大
    accuracy = 1 - (0.5 * (0.9 ** n_iter)) + np.random.random() * 0.05

    # 2. 写入数据
    # tag='Loss/train', scalar_value=loss (Y轴), global_step=n_iter (X轴)
    writer.add_scalar('Loss/train', loss, n_iter)
    writer.add_scalar('Accuracy/train', accuracy, n_iter)
    

# 3. 关闭 Writer
writer.close()
print("数据记录完毕！")