
from google.cloud import recaptchaenterprise_v1
from google.cloud.recaptchaenterprise_v1 import Assessment
from dotenv import load_dotenv
import os
from configparser import ConfigParser

load_dotenv()
recaptcha_config = ConfigParser()
recaptcha_config.read("config.ini")
assert "recaptcha_actions" in recaptcha_config


def create_assessment(
    project_id: str, recaptcha_site_key: str, token: str, expected_action: str
) -> Assessment:
    """Create an assessment to analyze the risk of a UI action.
    Args:
        project_id: Google Cloud Project ID
        recaptcha_site_key: Site key obtained by registering a domain/app to use recaptcha services.
        token: The token obtained from the client on passing the recaptchaSiteKey.
        expected_action: The expected action for this type of event.
    Returns: Assessment response.
    """

    client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceClient()

    event = recaptchaenterprise_v1.Event()
    event.site_key = recaptcha_site_key
    event.token = token
    event.expected_action = expected_action

    assessment = recaptchaenterprise_v1.Assessment()
    assessment.event = event

    project_name = f"projects/{project_id}"

    request = recaptchaenterprise_v1.CreateAssessmentRequest()
    request.assessment = assessment
    request.parent = project_name

    response = client.create_assessment(request)

    return response
