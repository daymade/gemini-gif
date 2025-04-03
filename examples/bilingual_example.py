#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bilingual example of programmatic usage of the gemini-gif package.
双语版本的 gemini-gif 包编程使用示例。

This example demonstrates how to use the gemini-gif package in your own Python code
without using the command-line interface.
本示例演示如何在您自己的 Python 代码中使用 gemini-gif 包，而不使用命令行界面。
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from gemini_coder.core import main, config
from loguru import logger

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

# Load API key from .env file
# 从 .env 文件加载 API 密钥
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please set it before running this example.")

logger.info(f"Using API key: {api_key[:5]}...{api_key[-5:]}")
logger.info(f"使用 API 密钥: {api_key[:5]}...{api_key[-5:]}")

# Define animation parameters
# 定义动画参数
subject = "a butterfly emerging from a cocoon"  # 一只蝴蝶从茧中羽化
style = "in a watercolor painting style"  # 水彩画风格
output_path = "butterfly_animation.gif"  # 输出文件路径

# Generate the animation
# 生成动画
logger.info(f"Generating animation of '{subject}' {style}")
logger.info(f"正在生成 '{subject}' {style} 的动画")

result = main.generate_animation(
    api_key=api_key,
    subject=subject,
    style=style,
    framerate=2,
    output_path=output_path,
    max_retries=3,
    verbose=True,
    log_file="gemini_coder.log"
)

# Check the result
# 检查结果
if result and os.path.exists(output_path):
    logger.success(f"Animation successfully generated at {output_path}")
    logger.success(f"动画成功生成于 {output_path}")
    logger.info(f"File size: {os.path.getsize(output_path) / 1024:.2f} KB")
    logger.info(f"文件大小: {os.path.getsize(output_path) / 1024:.2f} KB")
else:
    logger.error("Failed to generate animation")
    logger.error("生成动画失败")

"""
Alternative method using argparse.Namespace:
使用 argparse.Namespace 的替代方法：

If you need more control or want to use the same parameters as the CLI,
you can create an argparse.Namespace object manually:
如果您需要更多控制或想要使用与 CLI 相同的参数，
您可以手动创建一个 argparse.Namespace 对象：

```python
import argparse
from gemini_gif.core import main, config

args = argparse.Namespace(
    api_key=api_key,
    subject="a butterfly emerging from a cocoon",  # 一只蝴蝶从茧中羽化
    style="in a watercolor painting style",  # 水彩画风格
    template=config.DEFAULT_TEMPLATE,
    framerate=2,
    output="butterfly_animation.gif",
    max_retries=3,
    model=config.DEFAULT_MODEL,
    log_file="gemini_gif_generator.log",
    verbose=True,
    no_preview=False
)

result = main.run(args)
```
""" 