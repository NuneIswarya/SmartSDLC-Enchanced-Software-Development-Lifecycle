"""
Untitled9.ipynb

Original file is located at
https://colab.research.google.com/drive/1g8uBzEIg5jugQgDQuf7QHVGVZBdkGBg1
"""

!pip install pymupdf
import fitz 
import re
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()
def classify_sentences(text):
    sentences = re.split(r'(?<=[.?!])\s+', text)
    classified = []
    for sentence in sentences:
        if 'shall' in sentence.lower() or 'must' in sentence.lower():
            phase = "Requirements"
        elif 'design' in sentence.lower():
            phase = "Design"
        elif 'test' in sentence.lower():
            phase = "Testing"
        elif 'code' in sentence.lower() or 'develop' in sentence.lower():
            phase = "Development"
        else:
            phase = "Others"
        classified.append((sentence, phase))
    return classified
def generate_user_stories(classified_sentences):
    user_stories = []
    for sentence, phase in classified_sentences:
        if phase == "Requirements":
            story = f"As a user, I want {sentence.lower()} so that it fulfills a business need."
            user_stories.append(story)
    return user_stories
pdf_url = "https://arxiv.org/pdf/1706.03762.pdf" 
import urllib.request
urllib.request.urlretrieve(pdf_url, "sample.pdf")
pdf_text = extract_text_from_pdf("sample.pdf")
classified = classify_sentences(pdf_text[:2000]) 
user_stories = generate_user_stories(classified)
classified = classify_sentences(pdf_text)
user_stories = generate_user_stories(classified)

print("Extracted Requirements and User Stories:\n")
for story in user_stories[:5]:
    print("👉", story)
