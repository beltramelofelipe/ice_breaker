from dotenv import load_dotenv
import os

# from langchain import PromptTemplate
# from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    load_dotenv()
    print("Hello Langchain")
    # os.environ['OPENIA_API_KEY']

    # information = """
    # Kurt Donald Cobain (Aberdeen, 20 de fevereiro de 1967 – Seattle, c. 5 de abril de 1994) foi um cantor, compositor e músico norte-americano, famoso por ter sido o fundador, vocalista e guitarrista da banda Nirvana.[1]

    # Dentre suas principais composições, o single Smells Like Teen Spirit, do segundo álbum do Nirvana, "Nevermind", foi o responsável pelo início do sucesso do grupo e do próprio Kurt, popularizando um subgênero do rock alternativo que a imprensa passou a chamar de grunge.[2] Outras bandas grunge de Seattle, como Alice in Chains, Pearl Jam e Soundgarden, ganharam também um vasto público e, como resultado, o rock alternativo tornou-se um gênero dominante no rádio e na televisão nos Estados Unidos, do início à metade da década de 1990. O Nirvana foi considerado a banda "carro-chefe da Geração X", e seu vocalista, Kurt Cobain, viu-se ungido pela mídia como porta-voz da geração, mesmo contra sua vontade.[3]

    # Cobain não se sentia bem com a atenção que recebeu, e colocou seu foco na música da banda, acreditando que a mensagem da banda e sua visão artística tinham sido mal-interpretadas pelo público, desafiando a audiência da banda com o seu terceiro álbum In Utero. Desde sua estreia, a banda Nirvana, com Cobain como compositor, vendeu mais de vinte e cinco milhões de álbuns nos Estados Unidos, e mais de cinquenta milhões em todo o mundo.[4][5]

    # Durante os últimos anos de sua vida, Cobain lutou contra o vício em heroína, doenças, depressão, fama e imagem pública, bem como as pressões ao longo da vida profissional e pessoal em torno dele próprio e de sua esposa, a cantora Courtney Love. Em 8 de abril de 1994, Cobain foi encontrado morto em sua casa em Seattle, três dias após a sua morte, vítima do que foi oficialmente considerado um suicídio por um tiro de espingarda na cabeça. As circunstâncias de sua morte, por vezes, tornam-se um tema de fascínio e debate.[2]

    # A vida do cantor já foi retratada de várias maneiras e diversas vezes após a sua morte, seja no cinema, em livros ou em documentários televisivos.[6] A primeira delas foi em 1998, com o documentário Kurt & Courtney. Em seguida, em 2005, foi produzido o filme Last Days, um filme de gênero drama que narrava, de forma fictícia, os últimos dias de vida de Kurt. O documentário Kurt Cobain - Retrato de uma Ausência, lançado em 2006, continha entrevistas de amigos, parentes e do próprio Cobain.[7][8] Em 2006, doze anos após a sua morte, a revista Forbes listou as treze celebridades mortas que mais lucraram nos últimos doze meses do respectivo ano. O cantor ficou em primeiro lugar na lista, com ganhos estimados em cinquenta milhões de dólares estadunidenses.[9][10] Em 2014, no seu primeiro ano elegível, o cantor, junto com seus companheiros de banda, Krist Novoselic e Dave Grohl, foi admitido ao Rock and Roll Hall of Fame.[11]
    # """
    summary_template = """

        Dadas as informações {information} sobre uma pessoa , quero que você crie:
        1. Um breve resumo
        2. Dois fatos interessantes sobre ela

    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

    chain = summary_prompt_template | llm | StrOutputParser()

    linkedin_information = scrape_linkedin_profile(
        "https://www.linkedin.com/in/felipe-garcia-beltramelo/", mock=True
    )

    res = chain.invoke(input={"information": linkedin_information})

    print(res)
