# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that changing the docker port from 9000 to 9005 resolved the issue. This change was applied to the ClickHouse port, which was originally set at 9000. The solution was found after changing the port number, demonstrating that the issue stemmed from an incorrect port configuration.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may stem from a security process running on port 9000. This process is preventing the desired operation on that port and cannot be terminated.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the logs for the Redis, PostgreSQL, ClickHouse, MinIO, LangFuse, and other components, have been updated.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested updating the `docker-compose.yml` file to resolve a persistent issue. They have modified the ports for both ClickHouse (`9009`) and MinIO (`9010`) in the `environment` section for `clickhouse` and `minio` services, respectively. The updated code is provided in the comment. If the problem persists, @Vidit-Ostwal recommends examining other*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2067#issuecomment-2646579129) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested a solution to the issue by creating a PR that allows passing an instance of an `LLM` class to run the evals. This change enables greater flexibility and control over the evaluation process.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646469809) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might be arising from the "\n" character in the string. They recommend replacing it with a comma or using triple quotation marks (""") instead of single quotation marks (""). These changes should resolve the problem with the string.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2014#issuecomment-2646308001) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue faced by @paarttipaabhalaji might be due to a misunderstanding. They have mentioned that they set the `CREWAI_STORAGE_DIR` environment variable and created the crew instance and memories in the specified directory. This suggests that the issue could be related to the configuration or usage of*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646302061) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that there might be an error in how the argument is passed to the tool. To help debug the issue, @Vidit-Ostwal has requested that the entire code be shared.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2054#issuecomment-2646300138) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the complete code snippet in the thread. This would provide context and allow for a more comprehensive understanding of the issue being discussed. The code should be shared directly in the thread rather than referring to an external link. This will ensure that all participants have*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2065#issuecomment-2646298829) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested exploring alternatives to Serper.dev, as it may not be the best option for all use cases. Some potential alternatives include: - **Google Custom Search API:** An official API from Google that allows you to customize and control your search experience. - **Algolia:** A powerful search and discovery*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that there is an issue while setting up langfuse via docker-compose. The port 9000, on which both clickhouse and minio listen, is already in use by a different system process that cannot be killed. Additionally, changing the port in the configuration did not resolve the issue, suggesting*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the documentation for memory should be updated to replace the `model_name` parameter with `model` in the input to the embedder. This is because the sample code examples given in the documentation currently use `model` instead of `model_name`. The specific documentation pages that need to be updated*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding JSON format to the logging file named output_log_file to enhance its parsability and enable further analysis. This change will partially address issue #1970. @Vidit-Ostwal is willing to contribute a pull request for this enhancement.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested looking into the `use_vision` parameter when defining an agent. They question its purpose, specifically whether it triggers multimodal processing of images or if the image is still analyzed through element scraping. While enabling `use_vision` results in a saved .gif, the output content appears unchanged. They also inquire*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. Unfortunately, the comment does not provide any details about the suggested fix. I recommend reviewing the commit associated with this comment or reaching out to @Vidit-Ostwal for more information.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the reset memories issue mentioned in issue #2023. To do this, they recommend removing the CLI command for resetting memories and making necessary documentation changes. They are willing to make these additional changes if the proposed solution aligns with the overall project goals.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in issue #2030. The exact details of the fix are not specified in the comment, but it can be assumed that the changes address the concerns outlined in the original issue report.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support for saving logs as a JSON file. By setting output_log_file to True or specifying a file name, and enabling save_as_json, logs can be saved in a JSON format. This makes it easier to parse and work with the logs, as they are stored in an*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested an alteration to the parse_run_traces function by incorporating the last four characters of the run ID into the trace. This approach generates a distinctive key for each function invocation. The change ensures that every call has a unique identifier, enhancing precision and traceability.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
