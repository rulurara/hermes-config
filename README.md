# Hermes Agent Configuration

노트북 환경에 최적화된 Hermes Agent 설정 저장소입니다.

## 설정 파일 구조

```
config.yaml          - Hermes Agent 메인 설정
.env.example         - API 키 환경변수 템플릿 (실제 .env는 커밋하지 않음)
.gitignore           - .env, 세션, 로그 등 제외
.gitattributes       - 줄 끝 정규화
README.md            - 이 파일
```

## 주요 설정 (노트북 환경 맞춤)

| 항목 | 값 | 이유 |
|------|-----|------|
| `agent.max_turns` | 180 | 긴 작업 대응 |
| `session_reset.mode` | off | 노트북을 껐다 켜도 세션 유지 |
| `memory.memory_char_limit` | 4000 | 더 많은 맥락 기억 |
| `compression.threshold` | 0.7 | 압축 늦춰서 맥락 유지 |
| `approvals.mode` | smart | 안전한 명령 자동 승인 |
| `display.show_cost` | true | 비용 모니터링 |
| `display.language` | ko | 한국어 인터페이스 |
| `fallback_model` | claude-sonnet-4 | 429/503 시 자동 전환 |

## 다른 PC에서 사용하기

### 1. Hermes Agent 설치
```powershell
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

### 2. 설정 파일 복원
```powershell
# 이 저장소 클론
git clone https://github.com/YOUR_USERNAME/hermes-config.git

# 설정 파일을 Hermes 홈 디렉토리로 복사
$hermesHome = "$env:LOCALAPPDATA\hermes"
Copy-Item ".\hermes-config\config.yaml" -Destination "$hermesHome\config.yaml" -Force
# 또는 CLI 사용
hermes config edit  # 수동으로 내용 복사
```

### 3. API 키 설정
```powershell
# .env.example을 참고해서 .env 파일 생성
Copy-Item ".\hermes-config\.env.example" -Destination "$hermesHome\.env"
# .env 파일을 편집해서 실제 API 키 입력
notepad "$hermesHome\.env"
```

## 주의사항

- `.env` 파일은 **절대 커밋하지 마세요** — API 키가 포함되어 있습니다
- 스킬 업데이트는 Hermes 자동 업데이트(`hermes skills update`)를 이용하세요
- 설정 변경 후 `hermes`를 재시작하면 적용됩니다
