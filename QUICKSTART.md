# Gemini GIF Generator 快速入门指南

这个指南将帮助你快速安装和使用 Gemini GIF Generator。

## 安装

### 使用 pip 安装（推荐）

```bash
pip install gemini-gif
```

## 设置 API 密钥

你需要一个 Google Gemini API 密钥才能使用这个工具。有几种方式可以提供 API 密钥：

### 使用 .env 文件（推荐）

在当前目录创建一个名为 `.env` 的文件，内容如下：

```
GEMINI_API_KEY=你的_API_密钥
```

### 使用环境变量

```bash
# 设置 Gemini API 密钥为环境变量
export GEMINI_API_KEY="你的_API_密钥"
```

### 使用命令行参数

```bash
# 直接在命令行参数中提供 API 密钥
gemini-gif --api-key "你的_API_密钥" --subject "你的主题"
```

## 基本用法

安装后，你可以使用 `gemini-gif` 命令：

```bash
# 使用默认设置生成 GIF（像素风格的跳舞猫）
gemini-gif

# 使用自定义主题和风格生成 GIF
gemini-gif --subject "一个跳舞的机器人" --style "霓虹赛博朋克风格"

# 保存到特定的输出文件
gemini-gif --subject "一只蝴蝶从茧中羽化" --output butterfly_animation.gif

# 启用详细输出以获取更多日志信息
gemini-gif --verbose

# 禁用自动预览生成的 GIF
gemini-gif --no-preview
```

## 命令行选项

```bash
gemini-gif --help
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
- `--log-file`: 日志文件路径（默认：gemini_gif_generator.log）
- `--verbose`: 启用详细输出
- `--no-preview`: 禁用自动预览生成的 GIF

## 示例

```bash
# 生成一朵开花的动画
gemini-gif --subject "一颗种子长成植物然后开花" --style "水彩风格"

# 创建一个火箭发射动画，使用自定义帧率
gemini-gif --subject "一枚火箭发射到太空" --style "复古科幻风格" --framerate 3

# 保存到特定的输出文件
gemini-gif --subject "一只蝴蝶从茧中羽化" --output butterfly_animation.gif
```

## 编程使用

如果你想在自己的 Python 代码中使用 gemini-gif，可以使用以下方式：

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

## 故障排除

- 如果你遇到 Gemini API 问题，请检查你的 API 密钥并确保你有权访问 Gemini 2.0 Flash 模型。
- 对于任何其他问题，请查看日志文件（`gemini_gif_generator.log`）获取详细的错误信息。
- 使用 `--verbose` 参数启用详细输出，以获取更多调试信息。 