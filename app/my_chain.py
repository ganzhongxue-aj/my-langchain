from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_redis import RedisChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import os

history = RedisChatMessageHistory(
    session_id="test",
    url="redis://59.110.5.225:6379/0",
    key_prefix="redis_chat_history",
)

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
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3-max"
)

#   定义输出格式

parser = StrOutputParser()

# chain =


chain = RunnableWithMessageHistory(prompt_template | model | parser, history)

res = chain.invoke({"query": "请写一个python程序，打印1到10"})
print(res)
res2 = chain.invoke({"query": "请再写一遍"})
print(res2)
res3 = chain.invoke({"query": "目前我们的对话有多少条"})
