# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that changing the Docker port resolved the issue. Specifically, the ClickHouse port was modified from 9000 to 9005, leading to a successful resolution.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may arise due to a security process running on port 9000, preventing the execution of the program on that port. Attempts to terminate this security process have failed.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested providing logs for further analysis. These logs show that: - Redis and Postgres are running and have initialized successfully. - ClickHouse is skipping initialization as the database directory contains a database. - MinIO is running and listening on port 9000 and 9001. - Langfuse's trace-upsert, trace-delete, project-delete,*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested the following changes to the `docker-compose.yml` file:

- Updated both the external and migration ports for ClickHouse to 9009.
- Updated both the external and internal ports for Minio to 9010.
- Made other minor changes to the ports and volumes used in the configuration.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2067#issuecomment-2646579129) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested a change to the codebase to improve the flexibility of the evaluation process. Specifically, they have added the ability to pass an instance of a custom `LLM` class to run the evaluations, providing more control and flexibility for customized evaluation logic. This enhancement allows users to define*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646469809) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that the error might be caused by using `\n` in the code. They recommend replacing `\n` with a comma or using triple double quotes (`"""`) instead of single double quotes (`""`) when passing the string, which should resolve the issue.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2014#issuecomment-2646308001) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested to set the `CREWAI_STORAGE_DIR` environment variable to specify the directory where CREW instances and memories should be stored. By doing so, all instances and memories will be created in the specified directory.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646302061) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that there may be an error in the way arguments are being passed to the tool. To help resolve this issue, they have requested the entire code to be shared for further examination.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2054#issuecomment-2646300138) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the complete code in the current thread for better visibility and easier access for everyone interested. This would provide a comprehensive overview of the code and its functionality, facilitating discussions and collaboration among individuals within the context of the current conversation.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2065#issuecomment-2646298829) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested exploring alternative solutions to Serper.dev, as there may be other tools that offer similar or more suitable functionality. It is recommended to evaluate the requirements and consider various options to find the best fit for the specific needs and preferences.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested a bug where port 9000, used by both ClickHouse and Minio, is already occupied by another system process that cannot be terminated. They attempted to change the port, but believe that port 9000 is also being used internally. When running the setup command via Docker Compose, the*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that in the linked CrewAI documentation, the embedder input should be `model_name` instead of `model`. This change should be made in several code examples provided:

* Using Azure OpenAI Embeddings
* Using Google AI Embeddings
* Using Vertex AI Embeddings
* Using Cohere Embeddings*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format option to the `output_log_file` for further analysis. This is partially related to issue #1970 and would enhance the file's parsability and usefulness in logging. @Vidit-Ostwal has expressed willingness to contribute a pull request for this feature.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the purpose of `use_vision set = True` when defining an agent. They inquire if using this setting redirects screenshots for processing by the multimodal LLM or if the extraction still relies on web scraping. @Vidit-Ostwal observed that setting `use_vision = True` only saves a .gif, but*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. The proposed solution addresses the problem accurately, ensuring it does not resurface in the future. Additionally, the fix is well-tested and has no adverse effects on other functionalities, suggesting a comprehensive and reliable solution.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested addressing the reset memories issue mentioned in issue #2023, but also proposes additional changes:

- Removing the CLI command for resetting memories.
- Updating the documentation.

@Vidit-Ostwal awaits confirmation that these changes align with the project's goals before implementing them.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in Issue #2030. This resolves the problem mentioned there, ensuring that the documentation accurately reflects the intended functionality. With this change, users can now rely on the updated documentation for guidance and clarity.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support for saving logs as a JSON file to the crew initialization process. By setting output_log_file to True or a file name and save_as_json to True, users can now easily capture logs in a structured JSON format, enabling simplified parsing and analysis.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the parse_run_traces function to include the last 4 letters of the run_id of the trace, resulting in a unique key for every call. This modification ensures that each call can be uniquely identified, resolving the issue of multiple calls sharing the same identifier.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
