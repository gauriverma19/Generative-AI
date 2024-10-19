import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text,no_words,blog_style):

    ### LLama2 model

    print("Initializing model...")
    try:
        llm = CTransformers(model='models/llama-2-7b-chat.Q8_0.gguf', model_type='llama', config={'max_new_tokens': 500, 'temperature': 0.7})
        print("Model initialized successfully.")
    except Exception as e:
        print(f"Error initializing model: {e}")
        return "Model initialization failed."

    ## Prompt Template

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    print("Template Success!")
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    print("Prompt success!")
    ## Generate the ressponse from the LLama 2 model
    #response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))

    print("Response success!")
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))
    