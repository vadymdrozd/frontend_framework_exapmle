from dataclasses import dataclass

from selenium.webdriver.common.by import By

from core.locator import Locator


@dataclass(frozen=True, init=False)
class LocatorsCollection:
    create_new_button: Locator = Locator(By.XPATH, "//*[@data-testid='create-question']")
    poll_button: Locator = Locator(By.XPATH, "//*[@data-testid='create-poll']")
    trivia_button: Locator = Locator(By.XPATH, "//*[@data-testid='create-trivia']")
    prediction_button: Locator = Locator(By.XPATH, "//*[@data-testid='create-prediction']")
    question_input: Locator = Locator(By.XPATH, "//*[@data-testid='question']//input")
    answer_1_input: Locator = Locator(By.XPATH, "//*[@data-testid='answer-1']//input")
    answer_2_input: Locator = Locator(By.XPATH, "//*[@data-testid='answer-2']//input")
    trivia_points_input: Locator = Locator(By.XPATH, "//*[@data-testid='points']//input")
    trivia_correct_answer_1: Locator = Locator(By.XPATH, "//*[@data-testid='proper-answer-1']")
    trivia_correct_answer_2: Locator = Locator(By.XPATH, "//*[@data-testid='proper-answer-2']")
    prediction_answer_1_points: Locator = Locator(By.XPATH, "//*[@data-testid='points-answer-1']//input")
    prediction_answer_2_points: Locator = Locator(By.XPATH, "//*[@data-testid='points-answer-2']//input")
    save_button: Locator = Locator(By.XPATH, "//*[@data-testid='save-question']")
    first_draft_card: Locator = Locator(By.XPATH, "//*[@data-testid='Drafts-1']//span")
    question_form: Locator = Locator(By.XPATH, "//*[@data-testid='question-form']")