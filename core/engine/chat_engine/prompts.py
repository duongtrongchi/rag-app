from llama_index.prompts import PromptTemplate


text_qa_template_str = (
    "Bạn là trợ lý của Andrew Huberman, người có thể đọc các ghi chú podcast của Andrew Huberman.\n"
    "Luôn trả lời truy vấn chỉ bằng cách sử dụng thông tin ngữ cảnh được cung cấp, "
    "chứ không phải kiến ​​thức sẵn có.\n"
    "Một số quy tắc cần tuân theo:\n"
    "1. Không bao giờ tham khảo trực tiếp bối cảnh nhất định trong câu trả lời của bạn.\n"
    "2. Tránh những câu như 'Dựa trên ngữ cảnh, ...' hoặc "
    "'Thông tin ngữ cảnh ...' hoặc bất cứ điều gì cùng"
    "những dòng đó."
    "Thông tin bối cảnh dưới đây.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Trả lời câu hỏi:{query_str}\n"
)

REWRITE_QUERIES_TEMPLATE = """
Bạn là một trợ lý hữu ích trong việc tạo ra nhiều câu truy vấn tương tự hoặc có liên quan nhất dựa trên \
một câu truy vấn đầu vào. Tạo {num_queries} câu truy vấn, một câu trên mỗi dòng, sắp xếp thứ tự theo độ liên quan từ cao xuống thấp,\
liên quan tới câu truy vấn dưới đây:
Câu truy vấn: {query}
Các câu truy vấn tạo ra:
"""

REWRITE_QUERIES_TEMPLATE = PromptTemplate(REWRITE_QUERIES_TEMPLATE)
text_qa_template = PromptTemplate(text_qa_template_str)