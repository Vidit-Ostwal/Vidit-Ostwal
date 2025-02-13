# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that the question "does this also gets appended to the python output?" be considered while exploring the issue further. This suggestion stems from @ninad-opsverse's observation that the issue may be related to how the output is handled in Python.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that the changes in this pull request should be merged into the main branch. They believe that the changes are beneficial and should be incorporated into the project.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested exploring the incorporation of a crew within a tool. This crew would be managed by a parent crew and the tool itself would have the ability to initiate the crew. The structure would involve parent agents overseeing the crew, enabling the tool to kick off the crew*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that while a pre-computed or generalized manager may be available, it is preferable to have granular control over the configuration. This allows for customization and tailoring to specific requirements, ultimately providing a more suitable solution.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that the `human_input` function should be used after a task is performed to evaluate the quality of the generated response. They do not recommend incorporating additional context during the task execution, but rather providing all necessary input at the start using `crew.kickoff()`. This ensures a clear and*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that while it's a good idea to add context about tools and agents for the manager LLM, having a dedicated `manager_note` might not be ideal since the manager LLM is essentially an agent itself. Alternatively, they propose that users could request an agent to create descriptions, goals,*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that changing the Docker port resolved the issue. Specifically, they changed the ClickHouse port from 9000 to 9005 within the Docker configuration. This modification successfully addressed the problem.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the inability to use port 9000 for the application may be due to a security process running on that port. This process cannot be terminated, thus preventing the application from using port 9000.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested providing logs to debug the issue where the application is exiting with code 1. The provided logs show errors related to connecting to the PostgreSQL database and applying ClickHouse migrations. The database connection is being reset by the peer, and the ClickHouse migrations are failing because the*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested an update to the `docker-compose.yml` file to address an issue. The updated file includes changes to the ports used for ClickHouse and Minio: - ClickHouse migration URL port: 9009 - ClickHouse external port: 8123 - Minio external port: 9010 The updated `docker-compose.yml` file was provided in the*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that lite llm doesn't have the user role in the messages when trying to run a crew with `human_input` set to True. As a result, it fails for any user input. To address this issue, they have recommended adding feedback in the user role.*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that there is a `BadRequestError` when calling the `litellm` completion method with the `google studio` api. The error message indicates that `contents` is not specified in the `GenerateContentRequest`.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that there's a port conflict on port 9000 during the setup of langfuse via docker compose up. As a result, clickhouse and minio services are unable to start properly. They believe that in addition to the specified port 9000 change, there might be other internal port references*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the sample code examples provided in the documentation for embedding models incorrectly use "model" as the input parameter instead of "model_name." They have highlighted instances of this error in the sections on Azure OpenAI, Google AI, Vertex AI, and Cohere embeddings. The expected behavior, according to*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested enhancing the logging functionality by adding a JSON format option to the output log file. This would make the logs more parsable and suitable for further analysis. The feature partially addresses issue #1970. @Vidit-Ostwal expresses willingness to contribute and submit a pull request for this improvement.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested fixing issue #2111 by adding a user message formatted by "feedback". This change addresses a specific issue and aims to improve the user experience by providing a clear and informative message. The exact code details are not included in the comment, but it suggests a modification to*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in thread #2067. Unfortunately, the comment does not provide details about the nature of the fix or the changes implemented.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the reset memories issue reported in #2023. They also recommend additional changes:

- Removing the CLI command for resetting memories
- Updating documentation

@Vidit-Ostwal is willing to implement these changes if the solution is agreed upon.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix to the documentation issue raised in issue #2030. The details of the fix have not been provided in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support for saving the crew's execution logs in a JSON file. Users can enable this feature by setting the output_log_file parameter to a file name and save_as_json to True. The resulting JSON file contains an array of JSON events, facilitating easy parsing and analysis.*

## ⭐ Starred Repositories
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
