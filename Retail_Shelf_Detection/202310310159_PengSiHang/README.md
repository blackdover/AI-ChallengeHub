# 零售货架商品检测项目

基于 YOLOv8 模型的零售货架商品密集目标检测系统，使用 SKU110K 数据集训练。该系统能够高效精确地检测货架上密集排列的商品，适用于零售行业的自动化库存管理。

## 项目背景

零售货架商品检测是零售行业中的一个重要应用场景，可用于自动化商品盘点、陈列分析和库存管理。本项目构建了一个高效的商品检测系统，能够在复杂的零售环境中准确识别密集排列的商品。实验结果表明，系统在 SKU110K 测试集上达到了 mAP50 为 0.86 的优秀性能。

## 数据集介绍

SKU110K 数据集包含 11,762 张零售货架图片，标注了商品的边界框位置。该数据集主要特点：

- **密集小目标**：商品在货架上密集排列，且相对图像尺寸较小
- **高度相似**：许多商品外观相似，增加了检测难度
- **真实场景**：图像来自真实零售环境，包含各种光照和视角变化

数据集分为三个子集：

- 训练集：8,219 张图像
- 验证集：588 张图像
- 测试集：2,936 张图像

## 模型性能

在 SKU110K 测试集上，本项目的检测模型达到了以下性能：

- **mAP50-95**: 0.523
- **mAP50**: 0.859
- **mAP75**: 0.577
- **精确率**: 0.874
- **召回率**: 0.779
- **推理速度**: >30 FPS (GPU)

## 项目结构

```
├── code/                     # 代码目录
│   ├── main.py               # 主入口脚本
│   ├── train.py              # 模型训练脚本
│   ├── evaluate.py           # 模型评估脚本
│   ├── predict.py            # 预测脚本
│   ├── convert_annotations.py # 数据集转换工具
│   ├── fix_dataset.py        # 数据集修复工具
│   └── yolov8n.pt            # YOLOv8n预训练模型
├── data/                     # 数据目录
│   └── SKU110K/              # SKU110K数据集
│       ├── images/           # 图像文件
│       ├── annotations/      # 原始标注
│       └── yolo_format/      # YOLO格式标注
├── runs/                     # 训练结果目录
│   └── SKU110K_detection041701/ # 训练结果
│       └── weights/          # 模型权重
│           ├── best.pt       # 最佳模型
│           └── last.pt       # 最新模型
├── results/                  # 评估结果目录
│   └── predictions.png       # 预测可视化结果
└── requirements.txt          # 项目依赖
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 数据准备与修复

如果需要转换原始数据集或修复数据结构：

```bash
# 转换原始数据集到YOLO格式
python code/convert_annotations.py

# 修复数据集结构
python code/fix_dataset.py
```

### 训练模型

```bash
python code/main.py train
```

### 评估模型

评估模型性能：

```bash
python code/main.py eval
```

评估并可视化结果：

```bash
python code/main.py eval --viz --samples 10
```

### 预测

使用摄像头进行实时预测：

```bash
python code/main.py predict
```

使用图像进行预测：

```bash
python code/main.py predict --source /path/to/image.jpg --save
```

使用视频进行预测：

```bash
python code/main.py predict --source /path/to/video.mp4 --save
```

## 模型优化策略

针对 SKU110K 数据集中的密集小目标检测问题，本项目采用了以下优化策略：

1. **数据集结构优化**

   - 确保图像和标签的正确对应
   - 使用标准的 YOLO 目录结构

2. **训练优化**

   - 使用余弦学习率调度
   - 提高边界框损失权重 (box=7.5)，适应小目标特点
   - 使用矩形训练提高训练效率

3. **检测优化**
   - 调整 NMS 阈值，处理密集商品场景
   - 提高召回率的置信度阈值设置
   - 使用类别无关 NMS(agnostic_nms=True)

## 系统要求

- Python 3.8+
- PyTorch 1.7+
- CUDA 支持（推荐用于训练）
- 内存：至少 8GB
- 存储空间：至少 20GB（包含数据集）

## 参考资料

1. [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
2. [SKU110K 数据集](https://github.com/eg4000/SKU110K_CVPR19)
3. [Dense Object Detection in Retail Scenarios](https://arxiv.org/abs/1904.00853)
