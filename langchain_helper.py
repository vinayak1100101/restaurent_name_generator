from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from dotenv import load_dotenv
import os
load_dotenv()
os.environ['OPENAI_API_KEY']='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'

llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-4o-mini"
    
)
prompt_template_name=PromptTemplate(
    input_variables=['cusine'],
    template="I want to open a restaurant for {cusine} food, suggest one fancy name for it. Only give the name.")
name_chain=LLMChain(llm=llm,prompt=prompt_template_name,output_key="restaurent_name")
prompt_template_items=PromptTemplate(
    input_variables=['restaurent_name'],
    template="Imagine {restaurent_name} is a new {cusine} restaurant. Suggest a fancy sample menu in comma separated values. Just the menu items, no extra text.")
food_item_chain=LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu")
from langchain.chains import SequentialChain
chain=SequentialChain(
    chains=[name_chain,food_item_chain],
    input_variables=['cusine'],
    output_variables=['restaurent_name','menu']
)



def generate_restaurent_details(cuisine:str) ->dict :
    response=chain({'cusine':'indian'})
    return response

if __name__=="__main__":
    print(generate_restaurent_details(cuisine='indian'))
