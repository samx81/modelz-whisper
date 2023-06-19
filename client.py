from http import HTTPStatus

import requests
from datasets import load_dataset

import msgpack  # type: ignore


def main():
    # ds = load_dataset(
    #     "hf-internal-testing/librispeech_asr_dummy", "clean", split="validation"
    # )
    # sample = ds[0]["audio"]['path']
    # sample = "./example/1272-128104-0002.wav"
    sample = "/mnt/c/Users/Sam/Documents/ezai/debug_wavs/7554_chapters_sentence_412282_1686639328873.wav"
    print(sample)
    with open(sample, "rb") as f:
        req = {
            "binary": f.read(),
            "id": "1",
        }

        resp = requests.post("http://localhost:8080/inference", data=msgpack.packb(req))
    if resp.status_code == HTTPStatus.OK:
        print(resp.content.decode("utf-8"))
    else:
        print(resp.status_code, resp.text)


if __name__ == "__main__":
    main()
