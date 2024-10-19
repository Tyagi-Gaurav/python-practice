import time
from functools import reduce
from typing import Any, Callable, List, Union

import mt5_client


class Given:
    def __init__(self, **kwargs: Any):
        self.__dict__.update(kwargs)

    def add(self, key, value):
        self.__dict__.__setitem__(key, value)


CallableType = Union[
    Callable[[Given], Any],
    Callable[[Given, Any], Any],
    Callable[[Given, Any, Any], Any],
    Callable[[Given, Any, Any, Any], Any],
]


class When:
    def __init__(self, name: str, eval_function: Callable[[Given], bool]):
        self.__eval_function = eval_function
        self.name = name

    def evaluate(self, given: Given):
        result = self.__eval_function(given)
        print(f"Condition: {self.name}, result: {result}")
        return result


class Then:
    def __init__(self, name: str, eval_function: CallableType, **kwargs: Any):
        self.__eval_function = eval_function
        self.name = name
        self.kwargs = kwargs

    def evaluate(self, given: Given):
        return self.__eval_function(given, **self.kwargs)


class Rule:
    def __init__(self, when: list[When], then: list[Then]):
        self.then = then
        self.when = when

    def evaluate(self, given: Given):
        def evaluate_conditions(conditions: List[When], fact_param: Given) -> Given:
            results = map(lambda condition: condition.evaluate(fact_param), conditions)
            all_conditions = reduce(lambda x, y: x and y, results)

            return all_conditions

        all_conditions_satisfied = evaluate_conditions(self.when, given)
        if all_conditions_satisfied:
            for action in self.then:
                print(action.name)
                action.evaluate(given)


class Task:
    def __init__(self, name: str, eval_function: CallableType, **kwargs: Any):
        self.__eval_function = eval_function
        self.name = name
        self.kwargs = kwargs

    def evaluate(self, given):
        self.__eval_function(given, **self.kwargs)


class Strategy:
    def __init__(self, name: str, tasks: List[Task], rules: List[Rule]):
        self.tasks = tasks
        self.name = name
        self.rules = rules

    def apply(self, given: Given):
        print(f"Applying rule : {self.name}")
        print("Performing tasks..")
        for task in self.tasks:
            print(task.name)
            task.evaluate(given)

        print("Evaluating Rules..")
        for rule in self.rules:
            rule.evaluate(given)


do_nothing = Then("Do Nothing", lambda _: _)
