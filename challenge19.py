#!/usr/bin/env python3

from common import does_file_exist, authentication_help
from base64 import standard_b64decode
import wave

LOCAL_FILE_PATH = "bin.html"


def switch_endian():
    # TODO: implement this for real
    # The Python WAV libraries don't support endian order.
    # Kludge by "merging" the channels.
    # Switching endian order probably can be done via pack.
    wf = wave.open("c19.wav", "rb")
    frames = wf.readframes(wf.getnframes())
    result = wave.open("result.wav", "wb")
    result.setnchannels(wf.getnchannels())
    result.setsampwidth(wf.getsampwidth() // 2)
    result.setframerate(wf.getframerate() * 2)
    result.writeframes(frames)


def main():
    if not does_file_exist(LOCAL_FILE_PATH, "Challenge 1"):
        exit()

    line_num = 0
    data = ""
    with open(LOCAL_FILE_PATH) as in_file, open(f"c19.wav", "wb") as out_file:
        for line in in_file:
            # TODO - don't hardcode extracting out the attachment
            line_num += 1
            if line_num < 28:
                continue
            data += line.strip()
        wav_data = standard_b64decode(data)
        out_file.write(wav_data)
    switch_endian()
    print("As you can see, this does not print the result in a traditional format.")
    print("In fact, it's not graphical at all.  Listen to result.wav.  Listen to what you are called.")
    print("Use the standard format of: http://www.pythonchallenge.com/pc/hex/{answer}.html")
    authentication_help("hex")


if __name__ == "__main__":
    main()
