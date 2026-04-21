import pytest
import allure

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.moderation
def test_poll_creating(event_moderation_page,
                        question: str,
                        answer_1: str,
                        answer_2: str):
    """
    Test type - positive
    In this test we check if everything is okay with polls creating
    """
    event_moderation_page.click_on_create_new_button()
    event_moderation_page.click_on_poll_button()
    event_moderation_page.enter_question(question)
    event_moderation_page.enter_answer_1(answer_1)
    event_moderation_page.enter_answer_2(answer_2)
    event_moderation_page.click_on_save_button()
    event_moderation_page.wait_until_question_form_disappeared()
    assert question == event_moderation_page.first_draft_card_question()

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.moderation
def test_trivia_creating(event_moderation_page,
                         question: str,
                         points: int,
                         answer_1: str,
                         answer_2: str):
    """
    Test type - positive
    In this test we check if everything is okay with trivia creating
    """
    event_moderation_page.click_on_create_new_button()
    event_moderation_page.click_on_trivia_button()
    event_moderation_page.enter_question(question)
    event_moderation_page.enter_trivia_points(points)
    event_moderation_page.enter_answer_1(answer_1)
    event_moderation_page.enter_answer_2(answer_2)
    event_moderation_page.set_trivia_correct_answer_1()
    event_moderation_page.click_on_save_button()
    event_moderation_page.wait_until_question_form_disappeared()
    assert question == event_moderation_page.first_draft_card_question()

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.moderation
def test_prediction_creating(event_moderation_page,
                             question,
                             answer_1,
                             answer_2,
                             answer_1_points,
                             answer_2_points):
    """
    Test type - positive
    In this test we check if everything is okay with prediction creating
    """
    event_moderation_page.click_on_create_new_button()
    event_moderation_page.click_on_prediction_button()
    event_moderation_page.enter_question(question)
    event_moderation_page.enter_answer_1(answer_1)
    event_moderation_page.enter_answer_2(answer_2)
    event_moderation_page.enter_prediction_answer_1_points(answer_1_points)
    event_moderation_page.enter_prediction_answer_2_points(answer_2_points)
    event_moderation_page.click_on_save_button()
    event_moderation_page.wait_until_question_form_disappeared()
    assert question == event_moderation_page.first_draft_card_question()
