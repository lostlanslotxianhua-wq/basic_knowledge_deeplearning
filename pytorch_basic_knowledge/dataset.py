from torch.utils.data import Dataset

# mydataset继承Dataset类，以实现作为数据数据集的功能
class Mydata(Dataset):
    def __init__(self, path, label):
        self.path = path
        self.label = label
        self.data_path = os.listdir(slef.path)

    # 该方法用于访问对应索引处的数据
    def __getitem__(self, idx):
        pass

    # 该方法用于获得整个数据集的长度，这对计算loss有点作用
    def __len__(self):
        return len(self.path)