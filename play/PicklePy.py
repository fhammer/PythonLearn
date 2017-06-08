#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块
json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，
    当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
"""

import pickle
import io
import json


class PickleFunc(object):
    def dump_bytes_file(self):
        d = dict(name='Bob', age=20, score=88)
        byte_file = io.BytesIO()
        byte_file.write(pickle.dumps(d))
        print(byte_file.getvalue())

    def dump_file(self):
        with open('./dumps.log', 'wb') as file:
            d = dict(name='Bob', age=20, score=88)
            pickle.dump(d, file)

    def un_dump_file(self):
        with open('./dumps.log', 'rb') as file:
            d = pickle.load(file)
            print(d)


class Student(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def obj2json(std):
        return {
            'name': std.name,
            'age': std.age,
            'gender': std.gender
        }

    def dict2student(d):
        return Student(d['name'], d['age'], d['gender'])


class JsonFunc(object):
    def to_json(self):
        d = dict(name='Bob', age=20, score=88)
        return json.dumps(d)

    def load_json(self):
        print(json.loads(self.to_json()))

    def obj_json(self):
        stu = Student('hammer', 18, 'm')
        print(json.dumps(stu, default=Student.obj2json))
        # 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
        print(json.dumps(stu, default=lambda obj: obj.__dict__))

    def json_obj(self):
        json_str = '{"age": 20, "gender": "m", "name": "Bob"}'
        print(json.loads(json_str, object_hook=Student.dict2student))


if __name__ == "__main__":
    pickle_fun = PickleFunc()
    pickle_fun.dump_file()
    pickle_fun.un_dump_file()

    json_func = JsonFunc()
    json_func.load_json()
    json_func.obj_json()
    json_func.json_obj()
