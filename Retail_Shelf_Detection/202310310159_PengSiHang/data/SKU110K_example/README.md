# SKU110K 示例数据集

本目录包含 SKU110K 数据集的精选示例样本，用于快速测试和演示零售货架商品检测系统。完整数据集可以从[SKU110K 官方仓库](https://github.com/eg4000/SKU110K_CVPR19)获取。

## 目录结构

```
SKU110K_example/
├── images/           # 示例图像文件
│   ├── train/        # 训练集示例图像
│   ├── val/          # 验证集示例图像
│   └── test/         # 测试集示例图像
├── annotations/      # 原始标注文件
│   ├── train.csv     # 训练集标注
│   ├── val.csv       # 验证集标注
│   └── test.csv      # 测试集标注
└── README.md         # 数据集说明文件
```

## 数据集特点

SKU110K 是一个大规模的零售货架商品检测数据集，具有以下特点：

- **密集目标分布**：平均每张图像包含约 147 个商品实例
- **类内变化大**：同类商品在外观、尺寸和姿态上有较大变化
- **遮挡和重叠**：商品之间存在大量重叠，增加检测难度
- **真实场景**：数据来自真实零售环境，包括各种光照和视角变化

## 标注格式

示例数据集使用与原始 SKU110K 相同的标注格式：

原始 CSV 文件格式（每行一个标注）：

```
image_name,x1,y1,x2,y2,class,image_width,image_height
train_0.jpg,10,20,50,60,object,1000,800
...
```

各字段说明：

- `image_name`: 图像文件名
- `x1,y1`: 商品边界框左上角坐标
- `x2,y2`: 商品边界框右下角坐标
- `class`: 类别标签（所有商品均标为"object"）
- `image_width,image_height`: 图像尺寸

## 使用方法

示例数据集主要用于以下用途：

1. **快速测试系统功能**：不需下载完整数据集即可测试系统

2. **演示检测效果**：展示系统在零售场景中的表现

3. **调试模型参数**：快速迭代测试参数变化的影响

### 转换为 YOLO 格式

使用转换脚本将示例数据转换为 YOLO 训练格式：

```bash
python code/convert_annotations.py --source data/SKU110K_example --target data/SKU110K_example/yolo_format
```

### 使用示例数据进行预测

```bash
python code/main.py predict --source data/SKU110K_example/images/test/test_1.jpg --save
```

## 注意事项

- 此示例数据集仅包含少量图像，不适合完整训练，仅用于测试和演示
- 转换脚本会自动生成 YOLO 格式所需的 data.yaml 配置文件
- 推荐使用预训练模型对示例数据进行推理，而不是从头训练
