# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that it is a nice observation to ask whether the content also gets appended to the Python output.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that the changes in this pull request should be merged into the main branch. They did not provide any specific details or reasons for requesting the merge.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool. Additionally, parent agents should be included with the tool's capability to commence a crew, which will be supervised by a parent crew. This proposed design aims to improve the organization and management of crews within the tool.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that while pre-computed or generalized managers may be available, it is preferable to retain control over such operations. This allows for greater flexibility and customization to meet specific requirements.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that there may be a misunderstanding about `human_input`. It is not intended to be used to incorporate additional context during task execution. Instead, it is called after the task is performed to ask the user to evaluate the generated response. It is recommended to provide all necessary*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests that including context and information about the manager LLM's tools and agents is a valuable addition. However, they express concern that adding a "manager_note" specifically for the manager LLM might not be ideal, as it's essentially just another agent internally. They also propose exploring the possibility of instructing*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested changing the Docker port to resolve the issue. They specifically changed the ClickHouse port from 9000 to 9005, which resolved the problem. They have also expressed gratitude to @Steffen911 for their assistance.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that port 9000 is causing the issue because a security process is running on it. This security process cannot be stopped.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that they have just tried the command again with logs for reference. The logs indicate that the Redis server is starting, and that the PostgreSQL database is ready to accept connections. However, there are several errors suggesting that the ClickHouse migrations failed due to the database being*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has updated the `docker-compose.yml` file and changed the ports for both ClickHouse and MinIO to resolve a persistent issue. The specific ports updated are 9009 for ClickHouse and 9010 for MinIO. Additionally, @Vidit-Ostwal has suggested that if the problem persists, it may be within a different internal file.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the `human_input` in the provided code is set to `True`, but it fails for any input provided by the user. This is because the lite LLM, when called, is not given the user role in the messages. Therefore, the lite LLM is unable to process user*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that while using the litellm API with the Google Studio API, they received a `BadRequestError` exception with the message "* GenerateContentRequest.contents: contents is not specified\n". They provided a code snippet where they are trying to call the `completion()` function without specifying the `contents` parameter. They are using*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the bug is due to port 9000 being used by another system process which cannot be killed. As a result, ClickHouse and MinIO cannot listen on port 9000 while setting up LangFuse via Docker, causing migration failures. They are requesting assistance in identifying all locations where*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the sample code examples for embedding input should use `model_name` instead of `model`. This change should be made in the following documentation pages:

- https://docs.crewai.com/concepts/memory#using-azure-openai-embeddings
- https://docs.crewai.com/concepts/memory#using-google-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-vertex-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-cohere-embeddings*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested enhancing the output_log_file's functionality by adding a JSON format option alongside the current .txt format. This JSON format would facilitate further analysis and partially address issue #1970. They are willing to contribute a pull request to implement this feature.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the issue #2111 has been addressed. Additionally, a formatted user message by `feedback` has been included as part of the fix. No further information or action items are mentioned in the comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. The exact details of the fix haven't been specified in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested further improvements to the fix that resolves the memory reset issue reported in #2023. These include:

- Removing the CLI command to reset memories
- Making necessary documentation changes*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a commit that resolves the documentation issue brought up in issue #2030. This commit modifies the documentation to address the concerns raised in the issue, thereby improving the clarity and accuracy of the documentation.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs in a JSON file format. You can now specify the output_log_file argument to set a file name and enable save_as_json to True while initializing the Crew object. This will create a JSON file containing an array of JSON events, allowing for convenient*

## ⭐ Starred Repositories
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
