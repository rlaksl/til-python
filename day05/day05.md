# Day 05 - 리스트, 튜플, 딕셔너리

## 오늘 배운 내용
리스트(List), 튜플(Tuple), 딕셔너리(Dictionary)와 불변성 차이

## 1. 문자열 메서드 (String Methods)
- 문자열에 내장된 다양한 기능들
- 메서드는 `.`(점)을 찍고 사용

### 주요 메서드
- `upper()`: 모든 문자를 대문자로 변환
- `capitalize()`: 첫 글자만 대문자로 변환
- `startswith()`: 특정 문자로 시작하는지 확인 (True/False 반환)

## 2. 리스트 (List)
- 여러 값을 순서대로 저장하는 컬렉션
- 대괄호 `[]`로 생성
- 변경 가능(mutable) - 값 추가, 삭제, 수정 가능

### 주요 메서드
- `append(값)`: 리스트 끝에 값 추가
- `remove(값)`: 특정 값 삭제
- 인덱스로 접근: `리스트[0]`, `리스트[1]`

## 3. 튜플 (Tuple)
- 리스트와 비슷하지만 변경 불가능(immutable)
- 소괄호 `()`로 생성
- 값 추가, 삭제, 수정 불가능
- 읽기만 가능 (인덱스로 접근)

```python
days = ("Mon", "Thu", "Wed")
print(days[0])  # Mon
# days.append("Fri")  # 오류 발생!
```

## 4. 딕셔너리 (Dictionary)
- Key-Value 쌍으로 데이터 저장
- 중괄호 `{}`로 생성
- 변경 가능(mutable) - 값 추가, 삭제, 수정 가능
- Key로 값에 접근

### 주요 메서드
- `get(key)`: Key로 값 가져오기
- `pop(key)`: Key-Value 쌍 삭제
- `딕셔너리[key] = 값`: 새로운 Key-Value 쌍 추가 또는 수정

## 불변성(Mutability) 비교

| 자료형 | 변경 가능 여부 | 특징 |
|--------|---------------|------|
| **리스트(List)** | 변경 가능 | 값 추가, 삭제, 수정 가능 |
| **튜플(Tuple)** | 변경 불가능 | 생성 후 수정 불가, 읽기만 가능 |
| **딕셔너리(Dictionary)** | 변경 가능 | Key-Value 추가, 삭제, 수정 가능 |

### 왜 튜플을 사용할까?
- 데이터 보호: 실수로 값을 변경하는 것 방지
- 성능: 튜플이 리스트보다 처리 속도가 빠름
- 딕셔너리의 Key로 사용 가능 (리스트는 불가능)

## Python vs Java 비교

| 구분 | Python | Java |
|------|--------|------|
| **리스트** | `list = [1, 2, 3]` | `ArrayList<Integer> list = new ArrayList<>()` |
| **튜플** | `tuple = (1, 2, 3)` | 기본 제공 없음 (불변 리스트로 구현) |
| **딕셔너리** | `dict = {'key': 'value'}` | `HashMap<String, String> map = new HashMap<>()` |
| **값 추가** | `list.append(4)` | `list.add(4)` |
| **값 삭제** | `list.remove(값)` | `list.remove(인덱스)` 또는 `list.remove(값)` |
| **접근** | `list[0]`, `dict['key']` | `list.get(0)`, `map.get("key")` |

### Java 예시 비교
```java
// List (ArrayList)
ArrayList<String> days = new ArrayList<>();
days.add("Mon");
days.add("Tue");
days.remove("Mon");

// Dictionary (HashMap)
HashMap<String, Object> player = new HashMap<>();
player.put("name", "hwanhui");
player.put("age", 12);
player.remove("age");
System.out.println(player.get("name"));  // hwanhui
```

## 핵심 정리
1. **메서드**: 문자열이나 리스트 등에 내장된 기능 (`.`으로 호출)
2. **리스트**: 변경 가능, 순서 있음, `[]`로 생성
3. **튜플**: 변경 불가능, 순서 있음, `()`로 생성
4. **딕셔너리**: 변경 가능, Key-Value 쌍, `{}`로 생성
5. **불변성이 핵심 차이점**: 튜플은 읽기만 가능, 리스트와 딕셔너리는 수정 가능