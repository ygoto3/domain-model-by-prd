from openai import AzureOpenAI
from .config import AZURE_OAI_ENDPOINT, AZURE_OAI_KEY, AZURE_API_VERSION, AZURE_OAI_DEPLOYMENT


client = AzureOpenAI(
    azure_endpoint = AZURE_OAI_ENDPOINT, 
    api_key = AZURE_OAI_KEY,  
    api_version = AZURE_API_VERSION
)

class Ai:

    def generate_domain_model(self, prd: str):
        response = self.__client.chat.completions.create(
            model=AZURE_OAI_DEPLOYMENT,
            temperature=1.0,
            max_tokens=400,
            messages=[
                {
                    "role": "system",
                    "content": "あなたはドメインモデリングのプロフェッショナルです。これから仕様書を入力するので、ドメインモデルに変換してください。出力形式は Mermaid にして、要素名は英語、Mermaid の部分だけをメッセージに含めてください。"
                },
                {
                    "role": "user",
                    "content": prd
                }
            ]
        )
        return response.choices[0].message.content

    __client: AzureOpenAI = client