import glob
import os
import time

import openai
from PyPDF2 import PdfReader

from bi import get_bing_ai_res


def get_pdf_info(path):
    with open(path, "rb") as f:
        pdf = PdfReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    print(info)

    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title

    print(f"Author: {author}")
    print(f"Creator: {creator}")
    print(f"Producer: {producer}")
    print(f"Subject: {subject}")
    print(f"Title: {title}")
    print(f"Number of pages: {number_of_pages}")

    return number_of_pages


def get_pdf_content(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        number_of_pages = len(reader.pages)
        content = ""
        for page_number in range(number_of_pages):
            content += reader.pages[page_number].extract_text()
        return content


def get_questions(pdf_path):
    content = get_pdf_content(pdf_path)

    file_path = pdf_path.replace(".pdf", "")

    file_path = file_path + "/questions.txt"
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf8") as file:
            content = file.read()

        return content

    openai.api_key = "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"

    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=f"qp:\nPrinted Page: 1 of 2 \n    Subject Code: KOE068 \n0Roll No:  0  0  0  0  0  0  0  0  0  0  0  0  0 \n \nBTECH \n(SEM VI) THEORY EXAMINATION 2021-22 \nSOFTWARE PROJECT MANAGEMENT \n \nTime: 3 Hours        Total Marks: 100 \nNote:  Attempt all Sections. If you require any missing data, then choose suitably. \n \nSECTION A \n1.  Attempt all  q u e s t i o n s   i n   b r i e f .               2*10 = 20 \nQ.no  Questions  Marks  CO \n(a)   Define Software Project Management.  2  1 \n(b)   Briefly discuss about the Project Evaluation.  2  1 \n(c)   Define Project Life Cycle.  2  2 \n(d)   Discuss about the Effort Estimation.  2  2 \n(e)   Briefly discuss about the need of Activity Planning.  2  3 \n(f)   What do you mean by Risk Management?  2  3 \n(g)   What do you mean by Project Management and Control?  2  4 \n(h)   Define Framework for Management.  2  4 \n(i)   What do you understand by the Organizational behavior?  2  5 \n(j)   Discuss about the need of Staffing in Software Projects.  2  5 \n \nSECTION B \n2.  Attempt any three  o f   t h e   f o l l o w i n g :               10*3 = 30 \nQ.no  Questions  Marks  CO \n(a)   Explain in detail about the Best methods of staff selection Motivation.   10  5 \n(b)   Write short notes on any two of the following: \n (i) Software process and Process Models \n(ii) Choice of Process models \n(iii) Rapid Application development(RAD) \n10  2 \n(c)   What  do  you  mean  by  Project  schedules?  Mention  the  Objectives  of \nActivity planning. \n10  3 \n(d)   Discuss about the concept and need of Cost monitoring Earned Value \nAnalysis. \n10  4 \n(e)   Describe   the   activities   and   Importance   of   Software   Project \nManagement. \n10  1 \n \nSECTION C \n3.  Attempt any one part of the following:                      10*1 = 10 \nQ.no  Questions  Marks  CO \n(a)   What is the concept and need of Agile methods in Project Life Cycle?   10  2 \n(b)   Explain about the Oldham Hackman job characteristic model under the \nStaffing in Software Projects. \n10  5 \n \n \n \nPrinted Page: 2 of 2 \n    Subject Code: KOE068 \n0Roll No:  0  0  0  0  0  0  0  0  0  0  0  0  0 \n \nBTECH \n(SEM VI) THEORY EXAMINATION 2021-22 \nSOFTWARE PROJECT MANAGEMENT \n \n4.  Attempt any one  p a r t   o f   t h e   f o l l o w i n g :            10 *1 = 10 \nQ.no  Questions  Marks  CO \n(a)   Discuss in detail about the Categorization of Software Projects.  10  1 \n(b)   Discuss  about  the  Forward  Pass  and  Backward  Pass  techniques  in  \nActivity Planning and Risk Management. \n10  3 \n \n5.  Attempt any one  p a r t   o f   t h e   f o l l o w i n g :             10*1 = 10 \nQ.no  Questions  Marks  CO \n(a)   Discuss  in  detail  about  the  Change  control  Software  Configuration \nManagement. \n10  4 \n(b)   Explain in detail about any two of the following. \n(i) Stress. \n(ii) Health and Safety. \n(ii) Ethical and Professional concerns. \n10  5 \n \n6.  Attempt any one  p a r t   o f   t h e   f o l l o w i n g :             10*1 = 10 \nQ.no  Questions  Marks  CO \n(a)   Describe any two of the following. \n(i) Basics of Software estimation. \n(ii) Effort and Cost estimation. \n(iii) Dynamic System Development Method. \n10  2 \n(b)   Write down about any two of the following. \n(i) Critical path (CRM) method. \n(ii) Risk identification. \n(iii) PERT technique. \n10  3 \n \n7.  Attempt any one  p a r t   o f   t h e   f o l l o w i n g :             10*1 = 10 \nQ.no  Questions  Marks  CO \n(a)   Briefly discuss any two of the following through an example. \n(i) Cost-benefit evaluation technology \n(ii) Risk evaluation \n(iii) Stepwise Project Planning \n10  1 \n(b)   Write  down  about  the  concept  of  Contract  Management  under  the \nManagement Technique. \n10  4 \n\nList all questions in , if the question can have a very long answer then divide that question in parts\n\nresult:\n###\n|(this question came in the exam of subject SOFTWARE PROJECT MANAGEMENT)|\n#\n1a\nDefine Software Project Management.\n#\n1b\nBriefly discuss about the Project Evaluation.\n#\n1c\nDefine Project Life Cycle. \n#\n1d \nDiscuss about the Effort Estimation.\n#\n1e\nBriefly discuss about the need of Activity Planning.\n#\n1f\nWhat do you mean by Risk Management? \n#\n1g\nWhat do you mean by Project Management and Control?\n#\n1h\nDefine Framework for Management.\n#\n1i\nWhat do you understand by the Organizational behavior?\n#\n1j\nDiscuss about the need of Staffing in Software Projects.\n#\n2a\nExplain in detail about the Best methods of staff selection Motivation.\nWhat are staff selection and motivation?\nWhat are some criteria for selecting staff for software projects?\nWhat are some methods for motivating staff in software projects?\nWhat are some benefits and challenges of staff selection and motivation?\n#\n2b\nWrite short notes on Software process and Process Models \nWrite short notes on Choice of Process models \nWrite short notes on Rapid Application development(RAD) \n#\n2c\nWhat do you mean by Project schedules? \nMention the Objectives of Activity planning.\n#\n2d\nDiscuss about the concept of Cost monitoring Earned Value Analysis. \n#\n2e\nDescribe the activities of Software Project Management.\nDescribe the Importance of Software Project Management.\n#\n3a\nWhat are agile methods?\nWhat are the characteristics of agile methods?\nHow do agile methods differ from traditional methods?\nWhat are some examples of agile methods?\nWhat are some benefits and challenges of using agile methods?\nWhat is the need of Agile methods in Project Life Cycle? \n#\n3b\nExplain about the Oldham Hackman job characteristic model under the Staffing in Software Projects. \n#\n4a\nDiscuss in detail about the Categorization of Software Projects.\n#\n4b\nWhat are forward pass and backward pass techniques?\nHow are they used in activity planning and risk management?\nWhat are the steps involved in applying these techniques?\nWhat are some advantages and disadvantages of these techniques?\n#\n5a\nDiscuss in detail about the Change control Software Configuration Management. \n#\n5b\nExplain in detail about Stress. \nExplain in detail about Health and Safety. \nExplain in detail about Ethical and Professional concerns. \n#\n6a\nDescribe Basics of Software estimation. \nDescribe Effort and Cost estimation. \nDescribe Dynamic System Development Method. \n#\n6b\nWrite down about Critical path (CRM) method. \nWrite down about Risk identification. \nWrite down about PERT technique. \n#\n7a\nBriefly discuss Cost-benefit evaluation technology \nBriefly discuss Risk evaluation \nBriefly discuss Stepwise Project Planning \n#\n7b\nExplain the concept of Contract Management under the Management Technique.\nProvide a detailed overview of the key aspects of Contract Management as a management technique.\nDescribe the various stages of Contract Management and their significance in ensuring successful implementation.\nDiscuss the challenges faced in Contract Management and the strategies used to overcome them.\nAnalyze the role of technology in Contract Management and its impact on the process.\nShare examples of successful Contract Management practices and their impact on business operations.\n____________\nqp:\n\n{content}\n\nList all questions in , if the question can have a very long answer then divide that question in parts\n\nresult:\n###",
        temperature=0,
        max_tokens=3666,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["____________"],
    )
    text = response["choices"][0]["text"]

    with open(file_path, "a", encoding="utf8") as file:
        file.write(f"{text}")

    return text


