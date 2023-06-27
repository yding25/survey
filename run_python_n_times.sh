#!/bin/bash

# 用法: ./run_python_n_times.sh <python_script> <number_of_runs>
# 示例: ./run_python_n_times.sh my_script.py 10

PYTHON_SCRIPT="$1"
NUMBER_OF_RUNS="$2"

# 检查参数数量
if [ "$#" -ne 2 ]; then
  echo "错误: 需要两个参数"
  echo "用法: ./run_python_n_times.sh <python_script> <number_of_runs>"
  exit 1
fi

# 检查Python脚本是否存在
if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "错误: 文件 '$PYTHON_SCRIPT' 不存在"
  exit 1
fi

# 检查是否为有效数字
if ! [[ "$NUMBER_OF_RUNS" =~ ^[0-9]+$ ]]; then
  echo "错误: 第二个参数必须为正整数"
  exit 1
fi

# 运行Python脚本N次
for ((j = 5; j < 51; j += 5)); do
  echo "Num. of Nodes: $j"
  echo "-------------nodes $j-------------" >> "all_results.txt"
  for ((i = 1; i <= NUMBER_OF_RUNS; i++)); do
    echo "运行次数: $i"
    python "$PYTHON_SCRIPT" $j
  done
done

echo "完成，共运行了 $NUMBER_OF_RUNS 次"
