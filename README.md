# sign-language-image-identification

### What is the ASL/BSL translator?
A computer vision/machine learning algorithm that identifies letters of the ASL and BSL alphabets to create phrases and translates between them.

### Background/Motivation
As an American living and studying in Great Britain, I frequently complain of not being able to understand the accent or slang. Whether it be scran, craic, or saying "I rate it" instead of "I like it", it often takes me a few seconds to understand what my friends or even professors are trying to communicate. However, this barrier is nothing compared to the barrier that the hard of hearing or deaf community faces.

Despite having English as a common tongue, ASL and BSL users cannot understand each other. Many hearing people expect them to be mutually intelligible, or perhaps like German and Dutch, which despite being two seperate languages have obvious similarities. However, this is not the reality. ASL and BSL are not mutually intelligible--a fairly basic sign to a user of one will be complete gibberish to a user of the other.

While obvious solution is just to write down what's trying to be communicated, this is often too time consuming and halts the flow of conversation. I wanted to create a machine learning algorithm that recognizes signs and creates phrases/sentences in real time, both producing a text version as well as displaying the equivalent in the other sign language (so if someone signs in BSL, it will output the same message in ASL). This allows not only a seamless flow of conversation, but provides sign language users to learn another country's sign.

The current goal of the program is to recognize the alphabet for both ASL and BSL. Once this is achieved I plan to add in numbers. This is obviously a quite limited sector of the languages, so in the future (training data permissible), I would like to expand the application to take in more complicated signs, particularly signs that involve movement.  

### Acknowledgements
- ASL image training set: @grassknoted on Kaggle

### Dataset Download Instructions
Due to size constraints, all datasets used in this project are **not included in the repository**. They must be downloaded manually using the Kaggle API. Please be aware this program will take a few GB's of space on your device.

Please follow these steps to set up and download the datasets:
1. **Install the Kaggle API**  
    Run:
    ```bash
    pip install kaggle
2. **Run the download script**
    Run download_data.py. This will create a folder called "data," download each dataset from Kaggle, and unzip it for you.