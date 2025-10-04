# Day 06 - for 반복문, requests 모듈, HTTP 상태 코드

## 오늘 배운 내용
`for` 반복문, URL Formatting, `requests` 모듈을 이용한 HTTP 요청

## 1. for 반복문
- 시퀀스(리스트, 튜플, 문자열 등)의 각 요소를 순회하며 반복 실행
- `while`과 달리 반복 횟수가 명확할 때 사용
- 자동으로 다음 요소로 이동

```python
websites = ("google.com", "airbnb.com", "twitter.com")

for website in websites:
    print(website)
```

### for vs while 비교
- **for**: 컬렉션의 각 요소를 순회할 때 (반복 횟수 명확)
- **while**: 조건이 True인 동안 계속 실행 (반복 횟수 불명확)

## 2. URL Formatting (URL 포맷팅)
- 웹사이트 주소를 올바른 형식으로 만들기
- `https://`가 없는 URL에 자동으로 추가하여 통일된 형식 유지

### 왜 URL Formatting이 필요한가?
- **통일성**: 모든 URL을 같은 형식으로 관리
- **안전성**: `https://` 사용으로 보안 연결 보장
- **정확성**: 요청이 제대로 전송되도록 보장

## 3. 문자열 메서드 활용
### startswith()
- 문자열이 특정 접두사로 시작하는지 확인
- `True` 또는 `False` 반환

### not 연산자
- 조건을 반대로 만듦
- `not True` → `False`
- `not False` → `True`

### f-string으로 URL 조합
- 변수와 문자열을 결합하여 새로운 URL 생성

## 4. requests 모듈
- HTTP 요청을 보내는 외부 라이브러리
- 웹사이트 상태 확인, 데이터 가져오기 등에 사용
- 설치: `pip install requests`

### get() 함수
- 지정한 URL로 GET 요청 보내기
- 응답 객체(response) 반환

### HTTP 상태 코드
- **200**: 성공 (OK)
- **404**: 페이지를 찾을 수 없음 (Not Found)
- **500**: 서버 오류 (Internal Server Error)

## 5. 딕셔너리에 데이터 저장
- for 반복문으로 여러 웹사이트 확인
- 결과를 딕셔너리에 저장하여 관리

```python
results = {}

for website in websites:
    response = get(website)
    if response.status_code == 200:
        results[website] = "OK"
    else:
        results[website] = "FAILED"

print(results)
# {'https://google.com': 'OK', ...}
```

## Python vs Java 비교

| 구분 | Python | Java |
|------|--------|------|
| **for 반복문** | `for item in collection:`<br>들여쓰기 | `for (String item : collection) {}`<br>중괄호 |
| **향상된 for** | 기본 제공 | `for-each` 문법 |
| **HTTP 요청** | `requests.get(url)` | `HttpURLConnection` 또는<br>`HttpClient` (Java 11+) |
| **not 연산자** | `not condition` | `!condition` |
| **문자열 메서드** | `str.startswith()` | `str.startsWith()` (camelCase) |

### Java 예시 비교
```java
// Java - for-each 반복문
String[] websites = {"google.com", "airbnb.com", "twitter.com"};

for (String website : websites) {
    System.out.println(website);
}

// Java - HTTP 요청 (Java 11+)
HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://google.com"))
    .build();

HttpResponse<String> response = client.send(request, 
    HttpResponse.BodyHandlers.ofString());
System.out.println(response.statusCode());  // 200
```
## 핵심 정리
1. **for 반복문**: 시퀀스의 각 요소를 자동으로 순회
2. **URL Formatting**: f-string과 조건문으로 URL을 올바른 형식으로 변환
3. **not 연산자**: 조건을 반대로 만듦 (`not True` → `False`)
4. **requests 모듈**: HTTP 요청을 쉽게 보낼 수 있는 라이브러리
5. **status_code**: HTTP 응답 상태 확인 (200 = 성공)
6. **딕셔너리 활용**: 여러 결과를 Key-Value로 저장하여 관리