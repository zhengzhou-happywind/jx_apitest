a = {"a": 123,
     "b": 1,
     "c": 23
     }
b = {
    "c": "sdfa",
    "a": "sdfa",
    "b": "sdfa",
}

from common.report import Result

result = Result("try")
result.one_fence(1, a, b)
print(result.fences)
