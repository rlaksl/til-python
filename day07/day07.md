# Day 07 - OOP(객체지향프로그래밍), 클래스, 상속

## 오늘 배운 내용
OOP(Object Oriented Programming), 클래스(Class), 생성자(`__init__`), 메서드(Methods), 상속(Inheritance), 캡슐화(Encapsulation)

## 1. OOP(객체지향프로그래밍)란?
- **데이터와 그 데이터를 다루는 함수를 하나로 묶어서 관리하는 프로그래밍 방식**
- 딕셔너리와 함수를 따로 관리하는 대신, 클래스로 하나로 묶음
- 코드 재사용성과 유지보수성이 좋아짐

### OOP 이전 방식 (딕셔너리 + 함수)
```python
def create_player(name, xp, team):
  return {
    "name": name,
    "XP": xp,
    "team": team,
  }

def introduce_player(player):
  name = player["name"]
  team = player["team"]
  print(f"Hello! My name is {name} and I play for {team}")

aksl = create_player("rlaksl", 1500, "Team X")
introduce_player(aksl)  # 함수를 따로 호출해야 함
```

### OOP 방식 (클래스 사용)
```python
class Player:
  def __init__(self, name, xp, team):
    self.name = name
    self.xp = xp
    self.team = team
  
  def introduce(self):
    print(f"Hello! My name is {self.name} and I play for {self.team}")

aksl = Player("rlaksl", 1500, "Team X")
aksl.introduce()  # 데이터와 기능이 한 곳에
```

## 2. 클래스 vs 딕셔너리

### 공통점
- 둘 다 여러 데이터를 하나로 묶어서 관리

### 차이점

| 구분 | 딕셔너리 | 클래스 |
|------|---------|--------|
| **접근 방식** | 대괄호 `[]` | 점 `.` |
| **메서드** | 함수 따로 작성 필요 | 클래스 안에 포함 |
| **캡슐화** | 데이터만 저장 | 데이터 + 기능 함께 관리 |

## 3. 클래스(Class)
- **객체를 만들기 위한 설계도(blueprint)**
- `class` 키워드로 정의
- 클래스 이름은 대문자로 시작 (PascalCase)
- 클래스는 우리가 캡슐화하고 싶은 것을 캡슐화할 수 있도록 도와줌

## 4. 생성자 (`__init__`)
- 클래스로 객체를 생성할 때 자동으로 실행되는 특별한 메서드
- `self`: 생성된 객체 자신을 가리키는 파라미터 (첫 번째 파라미터는 항상 `self`)
- `self.변수명`으로 객체의 속성(attribute) 정의

### self란?
- 생성된 객체 자신을 참조
- 메서드 정의 시 첫 번째 파라미터로 작성
- 호출 시에는 자동으로 전달되므로 명시하지 않음

## 5. 메서드(Methods)
- **클래스 안에 있는 함수를 메서드라고 부름**
- 첫 번째 파라미터는 항상 `self`
- 객체의 속성에 접근하거나 수정 가능

## 6. `__str__` 메서드
- 객체를 `print()`할 때 어떻게 출력할지 정의
- 문자열을 반환해야 함

## 7. 상속(Inheritance)
- **기존 클래스의 속성과 메서드를 물려받아 새로운 클래스를 만드는 것**
- 코드 중복을 줄이고 확장성 향상
- `super().__init__()`으로 부모 클래스의 생성자 호출

```python
# 부모 클래스 (Parent Class)
class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
  
  def sleep(self):
    print("zzzZzZZ...")

# 자식 클래스 1 (Child Class)
class Puppy(Dog):
  def __init__(self, name, breed):
    super().__init__(name, breed, 0.1)  # 부모 생성자 호출
    self.spoiled = True  # 자식만의 속성 추가
  
  def woof_woof(self):  # 자식만의 메서드
    print("멍멍")

# 자식 클래스 2
class GuardDog(Dog):
  def __init__(self, name, breed):
    super().__init__(name, breed, 5)
    self.aggressive = True
  
  def rrrr(self):  # 자식만의 메서드
    print("으르렁")

# 사용
ruffus = Puppy("Ruffus", "Beagle")
ruffus.sleep()      # 부모 메서드 사용 가능
ruffus.woof_woof()  # 자식 메서드 사용

bibi = GuardDog("Bibi", "Dalmatian")
bibi.sleep()        # 부모 메서드 사용 가능
bibi.rrrr()         # 자식 메서드 사용
```

### super()란?
- 부모 클래스를 참조하는 함수
- `super().__init__()`으로 부모 생성자를 호출하여 부모의 속성 초기화

## 8. 점(.) 표기법의 의미

```python
player.name         # "player의 name 속성"
player.introduce()  # "player의 introduce 메서드"
```

- **점(.)은 "~의" 라는 의미**
- `ruffus.name` = "ruffus의 name"
- `ruffus.sleep()` = "ruffus의 sleep 행동"

## 9. 캡슐화(Encapsulation)
- **관련된 데이터와 기능을 하나로 묶음**
- 플레이어의 정보와 플레이어가 할 수 있는 행동을 한 클래스에 모두 담음

## Python vs Java 비교

| 구분 | Python | Java |
|------|--------|------|
| **클래스 정의** | `class Puppy:` | `public class Puppy {}` |
| **생성자** | `def __init__(self):