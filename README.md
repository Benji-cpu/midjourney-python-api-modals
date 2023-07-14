:bangbang: :bangbang: :bangbang: DISCLAIMER :bangbang: :bangbang: :bangbang:

1️⃣ I've taken the code from an open-source project. The original source details are as follows:

Source code: Midjourney-python-api (https://github.com/ezioruan/midjourney-python-api/tree/main)

2️⃣ This version is an enhanced version where I've added functionality to parse modal popups such as the remix, zoom out, pan features etc.

3️⃣ To achieve this, I've made adjustments to the Discum library to support modal features. Please note that the development on Discum has stopped by the original developer.

4️⃣ While I've done my best to implement the features, please keep in mind that I'm not a professional coder. There might be potential bugs, and I'd appreciate any feedback you have. Feel free to share your thoughts and suggestions in the Discord group (https://discord.gg/AJSGUVeMd9).

5️⃣ This project is based on the original codebase which you can find here: Midjourney-python-api Original Code (https://github.com/ezioruan/midjourney-python-api/tree/main).

6️⃣ I have not thoroughly tested the poetry.lock and requirements.txt files. If you encounter any issues, you may need to adjust these files to fit your specific needs.

Please use this code keeping the above points in mind. Happy coding! :smile:

:arrow_down: :arrow_down: :arrow_down: ORIGINAL README STARTS BELOW :arrow_down: :arrow_down: :arrow_down:


中文说明[README.zh_CN.md](README.zh_CN.md)
# midjourney-python-api
This is a Python client for the unofficial MidJourney API, This implementation uses a Discord self bot, and utilizes this library: Merubokkusu/Discord-S.C.U.M. Please be aware that there might be a risk of being banned.


### *** risky actions: [issue #66](https://github.com/Merubokkusu/Discord-S.C.U.M/issues/66#issue-876713938)

## Key Features
- [x] Info
- [x] Imagine prompt
- [x] Image Upscale and Vectorize by label
- [x] All messages return via WebSocket, including banned words check and image processing
- [x] Auto reconnect WebSocket

## Planned Features
- [ ] Multi-account support
- [ ] Full support for all MidJourney APIs


### Setup, choose one of the following methods

#### by pip
```bash
# use pip, create visual env
python -m venv .venv
pip install -r requirements.txt
```


### by poetry
```bash
poetry install
```


### Sample Code

```python 
python example.py
```


## Discussion
- discord : https://discord.gg/AJSGUVeMd9
