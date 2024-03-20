import os
import nest_asyncio
from dotenv import load_dotenv

nest_asyncio.apply()
load_dotenv()

from datasets import Dataset

import openai

from ragas import evaluate
from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    context_recall,
    context_precision,
)
from ragas.metrics.critique import harmfulness
import openai


os.environ['OPENAI_API_KEY'] = os.environ['OPENAI_API_KEY']
openai.api_key = os.getenv('OPENAI_API_KEY')

import pandas as pd
import json

# ...Lưu ý: Comment lại đoạn này khi chạy code Ragas để hệ thống không chạy mấy phần dư thừa như call api openai,...
# ......................................Đoạn generation tập test ............................................ 

# from prompts import text_qa_template
# from simpleRAG import genaration_qa
# from chat import ChatEngine, generate_queries
# from testIntent import intent_classification
# # pip install openpyxl
# from openpyxl import Workbook


# def get_answer_and_contexts_simple(question):
#     generation = genaration_qa(question=question)
#     answer = generation.response
#     contexts = []
#     for node in generation.source_nodes:
#         contexts.append(node.text)
        
#     return answer, contexts

# def get_answer_and_contexts(question):
    
#     intent = json.loads(intent_classification(question))
#     response = ""
#     contexts = []

#     if intent['response'] == "Chào hỏi":
#         response = "Xin chào, tôi là trợ lý ảo có thể trả lời các câu hỏi về pháp luật, tôi có thể giúp gì cho bạn?"
#     elif intent['response'] == "Chủ đề khác":
#         response = "Câu hỏi của bạn không hợp lệ, hoặc không liên quan đến Pháp Luật. Vui lòng kiểm tra lại và cung cấp thêm thông tin cho tôi"
#     else:
#         queries = generate_queries(question)
#         response, references = chatEngine.chat_en(queries, question)
        
#         for node in references:
#             contexts.append(node['content'])
        
#     return response, contexts

# def read_data_test(filename):
    
#     # Read data test file
#     df = pd.read_excel(filename)

#     # Convert DataFrame to a list of dictionaries
#     list_of_dicts = df.to_dict(orient='records')

#     return list_of_dicts

# def export_data_test(filename, data_list):

#     # Create a new Workbook
#     wb = Workbook()

#     # Select the active worksheet
#     ws = wb.active

#     # Set the column headers
#     ws.append(['question', 'ground_truth'])
    
#     for data in data_list:
#         ws.append([data['question'], data['ground_truth']])

#     # Save the workbook
#     wb.save(filename)

# ................................end................................................
    

if __name__ == "__main__":
    
    # ............................Advanced RAG......................................
    # 1. Chạy đoạn này để sinh ra answer và context. Sau khi chạy xong hãy comment lại và mở phần ragas chạy tiếp
    
    # data_list = read_data_test('input.xlsx')
    
    # chatEngine = ChatEngine()
    # data_advanced_rag = [{"question": i['question'], "ground_truth": i['ground_truth']} for i in data_list]
    # for data in data_advanced_rag:
    #     answer, contexts = get_answer_and_contexts(data['question'])
    #     data["answer"] = answer
    #     data["contexts"] = contexts
    
    # with open('data_advanced_rag.json', 'w') as file:
    #     json.dump(data_advanced_rag, file)
    
    # 2. Phần Ragas ...................................................................
    
    # Use Ragas for evaluating after generating step
    with open('data_advanced_rag.json', 'r') as file:
        # Load JSON data from the file
        data_list= json.load(file)
    
    data_list = [i for i in data_list if len(i['contexts']) != 0 ]
    print(len(data_list))
    
    ds = Dataset.from_list(data_list)
    
    result = evaluate(
        ds,
        metrics=[
            context_precision,
            faithfulness,
            answer_relevancy,
            context_recall,
        ],
    )
    
    print(result)
    
    
    # ...........................simple RAG......................................
    # data_simple_rag = [{"question": i['question'], "ground_truth": i['ground_truth']} for i in data_list]
    # for data in data_simple_rag:
    #     answer, contexts = get_answer_and_contexts_simple(data['question'])
    #     data["answer"] = answer
    #     data["contexts"] = contexts
    
    # print(data_simple_rag)
    # with open('data_simple_rag.json', 'w') as file:
    #     json.dump(data_simple_rag, file)

    
    # Use Ragas for evaluating after generating step
    # with open('data_simple_rag.json', 'r') as file:
    #     # Load JSON data from the file
    #     data_list= json.load(file)
    # data_list = [i for i in data_list if len(i['contexts']) != 0 ]
    # print(len(data_list))
    
    # ds = Dataset.from_list(data_list)
    
    # result = evaluate(
    #     ds,
    #     metrics=[
    #         context_precision,
    #         faithfulness,
    #         answer_relevancy,
    #         context_recall,
    #     ],
    # )
    
    # print(result)