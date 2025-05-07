import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/beltramelofelipe/a33ba1f51a9ace463bb11462272ced50/raw/53d70a28b629c3d2ade732ab98124fab2a2ac480/scrap-felipe-beltra.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )

    else:

        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "api_key": os.environ["SCRAPING_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }

        response = requests.get(api_endpoint, params=params, timeout=10)

    data = response.json().get("person", response.json())

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="ttps://www.linkedin.com/in/felipe-garcia-beltramelo/",
            mock=True,
        ),
    )
