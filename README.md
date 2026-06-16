# Hermes Agent Configuration

여러 컴퓨터에서 Hermes Agent 설정을 공유하기 위한 저장소입니다.

## 설정 파일 구조

```
config.yaml          - Hermes Agent 메인 설정
.env.example         - API 키 환경변수 템플릿 (실제 .env는 커밋하지 않음)
skills/              - 설치된 스킬들
CLAUDE.md            - Agent 행동 지침
```

## 다른 PC에서 사용하기

### 1. Hermes Agent 설치
```powershell
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

### 2. 설정 파일 복원
```powershell
# 이 저장소 클론
git clone https://github.com/YOUR_USERNAME/hermes-config.git

# 설정 파일을 Hermes 홈 디렉토리로 복사 (Windows 기준)
$hermesHome = "$env:LOCALAPPDATA\hermes"

# config.yaml 복사
Copy-Item ".\hermes-config\config.yaml" -Destination "$hermesHome\config.yaml"

# skills 폴더 동기화
Copy-Item ".\hermes-config\skills\*" -Destination "$hermesHome\skills\" -Recurse -Force
```

### 3. API 키 설정
```powershell
# .env.example을 참고해서 .env 파일 생성
Copy-Item ".\hermes-config\.env.example" -Destination "$hermesHome\.env"
# .env 파일을 편집해서 실제 API 키 입력
```

## 주의사항

- `.env` 파일은 **절대 커밋하지 마세요** — API 키가 포함되어 있습니다
- 스킬 업데이트는 Hermes 자동 업데이트(`hermes skills update`)를 이용하세요
- 새 스킬 설치 후 이 저장소에 반영하려면 `skills/` 폴더를 동기화하세요