def main(content_type="text"):
    files = glob.glob("question_papers/**/*.pdf", recursive=True)

    for file in files:
        process_pdf_file(file)


def process_pdf_file(file_path):
    print(file_path)

    questions = get_questions(file_path)

    questions = questions.strip()

    questions = questions.split("#")

    # pop first element
    init = questions.pop(0)

    # remove empty elements
    questions = list(filter(None, questions))

    print(questions)

    for question in questions:
        questions_in_question = question.splitlines()

        questions = []

        for question in questions_in_question:
            questions.extend(question.split("?"))

        questions_in_question = []

        for question in questions:
            questions_in_question.extend(question.split("."))

        questions = []

        for question in questions_in_question:
            questions.extend(question.split(","))

        questions = list(filter(None, questions))

        question_numer = questions.pop(0)

        question_file_path = (
            file_path.replace(".pdf", "") + "/" + question_numer + ".md"
        )

        for question in questions:
            if not os.path.exists(os.path.dirname(question_file_path)):
                os.makedirs(os.path.dirname(question_file_path))

            # read the file

            try:
                with open(question_file_path, "r", encoding="utf8") as file:
                    initial_content = file.read()
            except:
                initial_content = ""

            if question in initial_content:
                continue
            answer = get_bing_ai_res(question + init)

            with open(question_file_path, "a", encoding="utf8") as file:
                file.write(f"## {question}\n\n")

                file.write(f"{answer}\n\n")


if __name__ == "__main__":
    while True:
        try:
            main()

        except Exception as error:
            time.sleep(60)
            print(error)
