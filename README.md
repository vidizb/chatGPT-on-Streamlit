# chatGPT-on-Streamlit
Quick-try to implement chatGPT+Streamlit : using [pychatGPT](https://github.com/terry3041/pyChatGPT)

## Update : [could not make it work after 1-2 usage]
- Despite it works once/twice, Selenium error pops up 
- using MacOS - observed same behaviour in Safari / Chrome 
- Best guess, it's some incompatiblity with Streamlit cloud chromium with Selenium 

Any help would be appreciated :) 

## Usage -> Follow pychatGPT's guide : 

 > Obtaining session_token
  Go to https://chat.openai.com/chat and open the developer tools by F12.
  Find the __Secure-next-auth.session-token cookie in Application > Storage > Cookies > https://chat.openai.com.
  Copy the value in the Cookie Value field.

1. Clone this repo. `app.py` has the codes
2. `requirements.txt` & `packages.txt` for the dependencies

Step 1 and 2 + cookie value in secrets > while deployinh works well!! 

Also the app wokrs fine with 1/2 time usage max! Error pop ups after that . 
