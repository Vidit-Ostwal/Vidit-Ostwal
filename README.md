# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested exploring incorporating a crew within a tool. The tool would have the capability to initiate a crew, which would be managed by a parent crew. Additionally, some parent agents would be included.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested providing more control to users by allowing them to manage pre-computed templates or generalized managers rather than relying solely on default configurations. This would enable users to customize and adapt the templates to their specific needs, resulting in greater flexibility and control over the generated content.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that `human_input` is used after the task to ask for feedback on the generated response. Incorporating additional context during agent input may not be ideal. It is recommended to provide all necessary input during `crew.kickoff()` instead.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested including context and information about the agents or tools that the manager LLM can use. However, they have raised a concern that adding a "manager_note" specifically for the manager LLM might not be ideal, since it is essentially just another agent internally. An alternative suggestion is to*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that changing the Docker port resolved the issue. They had mistakenly set the ClickHouse port to 9000 but changing it to 9005 fixed the problem. They expressed gratitude to @Steffen911 for their assistance.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may arise due to a security process running on port 9000, preventing the application from functioning on that port. As a result, it is not possible to terminate the process and continue with the application's execution.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that logs from a series of container startup processes are included in the comment. These logs show successful startup of the Redis and PostgreSQL containers. However, there are multiple failed attempts at starting the Langfuse container due to the database being unavailable.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested to update the `docker-compose.yml` file to include updated ports for ClickHouse and Minio. The updated external port for ClickHouse is 9009, and the updated external port for Minio is 9010. They also noticed that the issue could be originating from an internal file, but they have not*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2067#issuecomment-2646579129) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested a code change via a pull request that enables passing an instance of the `LLM` class to execute evaluations. This modification addresses an existing issue.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646469809) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that the error may be caused by the `\n` character passed in the code. As a solution, they proposed replacing it with a comma. Additionally, they suggested using triple double quotes `"""` instead of single double quotes `""` when passing multiple names, like this: `"""Dr. Mihir Shah*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested revising the code to include contents in the GenerateContentRequest. The error occurred due to the absence of the contents parameter. No ML Ops Team is involved, and the LiteLLM version being used is 1.60.2.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested investigating an installation issue with Langfuse using Docker Compose. The problem arises from port 9000 being occupied by another process, causing conflicts with ClickHouse and Minio. Despite attempts to change the port, internal references to port 9000 persist. @Vidit-Ostwal seeks assistance in identifying all necessary port changes*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the input parameter in the CrewAI docs for the `embedder` should be `model_name` instead of `model`. This issue is present in examples for different embedding providers, including Azure OpenAI, Google AI, Vertex AI, and Cohere.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format option to the output_log_file for better parsability and further analysis. This would partially address issue #1970. @Vidit-Ostwal is willing to contribute a pull request.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested reviewing the purpose and functionality of `use_vision set = True` when defining an agent. They want to know if the screenshot is processed by the multimodal LLM for parsing or if it still relies on scraping elements. Additionally, they have found that the primary difference when using*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. However, no specific details about the fix are provided in the comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal suggests a solution that resolves the reset memory issue reported in #2023. To implement this fix, @Vidit-Ostwal proposes removing the CLI command for memory reset and updating the documentation accordingly. However, implementation is contingent on approval of the proposed solution.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue reported in #2030. The proposed changes address the specific concerns raised in that issue and provide clearer and more accurate information to users. By implementing these suggestions, the documentation will be improved, enhancing the user experience and reducing potential confusion.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs in JSON format. Users can now set `output_log_file` to `True` or provide a file name and set `save_as_json` to `True` to enable this feature. The generated JSON file includes an array of JSON events, simplifying parsing and handling.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the `parse_run_traces` function to incorporate the final four characters of each trace's `run_id`. This alteration generates a unique identifier for each function call.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
