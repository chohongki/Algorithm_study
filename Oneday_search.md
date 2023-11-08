# 1) 특정 로봇(혹은 서비스)을 정해주세요.
> __2족 보행 로봇__

- Tesla - Optimus
https://www.youtube.com/watch?v=y4KYxyudQcU&ab_channel=%EC%B1%84%EB%84%90A%EB%89%B4%EC%8A%A4
- boston dynamics - atlas
https://www.youtube.com/watch?v=tF4DML7FIWk&ab_channel=BostonDynamics
- ghost robotics - vision 60
https://www.youtube.com/watch?v=hDSXD_cB_Hc&ab_channel=GhostRobotics

# 2) 관련 로봇의 자료를 조사해 주세요. 특히 먼저 블로그와 같은 자료를 찾아서 정리해 주세요.

- Dynamic Manipulation
- Real-time perception
- model-predictive control
https://bostondynamics.com/atlas/

https://www.e-patentnews.com/7717

http://www.sisaweek.com/news/articleView.html?idxno=208561
스팟 - 운동지능 AI

# 3) Search the patent related these robots

## Natural Pitch and Roll (US-9517561-B2)
https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9517561
> 첫번째 센서들로 사지 각각의 joint의 관절각을 구한다. 두번째 센서들로 몸의 Orientation을 측정한다. 
	시스템은 첫번째 측정값과 Orientation 정보를 조합하여 관계를 결정하고 이를 바탕으로 로봇의 Orientation을 추정하는 수단을 포함한다. 그리고 시스템은 로봇의 예상되는 Orientation을 바탕으로 적어도 하나 이상의 팔, 다리를 제어한다.
## Methods and devices for automatic gait transition (US-9931753-B1)
https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9931753
> 1. Computing system으로부터 

# 4) 
## Machine Learning Algorithms in Bipedal Robot Control
http://dx.doi.org/10.1109/TSMCC.2012.2186565
> 기존에 bipedal 제어 기술은 많았지만 제어 법칙이 일반적으로 미리 프로그래밍되고 유연하지 못함.
> 1. __Nonlinear dynamics__ : bipedal robot은 nonlinear하고 불안정한 시스템이므로 기존의 linear 제어 방식은 바로 적용시킬 수 없음.
> 2. __Discretely changing in dynamics__ : 두발로 딛고 안정된 상태와 한발로 선 불안정한 상태가 있는데 두 상황에서 차근차근 보행하는 적합한 제어 전략이 필요하다.
> 3. __Underactuated system__: 걷는 로봇은 땅과 붙어있지 않아 두 다리의 joint가 모두 완벽하게 제어되어야 함에도 로봇의 모든 자유도를 제어하기에 충분하지 않다.
> 4. __Multivariable system__: 3차원 공간에서 걷는 system은 굉장히 많은 자유도를 가지며, 자유도간의 상호작용과 multijoint 움직임의 좌표계는 매우 어려운 제어 문제를 야기한다.
> 5. __Changing environments__: 지면 상태와 장애물 등 여러 외부 요인으로 인한 제어 전략이 환경 변화에 맞게 빠르게 적응해야함
	(대충 그래서 우리는 어떤 솔루션이다.)
### Passive dynamics
https://www.science.org/doi/10.1126/science.1107799
bi-pedal control 안정화, 에너지 효율을 위한 기구학

# 5) 문제1에서 정한 주제를 문제 2, 3, 4의 자료를 통해 정리한 내용을 바탕으로 여러분들이 구현하고 싶은 로봇의 기술을 설명해 주세요.

자율 보행이 가능한 2족 보행 로봇
예상 필요 기술 ) bi-pedal control을 위한 학습, perception, path planning

# 6) 문제5에서 정리한 내용을 바탕으로 로봇의 동작을 설명해주세요

1. 정지시 환경 요인을 고려하여 밸런스를 잡고 서 있는다.
2. 사용자가 도착지를 설정한다
3. 잠시 뒤 로봇이 도착지를 향해 전진하며 장애물을 탐지하고 장애물 발견시 우회한다.

# 7) 오늘 주제를 바탕으로 검색을 통해 시장 규모를 찾아보고 요약해주세요

- 고스트 로보틱스 - 2022 기준 연 4000만 달러 매출
http://m.irobotnews.com/news/articleView.html?idxno=28748
- 보스턴 다이나믹스 -2021 기준 매출 약 57조 7천억원
https://news.bizwatch.co.kr/article/industry/2021/09/10/0032