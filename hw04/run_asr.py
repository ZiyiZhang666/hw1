import vosk
import json
import wave
import os

def main():
    model_path = "vosk-model-small-cn-0.22"
    audio_path = r"D:\git\hw1\hw04\assets\my_voice_narration.wav"

    # 检查文件
    if not os.path.exists(model_path):
        print("模型不存在")
        return
    if not os.path.exists(audio_path):
        print("WAV 文件不存在")
        return

    print("一切正常，开始识别...")

    wf = wave.open(audio_path, "rb")
    model = vosk.Model(model_path)
    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    result_text = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            result_text += res.get("text", "") + " "

    res = json.loads(rec.FinalResult())
    result_text += res.get("text", "")

    # 输出结果
    print("\n" + "="*50)
    print("识别成功！正确文字如下：")
    print(result_text)
    print("="*50)

    # 保存
    with open("asr_result.txt", "w", encoding="utf-8") as f:
        f.write(result_text)

if __name__ == "__main__":
    main()