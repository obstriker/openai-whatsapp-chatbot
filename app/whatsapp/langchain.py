###
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

template = "hello my man"

chat = get_or_create(sender, chat_options)

prompt = PromptTemplate(
    input_variables=["history", "human_input"], 
    template=template
)

chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0), 
    prompt=prompt, 
    verbose=True, 
    memory=chat.memory,
)

## Check for number of messages
request_message = "..."
output = chatgpt_chain.predict(human_input=request_message)

chat_client.send_message(
    reply,
    chat.sender.phone_number,
    on_failure="סליחה, לא הבנתי , תוכל להסביר שוב?",
)


"""
chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0), 
    prompt=prompt, 
    verbose=True, 
    memory=ConversationBufferWindowMemory(k=2),
)
"""