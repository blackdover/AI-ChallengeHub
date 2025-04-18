import argparse
import os
import sys
from train import train_model
from evaluate import evaluate_model, visualize_predictions

def parse_args():
    parser = argparse.ArgumentParser(description="零售货架商品检测 - YOLOv8")
    subparsers = parser.add_subparsers(dest="mode", help="运行模式")
    
    # 训练模式
    train_parser = subparsers.add_parser("train", help="训练模型")
    
    # 评估模式
    eval_parser = subparsers.add_parser("eval", help="评估模型")
    eval_parser.add_argument("--model", type=str, default=None, help="模型路径，默认使用最新训练的模型")
    eval_parser.add_argument("--viz", action="store_true", help="是否可视化预测结果")
    eval_parser.add_argument("--samples", type=int, default=5, help="可视化样本数量")
    
    return parser.parse_args()

def main():
    args = parse_args()
    
    if args.mode == "train":
        print("开始训练模型...")
        train_model()
        
    elif args.mode == "eval":
        print("评估模型性能...")
        # 如果未指定模型，使用默认的已训练模型
        if args.model is None:
            model_path = os.path.join(os.path.abspath('.'), 'runs/SKU110K_detection041701/weights/best.pt')
        else:
            model_path = args.model
            
        evaluate_model(model_path)
        
        if args.viz:
            print(f"可视化 {args.samples} 个预测结果...")
            visualize_predictions(model_path, args.samples)
            
    else:
        print("请指定运行模式: train, eval")
        print("例如: python main.py train")
        print("      python main.py eval --viz")
        sys.exit(1)

if __name__ == "__main__":
    main() 