import unittest
from src.ontrack import get_task_inbox

class TestOnTrack(unittest.TestCase):
    def test_get_task_inbox(self):
        student_id = "s1234567"
        tasks = get_task_inbox(student_id)
        self.assertIsInstance(tasks, list)
        self.assertGreater(len(tasks), 0)
        for task in tasks:
            self.assertIn("task_id", task)
            self.assertIn("title", task)
            self.assertIn("submission_date", task)
            self.assertIn("status", task)

if __name__ == "__main__":
    unittest.main()
