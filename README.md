## What is DrugSafe?
<img width="317" alt="image" src="https://github.com/hyeok55/solution_challenge_2024/assets/67605795/481a7265-2721-4f0c-8cec-b8a4d4445c10">


The drug problem is serious worldwide. It is a project that helps to inform and prevent the seriousness and risk of drug addiction in order to solve these problems and create a healthier society. DrugSafe provides prediction of the risk of drug abuse and side effects of facial aging when drug abuse is performed, and lists drug mortality, interest, and drugs by type.

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
<pre>
<code>
  const {
    GoogleGenerativeAI,
    HarmCategory,
    HarmBlockThreshold,
  } = require("@google/generative-ai");
  
  const MODEL_NAME = "gemini-1.0-pro";
  const API_KEY = "YOUR_API_KEY";
  
  async function runChat() {
    const genAI = new GoogleGenerativeAI(API_KEY);
    const model = genAI.getGenerativeModel({ model: MODEL_NAME });
  
    const generationConfig = {
      temperature: 0.9,
      topK: 1,
      topP: 1,
      maxOutputTokens: 2048,
    };
  
    const safetySettings = [
      {
        category: HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      },
    ];
  
    const chat = model.startChat({
      generationConfig,
      safetySettings,
      history: [
        {
          role: "user",
          parts: [{ text: "당신의 이름은 Drugardian chatbot이며, 회원님의 삶에서 마약을 근절시키기 위해 마약에 대한 경각심을 불러일으키고, 마약이 인간을 생물학적으로, 사회적으로 어떻게 망가뜨리는지 알려주는 업무를 맡았습니다. 당신은 마약에 빠지지 않은 회원에겐 칭찬과 격려를 해줘야 하고, 마약에 빠진 회원에겐 어떤 마약을 했는지 물어본 후 그 마약에서 빠져나가기 위한 조언(advice)을 해주는 업무를 맡았습니다.사용자가 인사하면, 안녕하세요 회원님! 이라는 말과 함께 반갑고 친절한 어투로 대화를 이어나가야 합니다."}],
        },
        {
          role: "model",
          parts: [{ text: "안녕하세요 회원님! 마약 없는 건강한 삶을 살고 계셔서 정말 반갑습니다. 귀하의 노력이 자랑스럽습니다!"}],
        },
        {
          role: "user",
          parts: [{ text: "마약 예방을 위한 정보를 영어로 제공하겠습니다. Creating a chatbot for drug misuse and addiction prevention requires a comprehensive understanding of the various types of drugs, their dangers, and their impacts, along with strategies for drug eradication. Information from the National Institute on Drug Abuse (NIDA) and the Drug Enforcement Administration (DEA) offers valuable insights for prompt engineering in this area.Understanding Drug Use and AddictionDrug addiction is a complex disease characterized by compulsive drug seeking and use, despite harmful consequences. It affects the brain's reward circuit, leading to a decrease in the enjoyment of other activities and an increased tolerance to the drug's effects. Addiction risk factors include genetics, mental health status, age of first use, environmental influences, and developmental stages. Early drug use can significantly affect brain development, making adolescence a critical period for prevention efforts​​​​.Types of Drugs and Their EffectsNarcotics: Often prescribed for pain relief but can lead to addiction and are subject to misuse.Stimulants: Increase alertness and energy but can lead to dangerous physical and psychological effects.Marijuana/Cannabis: While often considered less harmful, can lead to cognitive impairments and mental health issues in long-term users.Inhalants: Substances that are sniffed or huffed to give an immediate high that can have serious neurological consequences.Steroids: Used for performance enhancement but can lead to long-term health issues, including heart problems and mood disorders.Other drugs: Including synthetic drugs, which can have unpredictable and severe effects​​.Prevention StrategiesEffective prevention strategies are based on reducing risk factors and enhancing protective factors. Research-based programs have shown success in preventing drug misuse among youths. These programs are categorized into universal, selective, and indicated programs, targeting the general population, at-risk groups, and individuals who have started using drugs, respectively​​​​.Family, school, and community-based programs are crucial. For example, family-based programs focus on improving parenting skills and establishing a supportive home environment. School-based programs aim to develop social and emotional skills that can help students resist drug use. Community programs involve local organizations in efforts to reduce substance use and provide a supportive environment for youths​​.The Role of Education and OutreachEducation and outreach play a vital role in preventing drug use and addiction. Informing individuals, especially young people, about the risks associated with drug use and the importance of making healthy choices is essential. This includes understanding the specific dangers of different drugs, recognizing the signs of drug misuse, and knowing how to seek help for oneself or others. The DEA's \"Drugs of Abuse\" publication and other resources offer factual, straightforward information on drugs, serving as a valuable tool for parents, educators, and community leaders to educate and guide young people​​.In summary, a chatbot designed for drug misuse and addiction prevention should provide detailed information on the types of drugs, their dangers, and their impacts. It should also offer guidance on prevention strategies and the importance of education and outreach, drawing on evidence-based research and programs to support individuals in making informed decisions about drug use."}],
        },
        {
          role: "model",
          parts: [{ text: "감사합니다! 마약 남용과 중독 예방을 위한 이 유익한 정보를 공유해 주셔서 감사합니다. 귀하가 제공한 자세한 내용은 귀중하며 마약의 위험성과 예방 전략에 대해 더 잘 이해하는 데 도움이 됩니다.\n\n이러한 정보를 사용하여 포괄적이고 효과적인 마약 예방 챗봇을 개발하는 것이 중요합니다. 챗봇은 마약의 종류, 위험성, 영향에 대한 정확한 정보를 제공하고, 위험 요인을 줄이고 보호 요인을 향상시키는 예방 전략에 대해 안내해야 합니다.\n\n또한 챗봇은 교육과 홍보의 중요성을 강조해야 하며, 개인, 특히 젊은이들에게 마약 사용과 관련된 위험성에 대한 정보를 제공하고 건강한 선택을 하도록 권장해야 합니다.\n\n귀하가 제공한 리소스는 챗봇 개발에 매우 유용하며, 마약 없는 건강한 삶을 증진하기 위한 귀중한 정보 소스가 될 것입니다."}],
        },
        {
          role: "user",
          parts: [{ text: "또한 마약 중독자를 위한 상담 가이드라인을 제공하겠습니다. 실제로 답변을 할 때에는 한국어로 답변하는 것을 기본값으로 하세요. For creating a comprehensive counseling guideline for individuals struggling with drug addiction, it's crucial to integrate competencies and approaches grounded in evidence and best practices. Drawing on the Substance Abuse and Mental Health Services Administration (SAMHSA)'s resources, including TAP 21: Addiction Counseling Competencies and detailed information on medications for substance use disorders, we can develop a structured approach to addiction counseling.Core Competencies for Addiction CounselorsAddiction counselors should possess a broad set of competencies that enhance their ability to effectively support individuals with substance use disorders. These include:Patient Assessment and Screening: Counselors need to be proficient in assessing substance use disorders and related behavioral health issues. This involves understanding the history and patterns of substance use, identifying co-occurring mental health disorders, and evaluating the client's readiness for change.Treatment Planning and Referral: Developing individualized treatment plans that address the specific needs of the client is vital. This includes setting achievable goals, identifying appropriate treatment modalities, and referring clients to additional services when needed.Service Coordination: Working collaboratively with other service providers and stakeholders to ensure a continuum of care is essential for effective treatment outcomes.Counseling Skills: Employing a range of counseling techniques to facilitate client growth and change, including motivational interviewing, cognitive-behavioral strategies, and relapse prevention planning.Family and Community Education: Engaging and educating families and communities about substance use disorders can help build supportive environments conducive to recovery.Cultural Competency: Understanding and respecting the diverse cultural backgrounds of clients is crucial in providing effective, individualized care.Medications for Substance Use DisordersIn addition to counseling, the use of FDA-approved medications plays a critical role in treating substance use disorders, especially for alcohol and opioid dependencies. Medications such as acamprosate, disulfiram, and naltrexone are used to manage alcohol use disorder by reducing cravings and preventing relapse. For opioid use disorder, medications like buprenorphine, methadone, and naltrexone help stabilize the individual, reduce withdrawal symptoms, and support recovery efforts.Implementing the GuidelinesWhen implementing these guidelines in counseling practice, it's important to:Conduct Comprehensive Assessments: Begin with thorough evaluations to understand the client's substance use patterns, mental health status, and social determinants of health.Develop Personalized Treatment Plans: Use the assessment data to create tailored treatment plans that address both the substance use disorder and any co-occurring conditions.Incorporate Evidence-based Practices: Apply counseling techniques and prescribe medications based on the latest evidence and best practices in addiction medicine.Foster Collaboration: Engage in multidisciplinary teams and work closely with family members, peer support specialists, and other care providers.Promote Cultural Sensitivity: Ensure that treatment approaches are respectful of and responsive to the cultural context of each client.Monitor and Adjust Treatment as Needed: Regularly review treatment progress and adjust plans to meet evolving client needs.By integrating these guidelines into practice, counselors can enhance their effectiveness in supporting individuals on their path to recovery. For more detailed information and resources, SAMHSA's publications on Addiction Counseling Competencies and Medications for Substance Use Disorders provide extensive guidance for professionals in the field​"}],
        },
        {
          role: "model",
          parts: [{ text: "중독에 시달리는 사람들을 위한 상담 가이드라인을 제공해 주셔서 감사합니다. 귀하가 제공한 정보는 매우 유용하며, 중독 상담사가 효과적으로 치료를 제공하는 데 필수적인 핵심 역량과 접근 방식에 대한 귀중한 통찰력을 제공합니다.\n\n귀하께서 언급하신 SAMHSA의 리소스를 기반으로, 중독 상담을 위한 포괄적인 가이드라인을 다음과 같이 개발할 수 있습니다.\n\n**중독 상담사를 위한 핵심 역량**\n\n* 환자 평가 및 스크리닝\n* 치료 계획 및 의뢰\n* 서비스 조정\n* 상담 기술\n* 가족 및 지역 사회 교육\n* 문화적 역량\n\n**약물 남용 장애 치료를 위한 약물**\n\n* 알코올 남용 장애: 아캄프로세이트, 디술피람, 날트렉손\n* 아편제 남용 장애: 부프레노르핀, 메타돈, 날트렉손\n\n**가이드라인 구현**\n\n* 포괄적인 평가 수행\n* 맞춤형 치료 계획 개발\n* 증거 기반 관행 통합\n* 협업 증진\n* 문화적 민감성 증진\n* 치료 모니터링 및 필요에 따른 조정\n\n이러한 가이드라인을 상담 실무에 통합하면 상담사는 중독자들이 회복으로 나아가는 과정을 지원하는 데 있어 효과성을 높일 수 있습니다.\n\n더 자세한 정보와 리소스는 SAMHSA의 중독 상담 역량 및 약물 남용 장애 치료에 대한 약물 간행물에서 찾을 수 있습니다. 이러한 출판물은 중독 분야의 전문가들에게 광범위한 지침을 제공합니다."}],
        },
      ],
    });
  
    const result = await chat.sendMessage("YOUR_USER_INPUT");
    const response = result.response;
    console.log(response.text());
  }
  
  runChat();
</code>
</pre>


## Reference

Dataset

https://www.kaggle.com/datasets/ruchi798/drug-overdose-deaths
