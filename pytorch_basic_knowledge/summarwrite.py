from torch.utils.tensorboard import SummaryWriter

# 创建一个 SummaryWriter 实例，你可以指定日志保存的目录（默认为 runs/）。
writer = SummaryWriter("logs")


# 记录标量 (Scalars): 比如 Loss 和 Accuracy。add_scalar(标签, 数值, 迭代步数)
writer.add_scalar('Loss/train', 0.85, 1)
writer.add_scalar('Accuracy/train', 0.70, 1)


# 记录图像 (Images): 查看模型中间生成的图片或输入样本。img_tensor 为 (C, H, W) 格式
writer.add_image('Input_Data', img_tensor, global_step=0)


# 记录模型结构: 看看你的网络层是怎么连接的。
writer.add_graph(model, input_to_model)


# 训练结束后，务必关闭 writer 以确保所有数据都已写入磁盘。
writer.close()


'''
打开终端（命令行），导航到你的项目根目录，运行该命令启动TensorBoard：tensorboard --logdir=logs。
运行出来后会显示很多内容，其中有一段关于tensorboard的链接，点击之后即可转到tensorboard
'''