import os
import shutil
from pathlib import Path

# 项目路径
ROOT_DIR = os.path.abspath('.')
YOLO_FORMAT_DIR = os.path.join(ROOT_DIR, 'data', 'SKU110K', 'yolo_format')
IMAGES_DIR = os.path.join(YOLO_FORMAT_DIR, 'images')
LABELS_DIR = os.path.join(YOLO_FORMAT_DIR, 'labels')

def main():
    print(f"修复数据集结构...")
    
    # 创建必要的目录
    os.makedirs(os.path.join(IMAGES_DIR, 'train'), exist_ok=True)
    os.makedirs(os.path.join(IMAGES_DIR, 'val'), exist_ok=True)
    os.makedirs(os.path.join(IMAGES_DIR, 'test'), exist_ok=True)
    
    # 移动根目录的图像到对应子目录
    for file in os.listdir(IMAGES_DIR):
        if not file.endswith('.jpg'):
            continue
            
        if file.startswith('train_'):
            dst = os.path.join(IMAGES_DIR, 'train', file)
            src = os.path.join(IMAGES_DIR, file)
            if not os.path.exists(dst) and os.path.exists(src):
                shutil.move(src, dst)
                print(f"移动: {file} -> train/")
        
        elif file.startswith('val_'):
            dst = os.path.join(IMAGES_DIR, 'val', file)
            src = os.path.join(IMAGES_DIR, file)
            if not os.path.exists(dst) and os.path.exists(src):
                shutil.move(src, dst)
                print(f"移动: {file} -> val/")
                
        elif file.startswith('test_'):
            dst = os.path.join(IMAGES_DIR, 'test', file)
            src = os.path.join(IMAGES_DIR, file)
            if not os.path.exists(dst) and os.path.exists(src):
                shutil.move(src, dst)
                print(f"移动: {file} -> test/")
    
    # 检查标签和图像的对应关系
    print("\n检查图像和标签的对应关系...")
    
    for split in ['train', 'val', 'test']:
        img_dir = os.path.join(IMAGES_DIR, split)
        label_dir = os.path.join(LABELS_DIR, split)
        
        # 检查所有图像都有对应的标签
        image_files = [f.stem for f in Path(img_dir).glob('*.jpg')]
        label_files = [f.stem for f in Path(label_dir).glob('*.txt')]
        
        missing_labels = set(image_files) - set(label_files)
        if missing_labels:
            print(f"{split}数据集中有 {len(missing_labels)} 个图像缺少标签")
        else:
            print(f"{split}数据集标签完整")
    
    # 更新data.yaml文件
    print("\n更新data.yaml配置文件...")
    data_yaml = os.path.join(YOLO_FORMAT_DIR, 'data.yaml')
    with open(data_yaml, 'w') as f:
        f.write("# SKU110K数据集配置\n\n")
        f.write(f"path: {YOLO_FORMAT_DIR}\n")
        f.write("train: images/train\n")
        f.write("val: images/val\n")
        f.write("test: images/test\n\n")
        f.write("# 类别数量和名称\n")
        f.write("nc: 1  # 类别数量\n")
        f.write("names: ['item']  # 类别名称\n")
    
    print("数据集结构修复完成!")

if __name__ == "__main__":
    main() 