# Gemini Coder

[![PyPI version](https://img.shields.io/pypi/v/gemini-coder.svg)](https://pypi.org/project/gemini-coder/)
[![Python Versions](https://img.shields.io/pypi/pyversions/gemini-coder.svg)](https://pypi.org/project/gemini-coder/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/gemini-coder)](https://pepy.tech/project/gemini-coder)
[![GitHub stars](https://img.shields.io/github/stars/daymade/gemini-coder.svg)](https://github.com/daymade/gemini-coder/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/daymade/gemini-coder.svg)](https://github.com/daymade/gemini-coder/issues)

A Python tool that uses Google's Gemini API to generate animated GIFs from text prompts.

![dancing_robot_cyberpunk](https://github.com/user-attachments/assets/8ece4fe2-4060-4646-ac17-cb080c0028f5)
![animation_6b77c2c1-8e37-4775-af39-a45fecd4c046](https://github.com/user-attachments/assets/4555adee-4dc6-40f7-ac82-fc07425a51ce)
![butterfly_animation](https://github.com/user-attachments/assets/ce1630b6-07e2-48b9-874e-7b95fe0cffdd)

> 🙏 Inspired by [@Miyamura80's gist](https://gist.github.com/Miyamura80/b593041f19875445ca1374599d219387)

[English](#features) | [中文](#功能特点)

## Features

- Generate animated GIFs using Google's Gemini 2.0 Flash model
- Improved GIF generation with imageio for better compatibility and reliability
- Customize animation subject, style, and frame rate
- Automatic retry logic to ensure multiple frames are generated
- **Simple command-line interface** for quick and easy use
- Support for storing API key in .env file for convenience
- Progress bars for better user experience
- Programmatic API for integration into other projects

## Documentation

Comprehensive documentation is available to help you understand and extend the project:

- [Architecture Documentation](docs/ARCHITECTURE.md) - Detailed overview of the system design, component relationships, and data flow
- [Release Guide](RELEASE.md) - Instructions for releasing new versions of the package
- [Changelog](CHANGELOG.md) - History of changes and version updates
  - **Latest (0.1.2)**: Improved GIF generation with imageio for better compatibility

### Architecture Overview

![System Overview](docs/images/system_overview.png)

*High-level system overview showing the main components and their interactions.*

## Quick Start

```bash
# Install the package
pip install gemini-coder

# Set your API key (one-time setup)
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Generate a GIF with default settings (dancing cat in pixel art style)
gemini-coder

# Generate a GIF with custom subject and style
gemini-coder --subject "a dancing robot" --style "in a neon cyberpunk style"
```

## Requirements

- Python 3.10+
- Google Gemini API key

## Installation

### Using pip (Recommended)

```bash
# Install directly from PyPI
pip install gemini-coder
```

### System Requirements

## API Key Setup

You can provide your Gemini API key in several ways:

### Using a .env File (Recommended)

Create a file named `.env` in your current directory with the following content:

```
GEMINI_API_KEY=your_api_key_here
```

The script will automatically load the API key from this file.

### Using Environment Variables

```bash
# Set your Gemini API key as an environment variable
export GEMINI_API_KEY="your_api_key_here"
```

### Using Command-line Arguments

```bash
# Provide the API key directly as a command-line argument
gemini-coder --api-key "your_api_key_here" --subject "your subject"
```

## Command-line Usage

The command-line interface is the easiest way to use Gemini Coder:

```bash
# Generate a GIF with default settings (dancing cat in pixel art style)
gemini-coder

# Generate a GIF with custom subject and style
gemini-coder --subject "a dancing robot" --style "in a neon cyberpunk style"

# Save to a specific output file
gemini-coder --subject "a butterfly emerging from a cocoon" --output butterfly_animation.gif

# Enable verbose output for more detailed logs
gemini-coder --verbose

# Disable automatic preview of the generated GIF
gemini-coder --no-preview
```

### Command-line Options

```bash
gemini-coder --help
```

Available options:

- `--api-key`: Google Gemini API key (can also be set via GEMINI_API_KEY environment variable)
- `--subject`: Subject of the animation (default: "A cute dancing cat")
- `--style`: Style of the animation (default: "in a 8-bit pixel art style")
- `--template`: Template for the prompt (default: "Create an animation by generating multiple frames, showing")
- `--framerate`: Frames per second for the output GIF (default: 2)
- `--output`: Output file path (default: animation_<uuid>.gif)
- `--max-retries`: Maximum number of retries for generating frames (default: 3)
- `--model`: Gemini model to use (default: "models/gemini-2.0-flash-exp")
- `--log-file`: Path to the log file (default: gemini_coder_generator.log)
- `--verbose`: Enable verbose output
- `--no-preview`: Disable automatic preview of the generated GIF

### Examples

```bash
# Generate a blooming flower animation
gemini-coder --subject "a seed growing into a plant and then blooming into a flower" --style "in a watercolor style"

# Create a rocket launch animation with custom frame rate
gemini-coder --subject "a rocket launching into space" --style "in a retro sci-fi style" --framerate 3

# Save to a specific output file
gemini-coder --subject "a butterfly emerging from a cocoon" --output butterfly_animation.gif
```

## Programmatic Usage

You can also use the package programmatically in your own Python code:

```python
import os
from dotenv import load_dotenv
from gemini_coder.core.main import generate_animation

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Generate the animation
result = generate_animation(
    api_key=api_key,
    subject="a butterfly emerging from a cocoon",
    style="in a watercolor painting style",
    output_path="butterfly_animation.gif",
    framerate=2,
    verbose=True
)

if result:
    print(f"Animation successfully generated at {result}")
```

See the `examples/programmatic_usage.py` file for a complete example.

## Troubleshooting

- If you encounter issues with the Gemini API, check your API key and ensure you have access to the Gemini 2.0 Flash model.
- For any other issues, check the log file (`gemini_coder_generator.log`) for detailed error messages.
- Enable verbose output with `--verbose` for more detailed logs.

## License

This project is open source and available under the MIT License.

---

# Gemini Coder

[![PyPI version](https://img.shields.io/pypi/v/gemini-coder.svg)](https://pypi.org/project/gemini-coder/)
[![Python Versions](https://img.shields.io/pypi/pyversions/gemini-coder.svg)](https://pypi.org/project/gemini-coder/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/gemini-coder)](https://pepy.tech/project/gemini-coder)
[![GitHub stars](https://img.shields.io/github/stars/daymade/gemini-coder.svg)](https://github.com/daymade/gemini-coder/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/daymade/gemini-coder.svg)](https://github.com/daymade/gemini-coder/issues)

一个使用 Google Gemini API 从文本提示生成动画 GIF 的 Python 工具。

> 🙏 灵感来源于 [@Miyamura80 的 gist](https://gist.github.com/Miyamura80/b593041f19875445ca1374599d219387)

[English](#features) | [中文](#功能特点)

## 功能特点

- 使用 Google Gemini 2.0 Flash 模型生成动画 GIF
- 改进的 GIF 生成与 imageio 更好的兼容性和可靠性
- 自定义动画主题、风格和帧率
- 自动重试逻辑确保生成多个帧
- **简单的命令行界面**，使用快速方便
- 支持在 .env 文件中存储 API 密钥，使用更便捷
- 进度条提供更好的用户体验
- 提供编程 API，可集成到其他项目中

## 文档

我们提供了全面的文档，帮助您理解和扩展项目：

- [架构文档](docs/ARCHITECTURE.md) - 系统设计、组件关系和数据流的详细概述
- [发布指南](RELEASE.md) - 发布包新版本的说明
- [更新日志](CHANGELOG.md) - 变更历史和版本更新记录
  - **最新 (0.1.2)**: 改进的 GIF 生成与 imageio 更好的兼容性和可靠性

### 架构概览

![系统概览](docs/images/system_overview.png)

*高级系统概览，展示了主要组件及其交互。*

## 快速开始

```bash
# 安装包
pip install gemini-coder

# 设置 API 密钥（一次性设置）
echo "GEMINI_API_KEY=你的_API_密钥" > .env

# 使用默认设置生成 GIF（像素风格的跳舞猫）
gemini-coder

# 使用自定义主题和风格生成 GIF
gemini-coder --subject "一个跳舞的机器人" --style "霓虹赛博朋克风格"
```

## 系统要求

- Python 3.10+
- Google Gemini API 密钥

## 安装

### 使用 pip 安装（推荐）

```bash
# 直接从 PyPI 安装
pip install gemini-coder
```

### 系统要求

## API 密钥设置

你可以通过几种方式提供 Gemini API 密钥：

### 使用 .env 文件（推荐）

在当前目录创建一个名为 `.env` 的文件，内容如下：

```
GEMINI_API_KEY=你的_API_密钥
```

脚本将自动从此文件加载 API 密钥。

### 使用环境变量

```bash
# 将 Gemini API 密钥设置为环境变量
export GEMINI_API_KEY="你的_API_密钥"
```

### 使用命令行参数

```bash
# 直接在命令行参数中提供 API 密钥
gemini-coder --api-key "你的_API_密钥" --subject "你的主题"
```

## 命令行使用

命令行界面是使用 Gemini Coder 最简单的方式：

```bash
# 使用默认设置生成 GIF（像素风格的跳舞猫）
gemini-coder

# 使用自定义主题和风格生成 GIF
gemini-coder --subject "一个跳舞的机器人" --style "霓虹赛博朋克风格"

# 保存到特定的输出文件
gemini-coder --subject "一只蝴蝶从茧中羽化" --output butterfly_animation.gif

# 启用详细输出以获取更多日志信息
gemini-coder --verbose

# 禁用自动预览生成的 GIF
gemini-coder --no-preview
```

### 命令行选项

```bash
gemini-coder --help
```

可用选项：

- `--api-key`: Google Gemini API 密钥（也可以通过 GEMINI_API_KEY 环境变量设置）
- `--subject`: 动画主题（默认："A cute dancing cat"）
- `--style`: 动画风格（默认："in a 8-bit pixel art style"）
- `--template`: 提示模板（默认："Create an animation by generating multiple frames, showing"）
- `--framerate`: 输出 GIF 的帧率（默认：2）
- `--output`: 输出文件路径（默认：animation_<uuid>.gif）
- `--max-retries`: 生成帧的最大重试次数（默认：3）
- `--model`: 使用的 Gemini 模型（默认："models/gemini-2.0-flash-exp"）
- `--log-file`: 日志文件路径（默认：gemini_coder_generator.log）
- `--verbose`: 启用详细输出
- `--no-preview`: 禁用自动预览生成的 GIF

### 示例

```bash
# 生成一朵开花的动画
gemini-coder --subject "一颗种子长成植物然后开花" --style "水彩风格"

# 创建一个火箭发射动画，使用自定义帧率
gemini-coder --subject "一枚火箭发射到太空" --style "复古科幻风格" --framerate 3

# 保存到特定的输出文件
gemini-coder --subject "一只蝴蝶从茧中羽化" --output butterfly_animation.gif
```

## 编程使用

你也可以在自己的 Python 代码中以编程方式使用该包：

```python
import os
from dotenv import load_dotenv
from gemini_coder.core.main import generate_animation

# 从 .env 文件加载 API 密钥
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 生成动画
result = generate_animation(
    api_key=api_key,
    subject="一只蝴蝶从茧中羽化",
    style="水彩画风格",
    output_path="butterfly_animation.gif",
    framerate=2,
    verbose=True
)

if result:
    print(f"动画成功生成于 {result}")
```

查看 `examples/programmatic_usage.py` 文件获取完整示例。

## 故障排除

- 如果你遇到 Gemini API 问题，请检查你的 API 密钥并确保你有权访问 Gemini 2.0 Flash 模型。
- 对于任何其他问题，请查看日志文件（`gemini_coder_generator.log`）获取详细的错误信息。
- 使用 `--verbose` 参数启用详细输出，以获取更多调试信息。

## License

本项目是开源的，根据 MIT 许可证提供。 
