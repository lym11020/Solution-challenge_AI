### AI_drug mortality

A model predicting the risk of mortality was developed using Vertex AI, and a chatbot was created using Google AI Studio.

## Risk prediction(using [vertex ai](https://cloud.google.com/vertex-ai?hl=ko))

drug_deaths_final_with_risk_age_sex_race.csv

1. Access the Vertex AI console and ensure you're working within the appropriate region, specifically Asia-northeast3.

2. Create datasets within this region to be used for training and evaluation purposes. These datasets will serve as the foundation for developing your machine learning models.

3. Move forward with Model Development and Training by initiating the process to train a new model. This involves selecting the appropriate algorithm, specifying the training data, configuring hyperparameters, and initiating the training process.

4. Once the model has been successfully trained, proceed to register it within the Model Registry. This step involves documenting essential information about the model, including its version, metadata, and any associated artifacts.

5. After registration, deploy the model to make it accessible for inference purposes. This deployment enables users to send input data to the model and receive predictions or classifications in return.

6. As part of the deployment process, it's crucial to conduct thorough testing to ensure the model's performance meets expectations. Utilize the "predict instance.txt" file to simulate real-world scenarios and assess how the model handles various inputs.

7. Monitor the deployed model's performance over time, making adjustments as necessary to maintain optimal accuracy and reliability.

<pre>
<code>
  fetch('https://asia-northeast3-aiplatform.googleapis.com/v1/projects/50762632220/locations/asia-northeast3/endpoints/5218607640866717696:predict', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer ya29.a0AfB_byCaT-GPp62k3fWpDyf9QtMyqEaVVWtji2K1ZT0WrSbx-Qi0lcIjZTXTibk6yUV_oUChX7pi37O2QWIHgmEX7PmecbSHmE0q428L6iZ7TxCBTNRbgkVctR_EtqrAaHS8FDC0yRmK3PIzFFaTKeYJmg1CIMZLIos600GS9qMaCgYKAYMSARMSFQHGX2MiUB-mOynxgO22aN_BTR9ZdQ0178',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    instances: [
      // Here, add data according to the model input data format
    ],
  }),
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
</code>
</pre>


## Chatbot

[google ai studio](https://ai.google.dev)

model: Gemini 1.0 Pro

Safety settings

![image](https://github.com/lym11020/Solution-challenge_AI/assets/124680236/82aa13de-8a98-4459-be59-d50c66964400)

Setting up the initial part & Entering information about the risks of drugs and specialized knowledge related to them."

![image](https://github.com/lym11020/Solution-challenge_AI/assets/124680236/66948032-a322-4502-9d2a-3ca7c7a797da)


Deploy model



## Reference

Dataset

https://www.kaggle.com/datasets/ruchi798/drug-overdose-deaths
