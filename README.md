# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2014#issuecomment-2646308001) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal suggests setting the environment variable `CREWAI_STORAGE_DIR` to specify the directory where crew instances and memories should be stored. This allows customizing the storage location and ensures that data is saved in the desired directory.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646302061) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that there's likely an error in how I'm passing arguments to the tool. They have requested me to share the entire code for further investigation.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2054#issuecomment-2646300138) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested to share the complete code for easier review. They believe it would be beneficial to have the entire code available for reference in the issue.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2065#issuecomment-2646298829) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal recommends exploring alternative solutions to Serper.dev. They suggest considering options like Google Search API, Bing Search API, or specialized tools for specific use cases. The choice of alternative depends on the specific requirements and budget of the user, and it's advised to evaluate each option carefully to determine the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2644717512) in [crewAIInc/crewAI] on 2025-02-08.
  > *AI Summary: @Vidit-Ostwal has suggested resolving the aforementioned issue by implementing the changes proposed in the provided PR and requests the issue be closed if the proposed solution is effective.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2644714108) in [crewAIInc/crewAI] on 2025-02-08.
  > *AI Summary: @Vidit-Ostwal suggests that when a generator object is created due to yielding a value, the actual value can be obtained by iterating over the generator. He provides an example where a flow generates a random city and then a fun fact about that city. The code uses yielding to pass*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2055#issuecomment-2643704539) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may have been fixed in a recent update. They recommend updating the crew version and checking out PR #2055 for additional information.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2643616523) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested that with the emergence of more agentic frameworks, built-in evaluations for CrewAI could become a valuable addition. These evaluations would assess tool outputs, agent performance, and task results based on specific criteria such as factual accuracy. They also mentioned the work of RAGAS in structured evaluations for*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2641883649) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested expanding the 'get_crew' functionality to make it a CLI command directly linked with the current crew instance. They believe this would be more efficient and user-friendly.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might be due to differences in how `reset_memory_command` initializes `short_term_memory` and `entity_memory` from the CLI compared to how they are initialized in `crew.py`. While `reset_memory_command` works for `long_term_memory` and `knowledge_memory`, it may not work for `short_term_memory` and `entity_memory` if they require custom initialization. The*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the port 9000 used by ClickHouse and MinIO is already in use, causing issues with setting up LangFuse via Docker Compose. They believe the port is used internally elsewhere. The error message indicates a failure to open the database. @Vidit-Ostwal requests guidance on where other port*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the input parameter for the embedder should be `model_name` instead of `model` in the documentation. This is suggested for:

- Azure OpenAI embeddings
- Google AI embeddings
- Vertex AI embeddings
- Cohere embeddings*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding JSON format support to the output log file. The current .txt format is not parsable, limiting analysis capabilities. By enabling JSON logging, further analysis becomes possible. This suggestion partially addresses issue #1970. @Vidit-Ostwal expresses willingness to contribute by submitting a pull request.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested addressing the following: The purpose of `use_vision` set to `True` when defining an agent is unclear. It's not known if screenshots go to the multimodal LLM for parsing or if elements are still scraped and decisions made based on that. The only noticeable difference with `use_vision =*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2023, which addresses the reset memory problem. However, there are additional changes that need to be made, including:
- Removing the CLI command that resets memories
- Updating documentation

@Vidit-Ostwal is willing to implement these changes once the solution's alignment is confirmed.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in issue #2030. They have not provided any specific details about the changes made or the nature of the fix.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file when initializing Crew. Users can now set output_log_file to a file name or True, and enable save_as_json to True. This will generate a .json file containing an array of JSON events, simplifying parsing and manipulation.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested a change in the #1871 pull request. The parse_run_traces function has been modified to incorporate the last 4 letters of the run_id for each trace. This modification guarantees that every function call has a unique key, resolving the issue of potential duplicate keys.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to specify the indexed sample causing an issue. This improvement will provide more detailed information when encountering issues, aiding in efficient debugging and resolution.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
