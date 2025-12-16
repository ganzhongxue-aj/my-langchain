from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

#   先写提示词
system_prompt = "你是一个python高级工程师"
prompt_template = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("user", '{query}'),
    ]
)



#   再定义模型
model = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url= "https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3-max"
)

#   定义输出格式

parser = StrOutputParser()

chain = prompt_template | model | parser


