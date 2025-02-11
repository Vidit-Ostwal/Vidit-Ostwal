# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the problem has been resolved by changing the Docker port. Specifically, they altered the ClickHouse port from 9000 to 9005. This seemingly minor adjustment was sufficient to rectify the issue.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may arise from a security process running on port 9000. This process cannot be terminated, which prevents the program from running on that port.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that they have just tried running the code again. They shared the logs from Redis, PostgreSQL, ClickHouse, MinIO, LangFuse, and other services. The logs indicate that all services are running properly, but LangFuse is encountering an error while applying ClickHouse migrations. The error message is "[hello] unexpected*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has updated the code to address a previous issue but continues to encounter the same problem. The updated code includes changes to the ports for ClickHouse and Minio: - `CLICKHOUSE_MIGRATION_URL`: Previously `http://clickhouse:9009`, now `http://clickhouse:8123`. - `CLICKHOUSE_URL`: Previously `http://clickhouse:8123`, now `http://clickhouse:8123`. - `LANGFUSE_S3_EVENT_UPLOAD_ENDPOINT`: Previously `http://minio:9010`, now `http://minio:9010`. - `LANGFUSE_S3_MEDIA_UPLOAD_ENDPOINT`: Previously*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2067#issuecomment-2646579129) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested a PR to address the issue, enabling passing an instance of the `LLM` class to execute evaluations. This modification enhances the flexibility and adaptability of the evaluation process.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646469809) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may be due to the `\n` character being passed. They recommend replacing it with a comma `,` or using triple quotation marks `"""` instead of single quotation marks `""` for the string containing the names. They believe this modification should resolve the problem.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2014#issuecomment-2646308001) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that they were unable to comprehend the intent of the original comment. However, they successfully set the `CREWAI_STORAGE_DIR` environment variable, resulting in the creation of crew instances and memories in the specified directory as defined in the `.env` file.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646302061) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that there might be an error in how the argument is being passed to the tool. To help troubleshoot the issue, they have requested the sharing of the entire code.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2054#issuecomment-2646300138) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the complete code for the project here. This would provide a more comprehensive understanding of the project's implementation and allow others to easily replicate the results or contribute to its development.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2065#issuecomment-2646298829) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested exploring alternative options to Serper.dev. They believe that a combination of tools and techniques can effectively fulfill the same functions as Serper.dev. This includes utilizing a combination of APIs, web scraping techniques, and SEO tools to gather and analyze search engine results.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested addressing a bug where both ClickHouse and MinIO use port 9000, which is already occupied by another system process. They request assistance in identifying all instances where port 9000 is used internally, as changing the port in one location may not be sufficient to resolve the issue.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the documentation for the `embedder` function should use the parameter name `model_name` instead of `model` to match the function's actual parameter name. This change should be made consistently throughout the documentation, including examples for Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and Cohere Embeddings.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested a feature to add a JSON format option to the output_log_file. This would enhance the parsability of the log file and partially resolve issue #1970. @Vidit-Ostwal is willing to contribute a pull request for this feature.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested exploring the usage and implications of the `use_vision` parameter when defining an agent. They inquire about the distinction between using it and not using it, specifically regarding whether the screenshot is processed by the multimodal LLM or scraped for element-based decision-making. They also express uncertainty about the*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. The proposed changes aim to resolve the reported problem, ensuring that the functionality operates as intended. These modifications address the specific concerns outlined in the referenced issue, thereby improving the overall performance and stability of the application.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested some changes to address the reset memories issue from #2023:
- Remove the CLI command to reset memories.
- Make necessary documentation changes.

@Vidit-Ostwal is willing to make these changes if the proposed solution aligns with the team's requirements.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue mentioned in issue #2030. The provided fix will address the error that was causing the documentation to fail. This change will result in more accurate documentation and will improve the overall quality of the project.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a feature to the crew initialization process that enables saving logs in a JSON file format. By setting the "output_log_file" parameter to a file name and setting "save_as_json" to True, users can generate a .json file containing an array of JSON events. This simplifies the parsing*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested altering the parse_run_traces function to incorporate the last four characters of the trace's run_id. This adjustment ensures that each call has a distinct key, thereby enhancing uniqueness.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
