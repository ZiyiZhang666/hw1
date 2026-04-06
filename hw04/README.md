# hw04 开源语音识别与声音克隆作业
本仓库包含 hw04 的完整作业代码与文档。

## 项目结构
- `text_gen.md`: 大模型生成的文稿脚本。
- `jianying.md`: 剪映声音克隆操作说明。
- `asr_report.md`: 开源 ASR (Whisper) 调研与实验报告。
- `run_asr.py`: 本地语音识别运行代码。
- `requirements.txt`: 环境依赖清单。

## 快速运行 (ASR 任务)
1. 进入目录: cd hw04
2. 安装依赖: pip install -r requirements.txt
3. 运行识别: python run_asr.py --audio assets/你的音频.mp3