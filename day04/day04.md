# Day 04 - 논리 연산자, while, input

## 오늘 배운 내용
`and`, `or` 논리 연산자, `while` 반복문, `input()` 함수, `random` 모듈

## 1. input() 함수
- 사용자로부터 입력값을 받는 함수
- 오직 하나의 argument만 받음 (입력 안내 메시지)
- 입력받은 값은 항상 문자열(String) 타입

```python
age = input("How old are you?")  # 문자열로 저장됨
age = int(input("How old are you?"))  # 숫자로 변환
```

### 타입 변환
- `int()`: 문자열을 정수로 변환
- `type()`: 변수의 타입 확인

```python
age = int(input("How old are you?"))
print(type(age))  # <class 'int'>
```

## 2. 논리 연산자 (and, or)

### and 연산자
- 모든 조건이 True일 때만 True
- 하나라도 False면 결과는 False

```python
True and True # True
False and True # False
True and False # False
False and False # False
```

### or 연산자
- 하나 이상이 True면 True
- 모두 False일 때만 False

```python
True or True    # True
True or False   # True
False or True   # True
False or False  # False
```

## 3. while 반복문
- 조건이 True인 동안 계속 반복 실행
- 조건이 False가 되면 반복 종료
- 조건이 항상 True면 영원히 반복

### while 반복문 제어
- 플래그 변수를 사용해 반복 제어 가능

```python
playing = True
while playing:
    # 게임 로직
    if 승리조건:
        playing = False  # 반복 종료
```

## 4. random 모듈
- 난수(랜덤한 숫자)를 생성하는 모듈
- `randint(a, b)`: a 이상 b 이하의 랜덤 정수 생성

```python
from random import randint

pc_choice = randint(1, 50)  # 1~50 사이의 랜덤 숫자
```

## Python vs Java 비교

| 구분 | Python | Java |
|------|--------|------|
| **사용자 입력** | `input("메시지")` | `Scanner` 클래스 사용 |
| **타입 변환** | `int(값)`, `str(값)` | `Integer.parseInt()` |
| **논리 연산자** | `and`, `or`, `not` | `&&`, `||`, `!` |
| **while 문** | `while 조건:`<br>들여쓰기 | `while (조건) {}`<br>중괄호 |
| **랜덤 숫자** | `from random import randint` | `import java.util.Random` |

### Java 예시 비교
```java
// Java - 사용자 입력
Scanner scanner = new Scanner(System.in);
System.out.print("How old are you?");
int age = scanner.nextInt();

// Java - 논리 연산자
if (age >= 18 && age <= 35) {
    System.out.println("You drink beer");
}

// Java - while 문
int distance = 0;
while (distance < 20) {
    System.out.println("I'm running: " + distance + " km");
    distance++;
}
```

## 핵심 정리
1. `input()`은 항상 문자열 반환 → 숫자 계산 시 `int()` 변환 필수
2. `and`는 모두 True, `or`은 하나만 True여도 됨
3. `while` 반복문은 조건이 True인 동안 계속 실행
4. 플래그 변수(`playing = True/False`)로 반복 제어 가능
5. `randint(a, b)`로 a 이상 b 이하의 랜덤 정수 생성