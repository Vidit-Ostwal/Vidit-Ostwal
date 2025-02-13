# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that the comment be directed to @ninad-opsverse, as it specifically addresses an observation made by them. @Vidit-Ostwal has asked if the issue being discussed also affects the Python output, but the details of the issue were not mentioned in their comment.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that the changes in this pull request should be merged into the main branch. They believe that the changes are ready to be integrated and will improve the overall quality of the project.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested organizing the code structure as follows:

- Incorporate a crew within a tool.
- Include parent agents.
- Allow the tool to initiate a crew.
- Manage the crew using a parent crew.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that instead of using pre-computed or generalized managers, it's better to have more control over the management. However, the comment does not provide specific reasons or details on why this is preferred.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that `human_input` is called after a task has been performed and asks for user feedback on the generated response, rather than incorporating additional context during crew execution. He recommends providing all necessary input during `crew.kickoff()` instead.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests providing context or guidance on tools and agents for the manager LLM. However, they note that internally, the manager LLM is an agent itself, making adding a dedicated 'manager_note' specific to one agent less ideal. Instead, they recommend allowing users to request an agent to create descriptions, goals,*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested a solution to the issue by changing the Docker port and ClickHouse port to 9005. The change resolved the issue.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may result from a security process running on port 9000, which is preventing the desired function from executing. Due to the security process being active, attempts to terminate it have been unsuccessful.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested to try the command again, as the logs provide more information about the issue. The logs show that Redis and PostgreSQL have started successfully, but LangFuse web services are repeatedly failing to apply ClickHouse migrations. These failures are likely due to the ClickHouse database being unavailable.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested updating the `docker-compose.yml` file with modified ports for ClickHouse and MinIO. The ClickHouse external port is now `9009` and the MinIO external port is `9010`. These changes have been made to resolve an issue that was previously being encountered.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested guidelines for summarizing the comment. The guidelines include: summarizing the entire comment in exactly 100 words, ignoring mentions, providing the summary from the perspective of "@Vidit-Ostwal has suggested", disregarding code details, avoiding external links, writing the summary in plain text, and ensuring all relevant information is included.*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that when attempting to call the litellm API with the google studio, they encountered a `BadRequestError`. The error message indicates that the `contents` parameter in the `GenerateContentRequest` is not specified. @Vidit-Ostwal is using litellm version 1.60.2 and is not part of an ML Ops Team.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested further investigating an issue regarding port 9000 conflicts during the setup of LangFuse via Docker Compose. They have encountered a problem where port 9000, used by both ClickHouse and MinIO, is already occupied by a system process. Changing the port did not resolve the issue, as they*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the documentation for using CrewAI embeddings is incorrect and should be updated to replace occurrences of "model_name" with "model" in the input parameters. The issue affects various examples in the documentation, including those for Azure OpenAI, Google AI, Vertex AI, and Cohere embeddings.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested enhancing the output logging feature by incorporating a JSON format. This change is proposed to address issue #1970 and enhance the parsability of the output log file. The user has expressed willingness to contribute to this feature through a pull request.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111. In this fix, user messages are now formatted by the "feedback" function. The details of the implementation are not included in the comment, but it can be assumed that the change addresses the issue reported in #2111.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. The commit addresses the reported problem and resolves it effectively. By implementing this change, the issue is thoroughly addressed and no longer persists.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the reset memories issue mentioned in #2023. Additionally, they recommend removing the CLI command to reset memories and making documentation changes. @Vidit-Ostwal is willing to implement these changes if the proposed solution aligns with the team's requirements.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue mentioned in issue #2030.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as JSON files.

When initializing the crew, set `output_log_file` to True or provide a file name, and enable `save_as_json` to True. The resulting JSON file holds an array of JSON events, making it convenient for parsing and analysis.*

## ⭐ Starred Repositories
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
