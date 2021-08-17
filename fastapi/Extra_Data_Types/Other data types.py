'''
UUID:
많은 데이터베이스 및 시스템에서 ID로 일반적으로 사용되는 표준 "Universally Unique Identifier"입니다.
요청 및 응답에서 str로 표시됩니다.

datetime.datetime:
파이썬 datetime.datetime
요청 및 응답에서 2008-09-15T15:53:00+05:00과 같이 ISO 8601 형식의 str로 표시됩니다.

datetime.date:
파이썬 datetime.date.
요청 및 응답에서 2008-09-15와 같이 ISO 8601 형식의 str로 표시됩니다.

datetime.time:
파이썬 datetime.time.
요청 및 응답에서 14:23:55.003과 같이 ISO 8601 형식의 str로 표시됩니다.

datetime.timedelta:
파이썬 datetime.timedelta.
요청 및 응답에서 총 초 단위로 표시됩니다.
Pydantic은 "ISO 8601 시간 차이 인코딩"으로 표현할 수도 있습니다.

frozenset:
요청 및 응답에서 집합과 동일하게 처리됩니다.
요청에서 목록을 읽고 중복을 제거하고 집합으로 변환합니다.
응답에서 집합이 목록으로 변환됩니다.
생성된 스키마는 설정 값이 고유하도록 지정합니다(JSON 스키마의 uniqueItems 사용).

bytes:
표준 파이썬 바이트.
요청 및 응답에서 str로 처리됩니다.
생성된 스키마는 바이너리 "형식"이 있는 str임을 지정합니다.

Decimal:
표준 파이썬 십진수.
요청 및 응답에서 float와 동일하게 처리됩니다.
여기에서 모든 유효한 pydantic 데이터 유형을 확인할 수 있습니다. Pydantic 데이터 유형.
'''