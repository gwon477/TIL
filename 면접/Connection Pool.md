## 데이터베이스 연결 풀(Connection Pool)을 사용하지 않으면 어떤 자원 문제가 발생할 수 있으며, 연결 풀을 사용함으로써 얻을 수 있는 장점은 무엇인가요? 추가로, 커넥션 풀 관련 설정을 만져봤다면 알려주세요

<br>

답변 키워드
---
- DB Connection Pool에 대해 알고 있는가?
- Connection Pool 을 사용하지 않을 경우 발생하는 문제점?
- 사용 경험

<br>

DB Connection Pool ?
---
어플리케이션 로딩 시점에 Connection 객체를 미리 생성해두고 DB 접근이 필요할 때마다 이를 사용함으로써 성능을 유지하는 것.

<br>

사용하지 않을 경우 발생할 수 있는 문제점
---
JDBC API를 사용해 DB에 접근하기 위해서 Connection 객체를 생성하게 되는데, 접근 마다 아래 절차를 거쳐서 생성하는 것은 굉장히 비효율적이다.


Connection 생성 절차

🅐 애플리케이션에서 DB 드라이버를 통해 커넥션을 조회한다.   
🅑 DB 드라이버는 DB와 TCP/IP 커넥션을 연결한다.(3Ways-Handshaking과 같은 네트워크 연결 동작 발생)   
🅒 DB 드라이버는 TCP/IP 커넥션이 연결되면 아이디와 패스워드, 기타 부가 정보를 DB에 전달한다.   
🅓 DB는 아이디, 패스워드를 통해 내부 인증을 거친 후 내부에 DB를 생성한다.   
🅔 DB는 커넥션 생성이 완료되었다는 응답을 보낸다.    
🅕 DB 드라이버는 커넥션 객체를 생성해서 클라이언트에 반환한다.   

(Connection Pool이 등장하게 된 배경)

<br>

Connection Pool 사용 경험?
---

디케이테크인 자사몰 구축 프로젝트에서 트래픽이 높지 않은 상황임에도 발생한 Connection Pool 부족 문제를 해결한 사례가 있습니다. 클라이언트 접속 시 DB Connection이 반납되지 않는 현상을 발견했고, 이를 해결하기 위해 Spring Boot 애플리케이션의 기본 설정인 OSIV(Open Session in View)를 비활성화했습니다.

문제 원인:

기본적으로 JPA의 open-in-view 설정이 활성화되어 있으면 API 요청부터 응답까지 영속성 컨텍스트가 유지됩니다. 이로 인해 DB Connection이 계속 연결된 상태로 유지되었고, Connection Pool 자원이 고갈되는 문제가 발생했습니다.

문제 해결:   

이를 해결하기 위해 spring.jpa.open-in-view=false로 설정하여 OSIV를 비활성화했습니다. 이 설정을 통해 JPA EntityManager가 요청-응답 주기와 별개로 독립적인 트랜잭션 단위에서 작동하도록 구성하였습니다.

결과:

설정 변경으로 DB Connection의 반납이 원활해졌고 Connection Pool의 효율성이 크게 향상되었습니다. 이를 통해 애플리케이션의 안정성과 성능을 개선할 수 있었습니다.
