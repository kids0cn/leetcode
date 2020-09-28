import unittest

from survey import AnonymousSurvey
'''
class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to program?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")
        self.assertIn("English",my_survey.responses)

    def test_store_three_responses(self):
        question = "What language did you first learn to program?"
        my_survey = AnonymousSurvey(question)
        responses = ["English","Spanish","Madn"]
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)
'''


# 使用setUP()方法

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to program?"
        self.my_survey = AnonymousSurvey(question) # 创建一个调差对象
        self.responses = ['English','Spanish',"man"] # 创建一个答案列表
    
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    
    def test_store_three_responses(self):
        self.my_survey.store_response(self.responses)
        self.assertIn(self.responses,self.my_survey.responses)

unittest.main()