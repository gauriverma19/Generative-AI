# Generating Blogs using LLama2 model

Steps:
* Download the LLama2 7b GGUF model and store it in a folder named 'models'
* Create the requirements.txt file as mentioned
* GGUF model is used instead of the GGML version as the latest version of langchain-community doesnt read the GGML version
* It can take upto 10 minutes to view the blog output if running on a basic CPU system
* To run the model, run the commeand 'streamlit run app.py' in the terminal

### References
* LLam2 research paper: https://arxiv.org/abs/2307.09288
* Krish Naik for helpful youtube content: https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/channel/UCNU_lfiiWBdtULKOw6X0Dig&ved=2ahUKEwietOHJ8pqJAxXwEVkFHY3uAD0QFnoECAkQAQ&usg=AOvVaw2PAfXfwR5FQgNnxjuYAKgj
* Meta Article of LLama2: https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/&ved=2ahUKEwj6_6u68pqJAxW5L1kFHVzVOx0QFnoECB0QAQ&usg=AOvVaw1MRxLFbwzXkrWpUa7sDsj7
