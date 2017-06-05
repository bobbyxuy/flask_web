import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):  # 尝试创建一个测试环境，
        self.app = create_app('testing')  # 使用测试配置创建程序
        self.app_context = self.app.app_context()  # 激活上下文，确保能在测试中使用current_app
        self.app_context.push()
        db.create_all()  # 创建一个全新的数据库，以备不时之需

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
