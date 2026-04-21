from selenium.webdriver import Chrome

from pages.event_moderation.locators_collection import LocatorsCollection
from pages.base.base import BasePage

import allure


class EventModerationPage(BasePage):
    def __init__(self, driver: Chrome) -> None:
        super().__init__(driver)

        self.__locators = LocatorsCollection()

    @allure.step('Click on the "Create new" button')
    def click_on_create_new_button(self):
        self._wait_until_not_visible(self.__locators.create_new_button).click()

    @allure.step('Click on the "Poll" button')
    def click_on_poll_button(self):
        self._wait_until_not_visible(self.__locators.poll_button).click()

    @allure.step('Click on the "Trivia" button')
    def click_on_trivia_button(self):
        self._wait_until_not_visible(self.__locators.trivia_button).click()

    @allure.step('Click on the "Prediction" button')
    def click_on_prediction_button(self):
        self._wait_until_not_visible(self.__locators.prediction_button).click()

    @allure.step('Entering the question: {question}')
    def enter_question(self, question: str):
        question_input = self._wait_until_not_visible(self.__locators.question_input)
        question_input.send_keys(f"{question}")

    @allure.step('Entering the trivia points: {points}')
    def enter_trivia_points(self, points: int):
        trivia_points_input = self._wait_until_not_visible(self.__locators.trivia_points_input)
        trivia_points_input.send_keys(points)

    @allure.step('Entering the 1st answer: {answer}')
    def enter_answer_1(self, answer: str):
        answer_1_input = self._wait_until_not_visible(self.__locators.answer_1_input)
        answer_1_input.send_keys(f"{answer}")

    @allure.step('Entering the 2nd answer: {answer}')
    def enter_answer_2(self, answer: str):
        answer_2_input = self._wait_until_not_visible(self.__locators.answer_2_input)
        answer_2_input.send_keys(f"{answer}")

    @allure.step('Setting the 1st answer as a correct')
    def set_trivia_correct_answer_1(self):
        correct_answer_button = self._wait_until_not_visible(self.__locators.trivia_correct_answer_1)
        correct_answer_button.click()

    @allure.step('Setting the 2nd answer as a correct')
    def set_trivia_correct_answer_2(self):
        correct_answer_button = self._wait_until_not_visible(self.__locators.trivia_correct_answer_2)
        correct_answer_button.click()

    @allure.step('Setting the 1st answer points: {points}')
    def enter_prediction_answer_1_points(self, points: int):
        answer_points = self._wait_until_not_visible(self.__locators.prediction_answer_1_points)
        answer_points.send_keys(points)

    @allure.step('Setting the 2nd answer points: {points}')
    def enter_prediction_answer_2_points(self, points: int):
        answer_points = self._wait_until_not_visible(self.__locators.prediction_answer_2_points)
        answer_points.send_keys(points)

    @allure.step('Click on the "Save" button')
    def click_on_save_button(self):
        self._wait_until_not_visible(self.__locators.save_button).click()

    @allure.step('Waiting until the question form disappears')
    def wait_until_question_form_disappeared(self):
        self._wait_until_visible(self.__locators.question_form)

    @allure.step('Looking for our question at the 1st position in the Drafts column')
    def first_draft_card_question(self):
        return self._wait_until_not_visible(self.__locators.first_draft_card).text