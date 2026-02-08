from IPython.display import clear_output
from datetime import datetime
from google.colab import ai


#⚠️⚠️BY USING THIS AI YOU WILL GIVE YOUR MESSAGES AND QUERIES AND TIME TO GOOGLE BY USING THEIR AI⚠️⚠️
gmt="" #type your gmt time, if positive type it alone like +5 and if it is negative type like this -6
now=datetime.now()
fnow=f"Year: {now.year}   Month: {now.month}   Day: {now.day}{gmt}   Hour: {now.hour}+3    Minute: {now.minute}   Second: {now.second}"
chathistory=[]

chans=input("Do you have a chathistory? if yes paste it here if no type capitalized N: ")
clear_output()
if chans.strip().upper()=="N":pass
else:chathistory.append(chans)
clear_output()

chosen_model = "google/gemini-2.5-flash" #You can choose here the model. If you don't want or don't know how to change anything just leave it alone also it is recommended to leave it like this

#Personlization
traits = "!" #Type how will the AI act or the AI's
human_role = "!" #Type here info about you or your role


while True:
    if len(chathistory) > 500:
        chathistory.pop(0)
    print()
    #Chat history command
    query = input("👦You: ")
    if query.lower().strip() == "/ch":
        print()
        print("\n".join(chathistory))
        print()
        print("_" * 1000)
        continue

    formatted_history = "\n".join(chathistory)

    #Here is the query or prompt to the AI feel free to customize it
    full_prompt = (f"""
        Context: I am {human_role}.
        Instruction: Act as an assistant with these traits: {traits}.
        Constraint: Keep answers concise and don't be dry get my vibe and be energitic.
        ChatHistory: {formatted_history}
        Current Question: {query}
        Additional info: My time is {fnow}
        """
    )
    print()
    print("🤖AI is thinking...", end ="")
    try:
        response = ai.generate_text(full_prompt, model_name=chosen_model)

        # Use \r to replace the "thinking" text
        print(f"\r🤖AI: {response}")
        print("_" * 1000)

        #Saving to chat history
        chathistory.append(f" (Human: {query}  |  AI's response: {response})")

    except Exception as e:
        print(f"\r❌ Error: {e}")
