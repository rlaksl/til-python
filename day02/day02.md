# Day 02 - 함수(Function)

## 오늘 배운 내용
함수(Function) 정의, 파라미터(Parameter), 아규먼트(Argument), 함수의 재사용

## 1. 함수란?
- **재사용 가능한 코드 블록**
- 한 번 정의하면 몇 번이고 호출하여 사용 가능
- 코드 중복을 줄이고 유지보수를 쉽게 만듦

## 2. 함수 정의 (def)
- `def` 키워드로 함수 정의
- 함수 이름 뒤에 `()` 추가
- 콜론(`:`) 후 들여쓰기로 함수 본문 작성

## 3. 파라미터 (Parameter)
- 함수 정의 시 괄호 안에 선언하는 변수
- 함수 안으로 데이터를 전달받아 함수의 결과를 다르게 만들 수 있음
- 플레이스홀더(Placeholder) 역할 - 실제 값이 들어올 자리를 미리 지정

```python
def say_hello(user_name, user_age):  # user_name, user_age가 파라미터
    print("hello", user_name)
    print("you are", user_age, "years old")
```

## 4. 아규먼트 (Argument)
- 함수 호출 시 전달하는 실제 값
- 파라미터에 대응되는 구체적인 데이터

```python
say_hello("hwanhui", 8)  # "hwanhui", 8이 아규먼트
```

## 5. 함수의 재사용성
- 같은 함수를 다른 값으로 여러 번 호출 가능

```python
def tax_calculator(money):
    print(money * 0.35)

tax_calculator(250000) # 87500.0
tax_calculator(25000) # 8750.0
```

## Python vs Java 비교

| 구분 | Python | Java |
|------|--------|------|
| **함수 정의** | `def function_name():` | `public static void functionName() {}` |
| **들여쓰기** | 필수 (코드 블록 구분) | 중괄호 `{}` 사용 |
| **파라미터 선언** | 타입 불필요<br>`def func(name, age):` | 타입 필수<br>`void func(String name, int age)` |
| **네이밍** | snake_case<br>`say_hello` | camelCase<br>`sayHello` |

### 용어 정리
- **파라미터(Parameter)**: 함수 정의에서 사용하는 변수 (형식 매개변수)
- **아규먼트(Argument)**: 함수 호출 시 전달하는 실제 값 (실 매개변수)
- **플레이스홀더(Placeholder)**: 나중에 값이 들어올 자리를 미리 확보해둔 것

## 실습 코드
```python

# 파라미터 없는 함수
def say_hello():
    print("hello how r u?")
  
say_hello()

# 파라미터 있는 함수
def say_hello(user_name, user_age):
    print("hello", user_name)
    print("you are", user_age, "years old")

say_hello("hwanhui", 8)

# 파라미터 없는 세금 계산기
def tax_calculator():
    print(1500000000 * 0.35)

tax_calculator()

# 파라미터 있는 세금 계산기 (재사용 가능)
def tax_calculator(money):
    print(money * 0.35)

tax_calculator(250000)
tax_calculator(25000)
tax_calculator(2500)
```