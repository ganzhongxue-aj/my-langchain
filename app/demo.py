from langchain_redis import RedisChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser

import os

#   先写提示词
prompt_template = ChatPromptTemplate(
    [
        ("system", "你是一个python高级工程师"),
        MessagesPlaceholder(variable_name="history"),
        ("human", '{input}'),
    ]
)

#   再定义模型
model = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3-max"
)


def get_session_history(session_ids: str) -> RedisChatMessageHistory:
    """根据 session_id 获取或创建 Redis 聊天历史"""
    return RedisChatMessageHistory(
        session_id=session_ids,
        redis_url="redis://59.110.5.225:6379/0",
        overwrite_index=True,
        ttl=3600
    )

parser = StrOutputParser()
runnable = RunnableWithMessageHistory(
    prompt_template | model | parser,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

