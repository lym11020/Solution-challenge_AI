### AI_drug mortality

Our model was developed using vertex ai, google ai studio.

## Risk prediction(using vertex ai)

drug_deaths_final_with_risk_age_sex_race.csv


go to console of vertex ai

create datasets(region:asia-northeast3)

Model Development-Training

Train new model

Deploy And Use- Model Registry 
"'fetch('https://asia-northeast3-aiplatform.googleapis.com/v1/projects/50762632220/locations/asia-northeast3/endpoints/5218607640866717696:predict', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer ya29.a0AfB_byCaT-GPp62k3fWpDyf9QtMyqEaVVWtji2K1ZT0WrSbx-Qi0lcIjZTXTibk6yUV_oUChX7pi37O2QWIHgmEX7PmecbSHmE0q428L6iZ7TxCBTNRbgkVctR_EtqrAaHS8FDC0yRmK3PIzFFaTKeYJmg1CIMZLIos600GS9qMaCgYKAYMSARMSFQHGX2MiUB-mOynxgO22aN_BTR9ZdQ0178',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    instances: [
      // 여기에 모델 입력 데이터 포맷에 맞춰 데이터를 추가
    ],
  }),
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));'"
Create Model Registry

Deploy&Test (using predict instance.txt)

## Chatbot

google ai studio

model: Gemini 1.0 Pro

Safety settings

![image](https://github.com/lym11020/Solution-challenge_AI/assets/124680236/82aa13de-8a98-4459-be59-d50c66964400)


Deploy model

![image](https://github.com/lym11020/Solution-challenge_AI/assets/124680236/66948032-a322-4502-9d2a-3ca7c7a797da)


## Reference

Dataset

https://www.kaggle.com/datasets/ruchi798/drug-overdose-deaths
