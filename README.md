# Azure AI Language Custom Text Classification Tool for Prompt Flow
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/InfinityReply/promptflow-azure-ai-language-custom-text-classification/python-publish.yml)
![PyPI - Version](https://img.shields.io/pypi/v/promptflow-azure-ai-language-custom-text-classification)
![PyPI - Downloads](https://img.shields.io/pypi/dm/promptflow-azure-ai-language-custom-text-classification)

> Based on [promptflow-azure-ai-language](https://pypi.org/project/promptflow-azure-ai-language/)

| Name                       | Description                                                          |
|----------------------------|----------------------------------------------------------------------|
| Custom Text Classification | Use Azure AI Language to generate abstractive summaries of documents |

## Requirements
PyPI package: promptflow-azure-ai-language.

- For AzureML users: follow this [wiki](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-custom-tool-package-creation-and-usage?view=azureml-api-2#prepare-runtime), starting from `Prepare runtime`.
- For local users:
```bash
pip install promptflow-azure-ai-language
```
You may also want to install the [Prompt flow for VS Code extension](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow).

## Prerequisites
The tool calls APIs from Azure AI Language. To use it, you must create a connection to an [Azure AI Language resource](https://learn.microsoft.com/en-us/azure/ai-services/language-service/). [Create a Language Resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics) first, if necessary.

- In Prompt flow, add a new `CustomConnection`.
  - Under the `secrets` field, specify the resource's API key:` api_key: <Azure AI Language Resource api key>`
  - Under the `configs` field, specify the resource's endpoint: `endpoint: <Azure AI Language Resource endpoint>`

## Inputs
When a tool parameter is of type `Document`, it requires a `dict` object of [this](https://learn.microsoft.com/en-us/rest/api/language/text-analysis-runtime/analyze-text?view=rest-language-2023-04-01&tabs=HTTP#multilanguageinput) specification.

Example:

```python
my_document = {
    "id": "1",
    "text": "This is some document text!",
    "language": "en"
}
```


| Name            | Type             | Description                                                                                          | Required |
|-----------------|------------------|------------------------------------------------------------------------------------------------------|----------|
| connection      | CustomConnection | The created connection to an Azure AI Language resource.                                             | Yes      |
| document        | Document         | The input document.                                                                                  | Yes      |
| project_name    | string           | The project to be called.                                                                            | Yes      |
| deployment_name | string           | The project deployment to be called.                                                                 | Yes      |
| max_retries     | int              | The maximum number of HTTP request retries. Default value is 5.                                      | No       |
| max_wait        | int              | The maximum wait time (in seconds) in-between HTTP requests. Default value is 60.                    | No       |
| parse_response  | bool             | Should the full API JSON output be parsed to extract the single task result. Default value is False. | No       |

## Outputs
- When the input parameter parse_response is set to False (default value), the full API JSON response will be returned (as a dict object).
- When the input parameter parse_response is set to True, the full API JSON response will be parsed to extract the single task result associated with the tool's given skill. Output will depend on the skill (but will still be a dict object).
Refer to Azure AI Language's REST API reference for details on API response format, specific task result formats, etc.