# 代码目录说明

本目录包含零售货架商品检测系统的所有源代码。项目基于 YOLOv8 实现，针对 SKU110K 数据集的零售商品密集检测场景进行了优化。

## 文件功能说明

### 主要模块

| 文件名          | 功能描述                                               |
| --------------- | ------------------------------------------------------ |
| **main.py**     | 系统入口点，统一的命令行界面，支持训练、评估和预测模式 |
| **train.py**    | 模型训练模块，包含训练流程和超参数设置                 |
| **evaluate.py** | 模型评估模块，计算性能指标和可视化预测结果             |
| **predict.py**  | 预测模块，支持图像、视频和摄像头实时推理               |

### 工具脚本

| 文件名                     | 功能描述                                                 |
| -------------------------- | -------------------------------------------------------- |
| **convert_annotations.py** | 数据集转换工具，将 SKU110K 原始 CSV 标注转换为 YOLO 格式 |
| **fix_dataset.py**         | 数据集修复工具，处理数据集目录结构和标签一致性问题       |

### 资源文件

- **yolov8n.pt**: YOLOv8 nano 预训练模型权重

## 使用说明

### 1. 主程序 (main.py)

主程序提供统一的命令行接口，支持三种运行模式：

**训练模式**:

```bash
python main.py train
```

**评估模式**:

```bash
# 基础评估
python main.py eval

# 带可视化的评估
python main.py eval --viz --samples 10

# 指定模型路径
python main.py eval --model ../runs/SKU110K_detection041701/weights/best.pt
```

**预测模式**:

```bash
# 使用摄像头
python main.py predict

# 使用图像
python main.py predict --source path/to/image.jpg --save

# 使用视频
python main.py predict --source path/to/video.mp4 --save

# 设置置信度阈值
python main.py predict --source path/to/image.jpg --conf 0.4 --save

# 设置NMS IOU阈值
python main.py predict --source path/to/image.jpg --iou 0.5 --save
```

### 2. 训练模块 (train.py)

训练模块使用 YOLOv8 API 进行模型训练，主要特点：

- 使用 YOLOv8n 预训练模型进行迁移学习
- 针对小目标密集检测场景优化的超参数
- 自动适应硬件环境，调整训练参数

**主要超参数**:

- 学习率: 0.01 (带余弦调度)
- 边界框损失权重: 7.5 (针对小物体优化)
- 输入图像大小: 512px
- 批次大小: 根据 GPU 内存自动调整

### 3. 评估模块 (evaluate.py)

评估模块计算模型在测试集上的性能，并提供可视化功能：

- 计算 mAP50, mAP75, mAP50-95 等性能指标
- 生成混淆矩阵和 PR 曲线
- 可视化预测结果

### 4. 预测模块 (predict.py)

预测模块支持对单张图像、视频和摄像头的实时推理：

- 支持多种输入源
- 可调整的置信度和 NMS 阈值
- 结果可视化和保存功能

### 5. 数据转换工具 (convert_annotations.py)

将 SKU110K 数据集的原始标注格式(CSV)转换为 YOLO 格式：

- 处理训练集、验证集和测试集的标注
- 生成 YOLO 格式所需的 data.yaml 配置文件
- 创建适合训练的目录结构

### 6. 数据集修复工具 (fix_dataset.py)

修复数据集结构问题，确保图像和标签的正确对应：

- 标准化目录结构
- 检查并修复标签文件与图像文件的对应关系
- 更新 data.yaml 配置文件

## 自定义开发

如需进一步开发此项目，以下是主要修改点：

1. **修改模型架构**：在 train.py 中更改 YOLO 模型版本或替换为其他模型
2. **调整超参数**：修改 train.py 中的训练参数以适应特定场景
3. **添加新数据集**：扩展 convert_annotations.py 以支持新的数据集格式
4. **增强预测功能**：在 predict.py 中添加后处理步骤或新的视觉效果

## 依赖项

- ultralytics>=8.0.0
- torch>=1.7.0
- opencv-python>=4.5.0
- matplotlib
- numpy
