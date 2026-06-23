# DevBridge AI 팀 구성

> 이 문서는 DevBridge 프로젝트의 AI 담당자 팀 구성을 정의합니다.
> 모든 담당자는 Hermes Agent 프로필로 실행됩니다.

## 팀 구조

```
                        👤 대표 (CEO)
                    전략, 의사결정, 최종 승인
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   💼 사업 개발팀    🛠️ 개발 기술팀    📊 경영 관리팀
```

## 사업 개발팀

| 프로필 | 역할 | 이름 |
|--------|------|------|
| `marketing` | CMO | 📈 마케팅 AI |
| `sales` | CSO | 🤝 영업 AI |
| `cs` | CCO | 🎧 고객관리 AI |

## 개발 기술팀

| 프로필 | 역할 | 이름 |
|--------|------|------|
| `devops` | CTO (인프라) | 🏗️ DevOps AI |
| `backend` | 백엔드 리드 | 🔧 Backend AI |
| `frontend` | 프론트 리드 | 📊 Frontend AI |
| `qa` | QA 리드 | ⚙️ QA AI |
| `security` | 보안 리드 | 🛡️ Security AI |

## 경영 관리팀

| 프로필 | 역할 | 이름 |
|--------|------|------|
| `finance` | CFO | 💰 회계 AI |
| `legal` | CLO | 📋 법무 AI |
| `data` | CDO | 📊 데이터 AI |

## 사용법

```bash
# 특정 담당자와 대화
hermes --profile marketing "블로그 포스트 작성해줘"
hermes --profile sales "제휴 제안서 만들어줘"
hermes --profile cs "FAQ 10개 만들어줘"
hermes --profile finance "이번 달 비용 리포트"
hermes --profile legal "이용약관 초안"
hermes --profile data "사용자 분석 리포트"
hermes --profile devops "서버 상태 확인"
hermes --profile backend "API 개발"
hermes --profile frontend "UI 개선"
hermes --profile qa "테스트 실행"
hermes --profile security "보안 점검"
```

## 제약사항

- 모든 담당자는 👤 대표의 승인이 필요한 작업을 인지해야 함
- 예산, 계약, 법적 문제는 👤에게 에스컬레이션
- 프로덕션 배포는 ⚙️ QA AI 테스트 통과 후 🏗️ DevOps AI가 실행
