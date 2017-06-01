# TOC-Project-2017
### 計算機理論project

* A telegram bot based on a finite state machine

### Prerequisite
* Python2 or Python3

#### 執行環境
* Linux

### API_TOKEN and WEBHOOK_URL
`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run the code.

此處的code中的`API_TOKEN`不需要更改，但`WEBHOOK_URL`需要被更改

#### 執行說明如下(Run Locally)
首先將ngrok這個執行檔(linux 32位元)載下來並執行
Use `ngrok` as a proxy.
**`ngrok` would be used in the following instruction**
```sh
./ngrok http 5000
```
在本機執行時要執行此指令，`ngrok`會產生一個新的https URL

設定 `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python app.py
    or
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"


## Author
[Tattos](https://github.com/Lee-W)


