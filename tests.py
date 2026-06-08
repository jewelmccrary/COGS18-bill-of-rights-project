"""Unit tests to test functionality of project."""

import unittest
from module import StudyingBillOfRights

class TestStudyingBillOfRights(unittest.TestCase):
    
    def setUp(self):
        self.study = StudyingBillOfRights()

    def test_amend_description_correct(self):
        response = self.study.amend_description(
            1,
            "speech religion press assembly petition"
        )
        self.assertEqual(self.study.score, 1)
        self.assertIn("Score: 1", response)
        
    def test_amend_description_case_insensitive(self):
        self.study.amend_description(
            1,
            "SPEECH RELIGION PRESS ASSEMBLY PETITION"
        )
        self.assertEqual(self.study.score, 1)

    def test_amend_description_missing_concepts(self):
        response = self.study.amend_description(
            1,
            "speech religion"
        )
        self.assertEqual(self.study.score, 0)
        self.assertIn("press", response)
        self.assertIn("assembly", response)
        self.assertIn("petition", response)
        
    def test_amend_date_string_input(self):
        self.study.amend_date("1791")
        self.assertEqual(self.study.score, 1)

    def test_score_accumulates(self):
        self.study.amend_date(1791)
        self.study.amend_description(
            2,
            "bear arms"
        )
        self.assertEqual(self.study.score, 2)

    def test_partial_phrase_not_accepted(self):
        response = self.study.amend_description(
            5,
            "right to remain silent"
        )
        self.assertEqual(self.study.score, 0)
        self.assertIn("no self-incrimination", response)

    



                 
    