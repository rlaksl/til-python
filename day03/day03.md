# Day 03 - 기본값, return, f-string, 조건문

## 오늘 배운 내용
기본 매개변수(Default Parameter), return, f-string(formatted string), if-elif-else 조건문

## 1. 기본 매개변수 (Default Parameter)
- 함수 정의 시 파라미터에 기본값을 설정할 수 있음
- 아규먼트를 전달하지 않으면 기본값이 사용됨

## 2. return
- 함수가 값을 반환(return)할 수 있게 해줌
- `print()`는 화면에 출력만 하지만, `return`은 값을 돌려줘서 다른 곳에서 사용 가능
- return한 값을 변수에 저장하거나 다른 함수의 아규먼트로 전달할 수 있음

### return의 재사용성
- return한 값을 여러 함수에 연결해서 사용 가능

## 3. f-string (Formatted String)
- 문자열 안에 변수나 표현식을 쉽게 삽입할 수 있는 방법
- 문자열 앞에 `f`를 붙이고 중괄호 `{}`로 변수를 감쌈

```python
my_name = "hwanhui"

print(f"Hello I'm {my_name}")
```

## 4. 조건문 (if-elif-else)
- 조건에 따라 다른 코드를 실행
- 들여쓰기로 코드 블록 구분

### if
- 조건이 `True`일 때만 코드 실행

### else
- `if` 조건이 `False`일 때 실행

### elif (else if)
- 여러 조건을 순차적으로 검사
- `if` 조건이 `False`일 때 다음 조건 확인
- `else`는 모든 조건이 `False`일 때 실행

## Python vs Java 비교

| 구분 | Python | Java |
|------|--------|------|
| **기본값** | `def func(a=0):` | 메서드 오버로딩으로 구현 |
| **return** | `return value` | `return value;` (세미콜론) |
| **문자열 포맷팅** | `f"Hello {name}"` | `String.format()` 또는 `"Hello " + name` |
| **조건문** | `if condition:`<br>들여쓰기 | `if (condition) {`<br>중괄호 `{}` |
| **비교 연산자** | `==`, `!=`, `>`, `<` | `==`, `!=`, `>`, `<` (동일) |

### Java에서의 조건문 예시
```java
int winner = 6;

if (winner > 10) {
    System.out.println("Winner is greater than 10");
} else if (winner < 10) {
    System.out.println("Winner is less than 10");
} else {
    System.out.println("Winner is 10");
}
```
## 핵심 정리
- **기본 매개변수**: 함수 호출 시 아규먼트를 생략할 수 있게 해줌
- **return**: 함수의 결과값을 반환하여 재사용 가능하게 만듦
- **f-string**: 변수를 문자열에 쉽게 삽입 (`f"..."`)
- **if-elif-else**: 조건에 따라 다른 코드 실행, 들여쓰기 필수