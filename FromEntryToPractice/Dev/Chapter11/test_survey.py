import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_suevey():
    """一个可供所有测试函数使用的AnonymousSurvey实例"""
    question = "What language did you first learn to speak?"
    language_suevey = AnonymousSurvey(question)
    return language_suevey


def test_store_single_responses(language_suevey):
    """测试单个答案也会被妥善的存储"""
    language_suevey.store_response('English')
    assert 'English' in language_suevey.responses


def test_store_three_responses(language_suevey):
    """测试三个答案也会被妥善的存储"""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_suevey.store_response(response)

    for response in responses:
        assert response in language_suevey.responses
